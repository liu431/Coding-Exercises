## Note on DBT (Data Building Tool)

[GitHub Repo](https://github.com/dbt-labs/dbt-core), [dbt Doc](https://docs.getdbt.com/docs/introduction), [Courses](https://courses.getdbt.com/collections), [Practical tips](https://medium.com/photobox-technology-product-and-design/practical-tips-to-get-the-best-out-of-data-building-tool-dbt-part-1-8cfa21ef97c5)

[Definiton](https://medium.com/the-telegraph-engineering/dbt-a-new-way-to-handle-data-transformation-at-the-telegraph-868ce3964eb4): command-line tool that enables data analysts and engineers to transform data in their warehouses simply by writing select statements.


## Who is an analytics engineer?
### Traditional data teams
* Data Engineer - maintain data infrastructure and the ETL process for creating tables and views (ETL, Orchestration, Python, Java, etc.) -> know how to build it
* Data Analyst - query tables and views to drive business insights for stakeholders (Dashboards, Reporting, Excel, SQL) -> know what to build

### ETL and ELT
* ETL: Extract, Transform, Load; require additional tools, languages, skills to orchestrate
* Data warehouses: combine a database and super computer for transforming data
* ELT: Extract, Load, Transform (in cloud data warehouse); noneed to extract and load repeatedly

### [Analytics Engineer](https://www.getdbt.com/what-is-analytics-engineering/)
* Focus on __T__: own the transformation of raw data up to the BI layer
* DE can focus on __E__ and __T__ of raw data and the larger data infrastructure
* DA can work to deliver dashboards and report to stakeholders

![](https://www.getdbt.com/ui/img/guides/analytics-engineering/analytics-engineer-role.png)

### Modern data stack
* Data sources
* Loaders
* Data platform: Snowflake, Redshift, BigQuery, Databricks
  * dbt workflow -> manage transformation, test and document
* BI tools (Tableau, Looker, mode, PowerBI)  / ML model / Operational Analytics

## Set up dbt cloud
* dbt CLI: a command line tool that can be run locally.
* dbt Cloud: a hosted version that streamlines development with an online Integrated Development Environment (IDE) and an interface to run dbt on a schedule.
* Redshift
  * Create new IAM Role to Redshift-Customizable that enables the AmazonRedshiftAllCommandsFullAccess
  * Under `Serverless configuration tab`, associate the role under `Permissions`








