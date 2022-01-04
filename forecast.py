class WeatherCurrently:

    def __init__(self, summary, precipType, precipIntensity, precipProbability, temperature, windSpeed):
        self.summary = summary 
        self.precipType = precipType
        self.precipIntensity = precipIntensity
        self.precipProbability = precipProbability
        self.temperature = temperature
        self.windSpeed = windSpeed

    def __repr__(self):
        return "It is " + str(self.summary) + " out. It is " + str(self.temperature) + " degrees. There is a " + str(self.precipProbability) + "%" + " chance of precipitation. There are " + str(self.windSpeed) + " mph winds."

    def precip(self):
        if self.precipProbability > 0:
            print("It might " + self.precipType + " " + str(self.precipIntensity) + " inches.")        

class WeatherHourly:

    def __init__(self, time, summary, temperature):
        self.time = time 
        self.summary = summary
        self.temperature = temperature

    def __repr__(self):
        return str(self.time) + " " + str(self.summary) + ", " + str(self.temperature) + " degrees."

class WeatherDaily:

    def __init__(self, time, summary, temperatureHigh, temperatureLow):
        self.time = time
        self.summary = summary
        self.temperatureHigh = temperatureHigh
        self.temperatureLow = temperatureLow

    def __repr__(self):
        return str(self.time) + " " + str(self.summary) + " High of " + str(self.temperatureHigh) + " degrees, low of " + str(self.temperatureLow) + " degrees."
