# import modules
import requests
import json
import datetime
import pandas as pd

# CURRENT WEATHER DATA
# access weather website API
url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"hong kong","lat":"0","lon":"0","callback":"",
               "id":"2172797","lang":"en","units":"imperial","mode":"null"}

# 5 DAY / 3 HOUR FORECAST
url2 = "https://community-open-weather-map.p.rapidapi.com/forecast"

querystring2 = {"q":"hong kong","lat":"0","lon":"0","lang":"en","units":"metric",
                "mode":"null"}

# define function to streamline checking 5 day forecast
def day_forecast(index_start, index_end):
    import datetime
    import pandas as pd

    # output user entered city name
    print("*********************************")
    print("Weather information for", cityname)

    units2 = querystring2['units']
   
    # print weather information about city
    for i in range(index_start,index_end,1):
        
        data = {'Date': [datetime.datetime.fromtimestamp(condition[i]['dt'])],
                'Temp': [condition[i]['main']['temp']],
                'Humidity': [condition[i]['main']['humidity']],
                'Feels Like': [condition[i]['main']['feels_like']],
                'Condition': condition[i]['weather'][0]['description']}

        df = pd.DataFrame(data, columns=['Date', 'Temp', 'Humidity', 'Feels Like', 'Condition']) 
        print(df)

# define function to streamline whether user wants to check other days
def check_other_days():
    global answer3
    global answer4
    global answer5
    global keep_looping1
    answer4 = input("Would you like to check for other days? (y/n)")
    if answer4 == 'y':
        print("Please select a date from below.")
        print("NOTE: TIMES SHOWN ARE ALL LOCAL TIME SET ON COMPUTER")
        print("1)", dt, "to", my_date1)
        print("2)", my_date1, "to", my_date2)
        print("3)", my_date2, "to", my_date3)
        print("4)", my_date3, "to", my_date4)
        print("5)", my_date4, "to", my_date5)
        answer3 = int(input("Which days would you like to check?"))
        if answer3 == 1:
            day_forecast(0,8)
            check_other_days()
        elif answer3 == 2:
            day_forecast(8,16)
            check_other_days()
        elif answer3 == 3:
            day_forecast(16,24)
            check_other_days()
        elif answer3 == 4:
            day_forecast(24,32)
            check_other_days()
        elif answer3 == 5:
            day_forecast(32,40)
            check_other_days()
        else:
            print("Invalid input. Please try again.")
    elif answer4 == 'n':
        answer5 = input("Would you like to find the current weather instead? (y/n)")
        if answer5 == 'y':
            keep_looping1 = True
        elif answer5 == 'n':
            print("Thank you for using my app!")
            keep_looping1 = False
        else:
            print("Invalid input. Please try again.")
    else:
        print("Invalid input. Please try again.")
        
# START OF OUTPUT
print("WEATHER FORECAST APP -- CREATED BY AC")

# while loop - keep looping until user types valid input
keep_looping1 = True
while keep_looping1 == True:
    cityname = input("Please enter a city name: ")
    querystring["q"] = cityname

    # asks user to select whether to see current data or 5 day / 3 hour forecast
    print("1) Current Weather Data")
    print("2) 5 day / 3 hour forecast data")
    answer2 = int(input("Please type the number corresponding from the following options below."))

    # if user requests to see current weather data
    if answer2 == 1:
        
        # while loop - keep looping until user types valid input
        keep_looping2 = True
        while keep_looping2 == True:
        
            # ask user to display units in either imperial/metric
            units = input("Metric or Imperial units?")
            if (units == 'metric' or 'Metric'):
                querystring['units'] = units
                keep_looping2 = False
            elif (units == 'imperial' or 'Imperial'):
                querystring['units'] = units
                keep_looping2 = False
            else:
                print("Invalid Input. Please try again.")

            headers = {"X-RapidAPI-Key": "ce77154966msh073d05d9160d253p14878djsnb3ffba0cc934",
                       "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"}

            # get information based on user input - current forecast
            response = requests.request("GET", url, headers=headers, params=querystring)
            weather_app = json.loads(response.text)

            # code block below prints if city entered actually exists
            # prints weather information for city
            try:
                print("NOTE: TIMES SHOWN ARE ALL LOCAL TIME SET ON COMPUTER")
                print("*********************************")
                print("Weather information for", cityname)

                lon_lat = weather_app['coord']
                for key, value in lon_lat.items():
                    print(key,":",value)

                enviro = weather_app['weather']
                print("current_situation : ", enviro[0]['description'])

                temp = weather_app['main']

                for key, value in temp.items():
                    print(key, ":", value)

                print("visibility :", weather_app['visibility'])

                wind = weather_app['wind']
        
                for key, value in wind.items():
                    print(key, ":", value)
        
                sun = weather_app['sys']
                sun_rise = sun.get('sunrise')
                sun_set = sun.get('sunset')
                time_rise = datetime.datetime.fromtimestamp(sun_rise)
                time_set = datetime.datetime.fromtimestamp(sun_set)

                print("sunrise : ", time_rise.strftime('%Y-%m-%d %H:%M:%S'))
                print("sunset : ", time_set.strftime('%Y-%m-%d %H:%M:%S'))

                # while loop - keep looping until user types valid input
                keep_looping3 = True
                while keep_looping3 == True:
                    # ask user if they would like to input another city
                    answer = input("Would you like to find the weather of another city? (y/n) ")
                    if answer == 'y':
                        keep_looping3 = False
                        break
                    elif answer == 'n':
                        print("Thanks for using my app!")
                        keep_looping3 = False
                        keep_looping1 = False
                        break
                    else:
                        print("Invalid input. Please try again.")
                    
            # if city does not exist 
            except KeyError:
                print("Error. City not found!")
                print("Please try again.")

    # if user requests to see 5 day / 3 hour forecast
    elif answer2 == 2:

        # while loop - keep looping until user types valid input
        keep_looping4 = True
        while keep_looping4 == True:

            # ask user to select either metric or imperial units
            units2 = input("Metric or Imperial units?")
            if (units2 == 'metric' or 'Metric'):
                querystring2['units'] = units2
                keep_looping4 = False
            elif (units2 == 'imperial' or 'Imperial'):
                querystring2['units'] = units2
                keep_looping4 = False
            else:
                print("Invalid Input. Please try again.")

            # code block below prints if city entered actually exists
            # prints weather information for city
            try:
            
                # get information based on user input - 5d/3h forecast
                headers = {"X-RapidAPI-Key": "ce77154966msh073d05d9160d253p14878djsnb3ffba0cc934",
                           "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"}
                
                response = requests.request("GET", url2, headers=headers, params=querystring2)
                weather_app2 = json.loads(response.text)

                # ask user what 24 hour period to check weather
                from datetime import datetime, timedelta
                dt = datetime.now()
                td1 = timedelta(days=1)
                td2 = timedelta(days=2)
                td3 = timedelta(days=3)
                td4 = timedelta(days=4)
                td5 = timedelta(days=5)

                my_date1 = dt + td1
                my_date2 = dt + td2
                my_date3 = dt + td3
                my_date4 = dt + td4
                my_date5 = dt + td5
                    
                print("Please select a date from below.")
                print("NOTE: TIMES SHOWN ARE ALL LOCAL TIME SET ON COMPUTER")
                print("1)", dt, "to", my_date1)
                print("2)", my_date1, "to", my_date2)
                print("3)", my_date2, "to", my_date3)
                print("4)", my_date3, "to", my_date4)
                print("5)", my_date4, "to", my_date5)
                answer3 = int(input("Which days would you like to check?"))

                # organize dictionary to display weather information
                condition = weather_app2['list']

                # if/elif/else statements based on user input
                if answer3 == 1:
                    day_forecast(0,8)
                    check_other_days()
                elif answer3 == 2:
                    day_forecast(8,16)
                    check_other_days()
                elif answer3 == 3:
                    day_forecast(16,24)
                    check_other_days()
                elif answer3 == 4:
                    day_forecast(24,32)
                    check_other_days()
                elif answer3 == 5:
                    day_forecast(32,40)
                    check_other_days()
                else:
                    print("Invalid input. Please try again.")

            # if city does not exist 
            except KeyError:
                print("Error. City not found!")
                print("Please try again.")
                break

    # if user enters invalid input
    else:
        print("Invalid input. Please try again.")



