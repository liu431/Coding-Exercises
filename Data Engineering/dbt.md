## Note on DBT (Data Building Tool)

[GitHub Repo](https://github.com/dbt-labs/dbt-core), [dbt Doc](https://docs.getdbt.com/docs/introduction), [Courses](https://courses.getdbt.com/collections), [Practical tips](https://medium.com/photobox-technology-product-and-design/practical-tips-to-get-the-best-out-of-data-building-tool-dbt-part-1-8cfa21ef97c5)

[Definiton](https://medium.com/the-telegraph-engineering/dbt-a-new-way-to-handle-data-transformation-at-the-telegraph-868ce3964eb4): command-line tool that enables data analysts and engineers to transform data in their warehouses simply by writing select statements.

### Who is an analytics engineer?
#### Traditional data teams
* Data Engineer - maintain data infrastructure and the ETL process for creating tables and views (ETL, Orchestration, Python, Java, etc.) -> know how to build it
* Data Analyst - query tables and views to drive business insights for stakeholders (Dashboards, Reporting, Excel, SQL) -> know what to build

#### ETL and ELT
* ETL: Extract, Transform, Load; require additional tools, languages, skills to orchestrate
* Data warehouses: combine a database and super computer for transforming data
* ELT: Extract, Load, Transform (in cloud data warehouse); noneed to extract and load repeatedly

### [Analytics Engineer](https://www.getdbt.com/what-is-analytics-engineering/)
* Focus on __T__: own the transformation of raw data up to the BI layer
* DE can focus on __E__ and __T__ of raw data and the larger data infrastructure
* DA can work to deliver dashboards and report to stakeholders

![](https://www.getdbt.com/ui/img/guides/analytics-engineering/analytics-engineer-role.png)

#### Modern data stack
* Data sources
* Loaders
* Data platform: Snowflake, Redshift, BigQuery, Databricks
  * dbt workflow -> manage transformation, test and document
* BI tools (Tableau, Looker, mode, PowerBI)  / ML model / Operational Analytics

### Set up [dbt cloud](https://cloud.getdbt.com/)
* dbt CLI: a command line tool that can be run locally.
* dbt Cloud: a hosted version that streamlines development with an online Integrated Development Environment (IDE) and an interface to run dbt on a schedule.
* Redshift
  * Create new IAM Role to Redshift-Customizable that enables the AmazonRedshiftAllCommandsFullAccess
  * Under `Serverless configuration tab`, associate the role under `Permissions`
* [Github repo](https://github.com/liu431/dbt-fundamentals/tree/main)

### Models
* Modeling: shaping of the data from raw data through to your final transformed data; source tables -> intermediate tables/views -> final tables
* Traditional: star schema, Kimball, data vault
* Models in dbt: models are SQL select statements; under 'Models' directory in dbt project; 1-1 mapping relationship with a table or view in warehouse
* Build model
  * After constructing a model, dbt run in the command line will actually materialize the models into the data warehouse. The default materialization is a view. 
  * Run raw query -> created as view in warehouse
  * Run with config block at top -> created as table in warehouse

```sql
{{ config (materialized="table") }}
{{ config (materialized='view') }}
```

```sql
# build all models
dbt run
# build a specific model
dbt run -m
# run all models exist in models/staging
dbt run -s staging
```

* Modularity
  * degree to which a system's components may be separated and recombined, often with the benefit of flexibility and variety in use.
  * build a final product piece by piece rather than all at once 
  * each model is reusable for other downstream models

Ex. Modularize code 

`stg_customers.sql`
```sql
with customers as (
    select id as customer_id, first_name, last_name
    from raw.jaffle_shop.customers
)
select * from customers
```

`stg_orders.sql`
```sql
with orders as (
   select id as order_id, user_id as customer_id, order_date, status
    from raw.jaffle_shop.orders
)
select * from orders
```

`dim_customers.sql`
```sql
with customers as (
    select * from {{ ref('stg_customers')}}
),

orders as (
    select * from {{ ref('stg_orders') }}
),

customer_orders as (
    select
        customer_id,
        min(order_date) as first_order_date,
        max(order_date) as most_recent_order_date,
        count(order_id) as number_of_orders
    from orders
    group by 1
),

final as (
    select
        customers.customer_id,
        customers.first_name,
        customers.last_name,
        customer_orders.first_order_date,
        customer_orders.most_recent_order_date,
        coalesce(customer_orders.number_of_orders, 0) as number_of_orders
    from customers
    left join customer_orders using (customer_id)
)
select * from final
```

* `ref` Macro
  * to reference the underlying tables and views that were building the data warehouse
  * allow us to build dependencies between models in a flexible way that can be shared in a common code base
  * builds a lineage graph to determine dependencies between models


* Naming conventions
  * Sources (src): raw data that have been built in the warehouse through a loading process.
  * Staging (stg): 
    * models that are built directly on top of sources; 1-1 with source tables
    * used for very light transformations that shape the data into what you want it to be
    * used to clean and standardize the data before transforming data downstream
    * typically materialized as views.
  * Intermediate (int): any models that exist between final fact and dimension tables; always built on staging models
  * Fact (fct): things that are occuring or have occurred, such as events, clicks, votes; typically skinny, long tables.
  * Dimension (dim): such as people, places, customers, or thing

* Project organization
  * Marts: all intermediate, fact, and dimension models; subfolders to separate data by business function
  * Staging: staging models and source configurations; subfolders to separate data by data source

### Sources
* Represent the raw data that is loaded into the data warehouse
* Benefits: make updates in one place; visualize raw tables in your lineage
* The source function is used to build the dependency of one model to a source
* Source freshness
  * A threshold can be configured for giving a warning and an error with the keys warn_after and error_after.
  * The freshness of sources can then be determine with the command dbt source freshness. 

```sql
dbt source freshness
```

### [Tests](https://docs.getdbt.com/reference/node-selection/test-selection-examples)
* Make sure the data feeding into dashboard is reliable
* Allow us to make sure that the SQL transformations we write produce a model that meets our assertions.
* Singular test: specific queries that you run against your models; run on the entire model.
* Generic test: written in YAML; run on specific columns in a model
  * unique (every value in this column is unique) 
  * not_null (every value in this column is not null) 
  * accepted_values (every value in this column is a value from a given list) 
  * relationships (every value in this column exists in the column of another table); [referential integrity](https://en.wikipedia.org/wiki/Referential_integrity)

```sql
# test model
dbt test -s stg_orders
# test source data
dbt test --select source:jaffle_shop
# runs all tests in the dbt project
dbt test 
dbt test --select test_type:generic
dbt test --select test_type:singular
dbt test --select one_specific_model
```

### Documentation 
* Empower users to self-service questions about data and enables new team members to on-board quickly.
* DAG are automatically generated
* Add your own text descriptions

```sql
dbt docs generate
```

### Deployment
* Development: process of building, refactoring, and organizing different files in your dbt project
* Deployment: process of running dbt on a schedule in a deployment environment
* The use of development environments and branches makes it possible to continue to build your dbt project without affecting the models, tests, and documentation that are running in production.

















