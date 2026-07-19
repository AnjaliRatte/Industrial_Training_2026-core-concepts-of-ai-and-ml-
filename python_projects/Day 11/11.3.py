import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

# 1. Write a Pandas program to read a csv file from a specified source and print the first 5 rows.
# print(diamonds.head(5))

# 2. Write a Pandas program to read a dataset from diamonds DataFrame and modify
#    the default columns values and print the first 6 rows.
# diamonds=diamonds.rename(columns={"carat":"CARAT","cut":"CUT","color":"COLOR","clarity":"CLARITY","depth":"DEPTH","table":"TABLE","price":"PRICE","x":'X','y':'Y','z':'Z'})
# print(diamonds.head(6))

# 3. Write a Pandas program to select a series from diamonds DataFrame. Print the content of the series.
# serie = diamonds["carat"]
# print(serie)

# 4. Write a Pandas program to create a new 'Quality -color' Series
#    (use bracket notation to define the Series name) of the diamonds DataFrame.

# 5. Write a Pandas program to find the number of rows and columns and data type of each column of diamonds Dataframe.
# print(diamonds.shape,diamonds.dtypes)

# 6. Write a Pandas program to summarize only 'object' columns of the diamonds Dataframe.
# print(diamonds.describe(include=["object"]))

# 7. Write a Pandas program to rename two of the columns of the diamonds Dataframe.
# diamonds = diamonds.rename(columns={"x":'X','y':'Y'})
# print(diamonds.columns)

# 8. Write a Pandas program to rename all the columns of the diamonds Dataframe.
# diamonds=diamonds.rename(columns={"carat":"CARAT","cut":"CUT","color":"COLOR","clarity":"CLARITY","depth":"DEPTH","table":"TABLE","price":"PRICE","x":'X','y':'Y','z':'Z'})
# print(diamonds.head(6))

# 9. Write a Pandas program to remove the second column of the diamonds Dataframe.
# diamonds=diamonds.drop(columns=diamonds.columns[1])
# print(diamonds.columns)

# 10. Write a Pandas program to remove multiple columns at once of the diamonds Dataframe
# diamonds=diamonds.drop(columns=[diamonds.columns[0],diamonds.columns[1],"table"])


# 11. Write a Pandas program to remove multiple rows at once (axis=0 refers to rows) from diamonds dataframe.
# diamonds=diamonds.drop(diamonds.index[:34],axis=0)
# print(diamonds.head())

# 12. Write a Pandas program to sort the 'cut' Series in ascending order (returns a Series) of diamonds Dataframe
# cut_series=diamonds["cut"].sort_values()
# print(cut_series)

# 13. Write a Pandas program to sort the 'price' Series in descending order (returns a Series) of diamonds Dataframe.
# price_series = diamonds["price"].sort_values(ascending=False)
# print(price_series)

# 14. Write a Pandas program to sort the entire diamonds DataFrame by the 'carat' Series in ascending and descending order.
# print(diamonds.sort_values("carat"))
# print(diamonds.sort_values("carat",ascending=False))

# 15. Write a Pandas program to filter the DataFrame rows to only show carat weight at least 0.3
# print(diamonds[diamonds["carat"]>=0.3])

# 16. Write a Pandas program to convert a python list to pandas series.
# ls=['a','b','c',1,2,3]
# print(pd.Series(ls))

# 17. Write a Pandas program to find the details of the diamonds where length>5, width>5 and depth>5.
# print(diamonds.query('x>5' and 'y>5' and 'z>5'))

# 18. Write a Pandas program to find the diamonds that are either Premium or Ideal.
# print(diamonds.query("cut == 'Ideal' or cut == 'Premium'"))

# 19. Write a Pandas program to find the diamonds that are with a Fair or Good or Premium.
# print(diamonds.query("cut=='Fair' or cut == 'Good' or cut == 'Premium'"))

# 20. Write a Pandas program to display all column labels of diamonds DataFrame.
# print(diamonds.columns)

# 21. Write a Pandas program to read only a subset of 3 rows from diamonds DataFrame.
# print(diamonds[1:4])
# print(diamonds.iloc[3:6,:])

# 22. Write a Pandas program to iterate through diamonds DataFrame.
# for i in diamonds:
#     for j in range(len(diamonds[i])):
#         print(diamonds[i][j])

# 23. Write a Pandas program to drop all non-numeric columns from diamonds DataFrame.
# print(diamonds.dtypes)0
# diamonds = diamonds.select_dtypes(exclude=["object", "string"])
# print(diamonds.head())

# 23. Write a Pandas program to drop all non-numeric columns from diamonds DataFrame.
# diamonds = diamonds.select_dtypes(exclude=["int","float"])
# print(diamonds.head())

# 25. Write a Pandas program to pass a list of data types to only describe certain types of diamonds DataFrame.
# dt = ["str","float"]
# print(diamonds.describe(include=dt))

# 26. Write a Pandas program to calculate the mean of each numeric column of diamonds DataFrame
# print(diamonds.mean(numeric_only=True))

# 27. Write a Pandas program to calculate the mean of each row of diamonds DataFrame
# print(diamonds.mean(axis=1,numeric_only=True))

# 28. Write a Pandas program to calculate the mean of price for each cut of diamonds DataFrame
# print(diamonds.groupby("cut")["price"].mean())

# 29. Write a Pandas program to calculate count, minimum, maximum price for each cut of diamonds DataFrame.
# print(diamonds.groupby("cut")["price"].agg(["count", "min", "max"]))
