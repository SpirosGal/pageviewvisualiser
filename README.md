This project focuses on visualizing time series data using Python libraries such as Pandas, Matplotlib, and Seaborn. The dataset used contains daily page views for the freeCodeCamp.org forum from May 9, 2016, to December 3, 2019. 

The main goal is to create three different types of data visualizations: a line chart, a bar chart, and box plots, to understand the patterns in visits and identify yearly and monthly growth. 
This project provides valuable insights into the freeCodeCamp.org forum's page view trends over time and showcases proficiency in data visualization using Python.

Some things i learned along the way:

- datetime is a module in Python's standard library that provides classes and functions for working with dates and times. A datetime object consists of various components, including year, month, day, hour, minute, second, microsecond, and timezone information.
You can access and manipulate these components individually depending on your needs.

- FuncFormatter is a class provided by the matplotlib.ticker module in Python's Matplotlib library. It is used to customize the formatting of tick labels (the numeric labels on the axes) in a Matplotlib plot. You apply this FuncFormatter to a specific axis (X-axis or Y-axis) in your Matplotlib plot. It will use your custom formatting function to format the tick labels for that axis.
For instance, instead of displaying "1500000," it formats it as "1.5M" for better clarity on the Y-axis of your graph.

-groupby function in Python, often used with libraries like Pandas, is a powerful tool for grouping and aggregating data based on one or more columns in a dataset. It's a fundamental operation in data analysis and allows you to perform various summary and analysis tasks on your data. 
You can split the dataset into groups based on the values of one or more specified columns. Each unique value in the grouping column(s) forms a separate group.
Once the data is divided into groups, you can apply various aggregation functions to each group. 
After applying the aggregation functions, the results from each group are combined into a new data structure. This can be a Pandas DataFrame, Series, or another suitable data structure, depending on the specific operation.
