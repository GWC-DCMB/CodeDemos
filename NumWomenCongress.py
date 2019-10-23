#!/usr/bin/env python3

####### Adapted from code by Pleuni Pennings https://github.com/pleunipennings/PlotNumWomenCongress

######## matplotlib

import matplotlib.pyplot as plt
import csv

      
def get_data():
    list_years = [] #create an empty list to store years
    list_num =[] #create an empty list to store the number of women
    linenum=0 #create a variable to count the lines, 
    with open("data/WomenCongress.csv") as file: #open the file with the data
        for line in file: #for each line
            data = line.split(",") #split the line at the commas (bc it is a csv file) 
            year = data[1][0:4] #take the first 4 characters from the second column as the year
            if linenum>0:  #do this, but not for the very first line
                list_years.append(int(year)) #append the year to the list of years
                list_num.append(int(data[2])) #append the number of women to the list for that
            linenum+=1 #update the counter for the number of lines
    return list_years,list_num # return the list for the years and the list for the number of women
    
list_years,list_num=get_data() #use the get_data function to get the list of years and the list of the number of women in congress

print(list_years[0]) #print statement to make sure it worked 

plt.plot(list_years, list_num, 'o') #plot year vs the number of women
plt.plot(list_years[-1], list_num[-1], 'ro')  #Highlight the last year (2019) in red
plt.suptitle('Number of Women in the US Congress', fontsize=16) #add a title
plt.show() # show the plot

############# pandas and dictionaries

import pandas as pd

#CSV to data frame
df=pd.read_csv("data/WomenCongress.csv")
df.head()


#Series vs Data Frame
type(df[["Congress"]]) #data frame
type(df["Congress"]) #series
type(df["Congress"][0])
df["Congress","Years"] #2 columns can't be a series, throws error
df[["Congress","Years"]] # 2 columns is a data frame

#iloc vs loc
df.iloc[0] #first row (this is a series)
df.iloc[0,0] #first row, first column (this is a string)
df.iloc[-1] #last row

#pandas data frame to dictionary
my_dict=df.to_dict()
my_dict.keys()
my_dict['Congress']
my_dict['Congress'][0]


