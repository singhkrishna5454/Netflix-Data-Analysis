#!/usr/bin/env python
# coding: utf-8

# In[223]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[224]:


Data=pd.read_csv("C:/Users/USER/Downloads/file (2).csv")
print(Data)


# # First Step is to Exmain the Dataset

# In[225]:


Data.head() # It is used to check the Starting 5 Data


# In[226]:


Data.shape # it is used to show the total no. of Rows and Columns


# In[227]:


Data.size # It is used to show total number of element in Dataset


# In[228]:


Data.columns # It is used to show the Column name in dataset


# In[229]:


Data.info() # to check the null value and their Data type


# # Task 1:- Find is there any Duplicate Record in this dataset? If yes,then remove the Duplicate Records.

# In[230]:


Data[Data.duplicated()] # Duplicate Function is used to check the duplicate value in the dataset


# In[231]:


Data.drop_duplicates(inplace=True) #  here we use Drop Duplicate function to remove the duplicate values form dataset 


# In[232]:


Data[Data.duplicated()] # now Duplicated function is again used to check the Duplicate values are remove or not hence it remove


# In[233]:


Data.shape


# # Task 2:- Is there sny null value present in any column? show with Heatmap.

# In[234]:


Data.isnull().sum()


# In[235]:


sns.heatmap(Data.isnull(),cmap='coolwarm')


# # Task 3:- For "House of cards",what is the show Id and who is the Director of this show?

# In[236]:


Data.head()


# In[237]:


Data[Data["Title"].isin(["House of Cards"])]


# From the above case the Show Id = s2833
#       And Director of this show = Robin Wright, David Fincher, Gerald McRaney, J...

# In[238]:


Data[Data["Title"].str.contains("House of Cards")]  


# From the above case the Show Id = s2833 
# 
# And Director of this show = Robin Wright, David Fincher, Gerald McRaney, J...
# 
# 
# We can use both of the function ".isin()" and ".str.contains()" to get the show id as well as Name of the Director

# # Task 4:- In which year highest number of the Tv show & movies were realsed ? Show with Bar graph. 

# In[239]:


Data.dtypes # here we check that Release_Date having the string data type so we have to change it into datetime data type 


# In[240]:


Data["date_N"] = pd.to_datetime(Data["Release_Date"], errors='coerce')


# In[241]:


Data.dtypes


# In[242]:


Data["date_N"].dt.year.value_counts() # it is used to show the occurance of the all the individual year in data column.


# In[243]:


Data["date_N"].dt.year.value_counts().plot(kind="bar") # we can use the above code to made the bar plot 

plt.title("Highest number of the Tv show & movies release respect to Year",color="r")
plt.xlabel("Year")
plt.ylabel("Number of Movies")

plt.show()


# From the above chart we can get the conclusion that highest number of movies with repect to year

# # Task 4:- How many Movies & Tv shows are in the Dataset? show with Bar Graph?

# In[244]:


# Here we can use the group by function to solve
Data.groupby("Category").Category.count()
print(a)


# In[245]:


c=["r","g"]
Data.groupby("Category").Category.count().plot(kind='bar',color=c)
plt.title("Number of Moives & TV Show in Dataset")
plt.show()


# From using the groupby function we can plot the bar graph 

# # Task 5:- Show all the movies that were released in year 2000

# In[246]:


# First we have to create new column to get only year form data_N column
Data["Year"]=Data["date_N"].dt.year


# In[247]:


Data.head()


# In[248]:


Data[ (Data["Category"]=="Movie") & (Data["Year"]==2020) ]


# By using the filter method we can get the data of Movies which released in Year 2020

# # Task 6:- Show only the Title of all TV Shows that were released in india

# In[249]:


Data[(Data["Category"]=="TV Show") & (Data["Country"]=="India")]["Title"]


# We use the filter method to get the Title of movies on above condition

# # Task 7:- Show top 10 Director, Who gave the highest number of TV Show & Movies to Netflix

# In[250]:


Data.head()


# In[251]:


Data["Director"].value_counts().head(10)


# We can use the count Function to get top 10 Director

# # Task 8:- Show all the records,Where"Category" wher Movies and type is comedies or Country is United Kingdom

# In[252]:


Data.head(2)


# In[253]:


Data[((Data["Category"]=="Movie") & (Data["Type"]=="Comedies")) | (Data["Country"]=="United Kingdom")]


# # Task 9:- In how many movies/shows, Tom cruise was cast?

# In[254]:


Data_new=Data.dropna() # it is used to drop all the null value from dataset


# In[255]:


Data_new.head(2)


# In[256]:


Data_new[Data_new["Cast"].str.contains("Tom Cruise")]


# I this case firstly we have to drop all the NaN values so for that we have to create the new dataset for exsiting data set after drop the Null values after the we can search with Str.contains() function to fetch the details 
# 
# In ths case Tom Cruise Cast only Two shows

# # Task 10:- What are the Different ratings defined by Netflix?

# In[257]:


Data_new["Rating"].unique()


# We can use the unique Function to get the diffrent Rating

# # Task 11:- How many Movies got the"TV-14" rating,in Canada?

# In[258]:


Data_new[(Data_new["Category"]=="Movie") & (Data_new["Rating"]=="TV-14") & (Data_new["Country"]=="Canada")]


# In[259]:


Data_new[(Data_new["Category"]=="Movie") & (Data_new["Rating"]=="TV-14") & (Data_new["Country"]=="Canada")].shape


# We can use the "And" operator to check the Movies who having rating of "TV-14" and Country is Canada

# # Task 12:- How many TV show got "R" rating, after year 2018

# In[260]:


Data[(Data["Category"]=="TV Show") & (Data["Rating"]=="R") & (Data["Year"]>2018)]


# We can use the "And" operator to check the TV Show who having rating of "R" and Year after 2018

# # Task 13:- what is the maximum Duration of a Movie/Show on Netflix?

# In[261]:


Data.head()


# In[262]:


Data["Duration"].unique()


# In[263]:


Data["Duration"].dtype # It is in string type so we have to change the Data type


# In[264]:


Data[["Minutes","Unit"]]=Data["Duration"].str.split(n=1, expand=True)
Data.head(2) # Here sperate the time and Unit we use here ".str.split" fuction to create the new column ("Minutes","Unit")


# In[265]:


Data["Minutes"].max()


# Here we can use the "unique" Function th check the duration and then we use the ".str.split()" Function the create two new column ("Minutes" , "Unit") to get the exact duration of Movies and at last we use the ".max()" Function th check the Maximum Duration of the movies on Netflix.

# # Task 14:- Which individual country has the Highest No. of TV shows?

# In[266]:


Data.head(2)


# In[267]:


Data_TV_Show=Data[Data["Category"]=="TV Show"]
Data_TV_Show.head(2)


# In[268]:


Data_TV_Show["Country"].value_counts().head(1)


# We have to create a new Dataset "Data_TV_Show" in which we add the specific Category "TV Show" and then we use the ".value_count()" Function and ".head()" to get the individual highest TV Show Country from Dataset 

# # Task 15:- How Can we sort the dataset by Year?

# In[274]:


Data.sort_values(by=["Year"]).head(2)


# We can use the ".sort_values()" function in respect to Year column to sort the Dataset

# # Task 16:- Find all the instances where:
#         
#         Category is "Movies" and Type is "Drama"
#         
#         or
#         
#         Category is "TV Show" and Type is "Kids TV"

# In[281]:


Data[((Data["Category"] == "Movie") & (Data["Type"] == "Dramas")) | ((Data["Category"] == "TV Show") & (Data["Type"] == "Kids TV"))]

