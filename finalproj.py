import json
import requests
from datetime import datetime
from forecast import WeatherCurrently
from forecast import WeatherHourly
from forecast import WeatherDaily

def world(c):
    if c ==1:
        response = requests.get("https://api.darksky.net/forecast/b2c3a8ba656716c04ae8ababa4681a60/40.7128,-74.0060") 
        NYcast = json.loads(response.text)
        return NYcast
    
    elif c ==2:
        response = requests.get("https://api.darksky.net/forecast/b2c3a8ba656716c04ae8ababa4681a60/-34.6037,-58.3816") 
        BAcast = json.loads(response.text)
        return BAcast

    elif c ==3:
        response = requests.get("https://api.darksky.net/forecast/b2c3a8ba656716c04ae8ababa4681a60/48.8566,2.3522") 
        PARcast = json.loads(response.text)
        return PARcast
    
    elif c ==4:
        response = requests.get("https://api.darksky.net/forecast/b2c3a8ba656716c04ae8ababa4681a60/30.0444,31.2357") 
        CAIcast = json.loads(response.text)
        return CAIcast
    
    elif c ==5:
        response = requests.get("https://api.darksky.net/forecast/b2c3a8ba656716c04ae8ababa4681a60/59.9311,30.3609") 
        StPcast = json.loads(response.text)
        return StPcast

    elif c ==6:
        response = requests.get("https://api.darksky.net/forecast/b2c3a8ba656716c04ae8ababa4681a60/-33.8688,151.2093") 
        SYDcast = json.loads(response.text)
        return SYDcast

    elif c ==7:
        longLat = input('Input a latitude and longitude:')
        LL = longLat.replace(" ", "")
        url = 'https://api.darksky.net/forecast/b2c3a8ba656716c04ae8ababa4681a60/'
        MYurl = url + LL
        response = requests.get(MYurl) 
        MYcast = json.loads(response.text)
        return MYcast
    
    else:
        print("Please enter a valid selection.")
        main()

def time(e):
    prettyDate = datetime.fromtimestamp(e).strftime('%Y-%m-%d %H:%M:%S')
    print(f'Date: {prettyDate}') 

def currentInfo(f):
    currentWeather = f.get('currently')
    precipType = currentWeather.get('precipType')
    precipIntensity = currentWeather.get('precipIntensity')
    precipProbability = currentWeather.get('precipProbability')
    precipProbability *= 100
    temperature = currentWeather.get('temperature')
    summary = currentWeather.get('summary')
    windSpeed = currentWeather.get('windSpeed')
    wc = WeatherCurrently(summary, precipType, precipIntensity, precipProbability, temperature, windSpeed)
    return wc

def hourlyInfo(f):
    print(" ")
    print("Here are the next two days:")
    print(" ")
    hourly = f.get('hourly')
    hourData = hourly.get('data')
    for i in hourData:
        summary = i.get('summary')
        epoch = i.get('time')
        time = datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')
        temperature = i.get('temperature')
        hw = WeatherHourly(time, summary, temperature)
        for i in range(1):
            print(hw,"\n---------------")

def dailyInfo(f):
    print(" ")
    print("Here is the next week:")
    print(" ")
    daily = f.get('daily')
    dayData = daily.get('data')
    for i in dayData:
        summary = i.get('summary')
        epoch = i.get('time')
        time = datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')
        high = i.get('temperatureHigh')
        low = i.get('temperatureLow')
        dw = WeatherDaily(time, summary, high, low)
        for i in range(1):
            print(dw,"\n---------------")
        
def newMenu(f):
    print("Select 1 for a different forecast\nSelect 2 for a different location\nSelect 3 to Exit")
    path = int(input())
    if path ==1:
        p = fCastMenu()
        castPath(p,f)
    elif path ==2:
        main()
    elif path ==3:
        print("Goodbye!")
    else:
        print("Please enter a valid selection.")
        newMenu(f)

def castPath(p,f):
    if p ==1:
        wc = currentInfo(f)
        print(wc)
        wc.precip()
        newMenu(f)
    elif p ==2:
        hourlyInfo(f)
        newMenu(f)
    elif p ==3:
        dailyInfo(f)
        newMenu(f)
    else:
        print("Please enter a valid selection.")  
        main()
        
def fCastMenu():
    print('Select 1 for the Current Weather\nSelect 2 for the Hourly Forecast\nSelect 3 for the Daily Forecast')
    path = int(input())
    return path

def menu():
    print("See the weather around the world!")
    print("Select 1 for New York\nSelect 2 for Buenos Aires\nSelect 3 for Paris\nSelect 4 for Cairo\nSelect 5 for St. Petersburg\nSelect 6 for Sydney\nSelect 7 to put in your own longitude and latitude!")
    city = int(input())
    return city

def main():
    city = menu()   
    forecast = world(city)
    path = fCastMenu()
    castPath(path, forecast)
    
    
    

if __name__ == "__main__":
    main()
