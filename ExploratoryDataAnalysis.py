import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)

df = pd.read_csv('D:\\New folder\\extended_sample_data.csv')
print(df)

print(df.head(5)) # Display first 5 rows
print(df.info()) # Display information about the DataFrame
print(df.tail(5)) # Display last 5 rows
print(df.describe())   # Display summary statistics
print(df.dtypes)   # Display data types of each column
print(df.columns)  # Display column names
print(df.rename(columns={"LastName":"SurName",})) # Rename column 'LastName' to 'SurName'
print(df.shape) # Display the shape of the DataFrame
print(df.size) # Display the size of the DataFrame
# bar diagram
df=df.head(10)
duplicate_rows_df = df[df.duplicated()] # Find duplicate rows
print("number of duplicate rows: ", duplicate_rows_df.shape) # Display number of duplicate rows
df_clean = df.dropna(subset=["FirstName", "Salary"]) 
plt.figure(figsize=(12,8))
plt.bar(df_clean["FirstName"], df_clean["Salary"], color="green") 
plt.xlabel("FirstName") # Set x-axis label
plt.ylabel("Salary") # Set y-axis label
plt.title("Salary by Name") # Set plot title
plt.xticks(rotation=90) # Rotate x-axis labels for better readability
plt.tight_layout() # Adjust layout to prevent clipping of tick-labels
plt.show() # Display the plot
# box plot
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Salary'])
plt.show()
# calculating IQR
df= df.select_dtypes(include=['int64', 'float64'])
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print("IQR for int columns:")
print('IQR for float columns:')
print(IQR)
# pie chart
df=df.head(5)
print(df.isnull().sum())
df=df.dropna()
df.count()
plt.figure(figsize=(8, 8))
plt.pie(df['Salary'], labels=df['ID'], autopct='%1.1f%%')
plt.title('Pie Chart from CSV Data')
plt.axis('equal')
plt.show()
