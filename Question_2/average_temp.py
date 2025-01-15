### Average_temp:
import pandas
# Create a function to calculate the average temperatures of all stations in spring across all years:
def spring_average_temp():
    # Create a list to contain all the temperatures of all stations in spring across all years:
    spring_average_temps = []
    # Looping through all years and putting all temperatures recorded in spring
    # across all years into spring_average_temps:
    for year in range(1986,2006):
        in_year = pandas.read_csv(f'temperature_data/stations_group_{year}.csv')
        for index, row in in_year.iterrows():
                temperatures = row[['January', 'February', 'March']].tolist()
                for each in temperatures:
                    spring_average_temps.append(each)
    # By using return function, it will return the result of this calculation about the average
    # temp in spring across all years when we call this function:
    return sum(spring_average_temps) / len(spring_average_temps)

#Continuing to do the same with other seasons:
def summer_average_temp():
    summer_average_temps = []
    for year in range(1986,2006):

        in_year = pandas.read_csv(f'temperature_data/stations_group_{year}.csv')
        for index, row in in_year.iterrows():
                temperatures = row[['April', 'May', 'June']].tolist()
                for each in temperatures:
                    summer_average_temps.append(each)
    return sum(summer_average_temps) / len(summer_average_temps)

def autumn_average_temp():
    autumn_average_temps = []
    for year in range(1986,2006):

        in_year = pandas.read_csv(f'temperature_data/stations_group_{year}.csv')
        for index, row in in_year.iterrows():
                temperatures = row[['July', 'August', 'September']].tolist()
                for each in temperatures:
                    autumn_average_temps.append(each)
    return sum(autumn_average_temps) / len(autumn_average_temps)

def winter_average_temp():
    winter_average_temps = []
    for year in range(1986,2006):

        in_year = pandas.read_csv(f'temperature_data/stations_group_{year}.csv')
        for index, row in in_year.iterrows():
                temperatures = row[['October', 'November', 'December']].tolist()
                for each in temperatures:
                    winter_average_temps.append(each)
    return sum(winter_average_temps) / len(winter_average_temps)

# Calling all 4 created functions to calculate the average temp across all years:
sum = spring_average_temp() + summer_average_temp() + autumn_average_temp() + winter_average_temp()
avg_temp = sum / 4

# open the file in order to show the result:
with open('average_temp.txt','w') as average_temp:
    average_temp.write(f'The average temp across all years is: {avg_temp}')

# These lines below are made to help you clear the result if you need to run multiples times:
# with open('average_temp.txt','w') as clear:
#     clear.write('')







