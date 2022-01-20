## Notes

### Principles
[The 5 Most Important Principles of Data Visualization](https://towardsdatascience.com/the-5-most-important-principles-of-data-visualization-455225a6c4b3#:~:text=Data%20visualization%2C%20in%20the%20simplest,understand%20patterns%20and%20communicate%20insights.&text=Misleading%2C%20confusing%2C%20and%20impractical%20visualizations,designers%20and%20journalists%20among%20us.)

1. Tell the truth
2. Know your audience
3. Choose the right chart
4. Emphasize the most important facts
5. Form should follow function

### Chart Types
[Tableau - Types of Charts and Graphs](https://www.tableau.com/learn/whitepapers/which-chart-or-graph-is-right-for-you)
* Pie Chart: powerful for adding detail to other visualizations
* Bar chart: compare data across categories, highlight differences, show trends and outliers, and reveal historical highs and lows at a glance.
  * Common mistake: [adjust your starting axis](https://uxdesign.cc/the-most-common-mistake-designers-make-when-adjusting-their-bar-charts-6f7405d69703) 
    * Problem: change the comparison points that people can make between the categories
    * Solution: horizontal bar chart; rethink the visualization message
* Line Chart: visualize changes in one value relative to another
* Maps: show how location correlates with trends in your data
* Density Maps: identify locations with greater or fewer numbers of data points
* Scatter Plot: investigate the relationship between different variables, showing if one variable is a good predictor of another, or if they tend to change independently
* Gantt Chart: display a project schedule or show changes in activity over time
* Bubble Chart: add detail to scatter plots or maps to show the relationship between three or more measures
* Treemap: relate different segments of your data to the whole




[How to Choose the Right Type of Chart for Your Message](https://education.microsoft.com/en-us/course/0a60eeb6/1)
![](https://az801952.vo.msecnd.net/uploads/b9335f90-bb61-4773-899e-3927c923b9be.png)



### Tableau
#### [Row Level Security](https://www.thedataschool.com.au/mipadmin/row-level-security-in-tableau-using-user-functions/) vs [Column Level Security](https://www.thedataschool.com.au/mipadmin/column-level-security-in-tableau-uisng-user-functions/)
Row-Level Security restricts data access at the row level, whereas Column-Level Security restricts access at the column level.

[LinkedIn Learing: Using Tableau to Discover Powerful Business Insights](https://www.linkedin.com/learning/using-tableau-to-discover-powerful-business-insights)
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

* Joins, unions, blend
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






























