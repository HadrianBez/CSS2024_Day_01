# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:22:58 2024

@author: HadrianBezuidenhout
"""

import pandas as pd # Used for data manipulation and analysis

#file = pd.read_csv("country_data.csv") # Reads country_data
#file = pd.read_csv("iris.csv") # Reads iris
#file = pd.read_csv("diab_data.csv") # Reads diab_data

column_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]
file = pd.read_csv("housing_data.csv",names = column_names) # Reads housing_data


#file = pd.read_csv("insurance_data.csv",skiprows=5) # Reads insurance_data
# Insurance data gives error: ParserError: Error tokenizing data. C error: Inconsistant coloumn numbers (Use 'skiprows' function)

print(file)
#print(file.info()) # Summarises table properties
#print(file.describe()) # Summarises numerical data

# Storing Data
#B1 = 39
#B2 = 25
#B3 = 29
#B4 = 46
#B5 = 22
#B6 = 35
#B7 = 22
#B8 = 49
#B9 = 30
#B10 = 40
#B11 = 30

#print(B1)
#print(B2)
#print(B3)
#print(B4)
#print(B5)
#print(B6)
#print(B7)
#print(B8)
#print(B9)
#print(B10)
#print(B11)

# Using Lists
age = [30,40,30,49,22,35,22,46,29,25,39]
#print(age)

# Lists indexes start at 0 which has the value of 30
#print(age[0])
#print(age[1])
#print(age[10])

# This will give an error as there is no value at index 11
#print(age[11]) # List index out of range

# Basic Stats
#print(min(age))
#print(max(age))
#print(len(age))
#print(sum(age))
#average = sum(age)/len(age)
#print(average)

# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
#print(gender[0])
#print(gender[1])
#print(gender[2])
#print(gender[-1]) # [-1] is the Last value in list

# country list
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]
#print(country)
#print(country[0])
#print(country[5])

# Data Storage With Lists
#my_list = [42, -2021, 6.283,"tau", "node"]
#rint(my_list)
#print(my_list[:]) # prints whole list

#my_list.append("pi")
#print(my_list)

#my_list.insert(1,"pi2")
#print(my_list)

#my_list.remove("pi")
#my_list.remove("pi2")
#my_list.remove("tau")
#print(my_list)
#print(len(my_list))

# View a certain range of items:
#print(my_list[0:3])

# Dictionaries
#d = {'key1': 'value1', 'key2': 'value2'} # Syntax for creating dictionary
person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
#print(person['name']) # 'John Doe'
#print(person.get('age')) # 30
person['phone'] = '555-555-5555'

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Displaying the DataFrame
#print(df)

# Accessing specific columns
#print(df['age'])
#print(df['gender'])

# Basic statistics
#print(df['age'].min())
#print(df['age'].max())
#print(df['age'].mean())

# Filtering data
#print(df[df['age'] > 30])

# Slicing rows and columns
#print(df[1:4])  # Select rows 1 to 3 and all columns

# Adding a new column
#df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#print(df)

# Removing a column
#df.drop(columns=['new_column'], inplace=True)
#print(df)