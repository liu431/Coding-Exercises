## Tableau Notes
Reference:

[LinkedIn Learing: Using Tableau to Discover Powerful Business Insights](https://www.linkedin.com/learning/using-tableau-to-discover-powerful-business-insights)

### Tableau basics

* Fundamental concepts of "right" visualization
  - Keep visualizations simple
  - Focus on the important metrics
  - Use the right visualization to uncover the trend

* 4 functions
  - Connect/join/union/blend to multiple types of data sources
  - Explore and analyze data quickly by creating charts and applying filters and analytic models
  - Share insights through basic visualizations or interactive dashboard
  - Enable user to analyze data, including aggregation, dimensions, measures, and types of fields

* Data types to connect to
  - A data file, such as csv, json, map, etc
  - Databases and servers, such as AWS, SQL Server, Salesforce

* Live vs. extracted data sources
  - Live: always use up-to-date data; can slow down performance, especially with large data
  - Extract: compressed snapshot of the underlying data source that is now stored on the user's computer's disk in the Tableau Repository folder; fast performance; doesn't rely on Internet; commonly used for weekly dashboards

* __Joins, unions, blend__
  - Joins: same amount of rows with wider data
  - Union: stack the two data sources with same fields on top of each other
  - Blend: use a common field as the linking field
  
[Join vs Blend](https://deep-r.medium.com/join-vs-blend-in-tableau-desktop-929fffe42c89)
![](https://miro.medium.com/max/1200/1*VJ_M5T4r7j6ojErChi3Ipg.png)

* Alias
Alllow you to change how the field values shows up in your visualization without altering the underlying data source

* [Dimensions vs. Measures](https://help.tableau.com/current/pro/desktop/en-us/datafields_typesandroles.htm)
  - Dimensions: contain qualitative values (such as names, dates, or geographical data); used to categorize, segment, and reveal the details in your data; affect the level of detail in the view.
  - Measures: contain numeric, quantitative values that you can measure; can be aggregated. When you drag a measure into the view, Tableau applies an aggregation to that measure (by default).

* Discrete vs. Continuous
  - Discrete field contains specific values. (blue color)
  - Continuous field exists on a spectrum. (green color)
  - Time can be both discrete and continuous, depending on analysis.

* [Level of Detail Expressions (LOD)](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm#how-to-create-lod-expressions)

Purpose: allow you to compute values at the data source level and the visualization level
  - FIXED: compute a value using the specified dimensions, without reference to the dimensions in the view
  - INCLUDE: compute values using the specified dimensions in addition to whatever dimensions are in the view
  - EXCLUDE: declare dimensions to omit from the view level of detail


* [Row Level Security](https://www.thedataschool.com.au/mipadmin/row-level-security-in-tableau-using-user-functions/) vs [Column Level Security](https://www.thedataschool.com.au/mipadmin/column-level-security-in-tableau-uisng-user-functions/)
Row-Level Security restricts data access at the row level, whereas Column-Level Security restricts access at the column level.



