import pandas
## The coolest and the warmest
def finding_out_the_best():
   # Looping through each year data:
   for year in range(1986, 2006):
        list_of_cool = {}
        list_of_warm = {}
        # These variables will hold the values which will be added into the result file later:
        warm_temp = 0
        cool_temp = 0
        the_coolest_station = ""
        the_warmest_station = ""

        in_year = pandas.read_csv(f'temperature_data/stations_group_{year}.csv')
        #Looping through the datas of each year:
        for index, row in in_year.iterrows():
            # Taking out and put these datas into variables to hold the values for use:
            station_name = row['STATION_NAME']
            temperatures = row[['January', 'February', 'March', 'April', 'May', 'June',
                                        'July', 'August', 'September', 'October', 'November', 'December']].tolist()

            # Creating variables for comparison:
            max_temp = 0
            min_temp = float(row['January'])
            # Looping through the list created earlier to find out the highest and lowest temp of a station:
            for temp in temperatures:
                 if temp > max_temp:
                    max_temp = temp
            for temp in temperatures:
                if temp < min_temp:
                    min_temp = temp
            # After finishing finding, adding these numbers to lists for the next steps:
            list_of_cool[station_name] = min_temp
            list_of_warm[station_name] = max_temp
            # These variables will temporarily hold the values because the lowest temp of adelaide kent town can not be
            # called outside the loop:
            the_warm_station = ""
            warm = 0
            the_cool_station = ""
            cool = list_of_cool['ADELAIDE-KENT-TOWN']
            # looping through and adding the numbers into the variables for saving the values:
            for station,temps in list_of_warm.items():
                if temps > warm:
                    warm = temps
                    warm_temp = warm
                    the_warm_station = station
                    the_warmest_station = the_warm_station
            for station,temps in list_of_cool.items():
                if temps < cool:
                    cool = temps
                    cool_temp = cool
                    the_cool_station = station
                    the_coolest_station = the_cool_station
        # Adding values to the result file:
        with open('warmest_and_coolest_station.txt','a') as warm_cool:
            warm_cool.write(f' {year} {the_warmest_station}: {warm_temp}, {the_coolest_station}: {cool_temp}\n ')


finding_out_the_best()
# These lines below are made to help you clear the result if you need to run multiples times:
# with open('warmest_and_coolest_station.txt','w') as clear:
#     clear.write('')