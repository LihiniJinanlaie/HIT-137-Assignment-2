import pandas

## The_largest_temp_range:
# Creating the function to find the station with the largest temp range:
def find_the_largest():
    # Looping through all years given:
    for year in range(1986, 2006):
        in_year = pandas.read_csv(f'temperature_data/stations_group_{year}.csv')
        # This dict will hold the keys, which are the station name and the values, which are the temp range
        # of each station:
        station_temperatures_range = {}
        # These variables will hold the value of the largest temp range and the station having that number:
        largest_temp_range = 0
        the_station = ''
        # Looping each row in the data of a year:
        for index, row in in_year.iterrows():
            # These row function will take the data that we need by typing the name of the column containing the datas that
            # we need
            station_name = row['STATION_NAME']
            temperatures = row[['January', 'February', 'March', 'April', 'May', 'June',
                                'July', 'August', 'September', 'October', 'November', 'December']].tolist()
            # Create variables for comparison in order to pick out the highest temp and the lowest temp for the
            # temp_range calculation
            max_temp = 0
            min_temp = float(row['January'])

            # Using for loop to find the highest and lowest temp:
            for temp in temperatures:
                if temp > max_temp:
                    max_temp = temp
            for temp in temperatures:
                if temp < min_temp:
                    min_temp = temp
            #Calculating the temp_range after finishing finding and add the temp_range to the dict created earlier:
            temp_range = round(max_temp - min_temp, 2)
            station_temperatures_range[station_name] = temp_range

            # Looping through the dict to find out the largest_temp_range:
            for station, temps in station_temperatures_range.items():
                if temps > largest_temp_range:
                    largest_temp_range = temps
                    the_station = station
        #After finishing finding the largest, add it to the file for showing the result:
        with open('largest_temp_range_station.txt', 'a') as the_largest:
            the_largest.write(f'{year} {the_station}: {largest_temp_range}\n')

find_the_largest()
# These lines below are made to help you clear the result if you need to run multiples times:
# with open('largest_temp_range_station.txt','w') as clear:
#     clear.write('')
