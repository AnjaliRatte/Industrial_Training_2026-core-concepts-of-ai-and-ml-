import pandas as pd

# Step 3. Use the tsv file and assign it to a dataframe called food
food = pd.read_csv("en.openfoodfacts.org.products.tsv",sep="\t",low_memory=False)

# Step 4. See the first 5 entries
# print(food.head())

# Step 5. What is the number of observations in the dataset?
# print("no of observations : ",food.shape[0]) # it gives no. of rows

# Step 6. What is the number of columns in the dataset?
# print("no of columns : ",food.shape[1])

# Step 7. Print the name of all the columns.
# print(food.columns)

# Step 8. What is the name of 105th column?
# print(food.columns[104])

# Step 9. What is the type of the observations of the 105th column?
# print(food.iloc[:,104].dtype)

# Step 10. How is the dataset indexed?
# print(food.index)

# Step 11. What is the product name of the 19th observation?
# print(food.loc[18,"product_name"])