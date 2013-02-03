from xml.dom import minidom
import urllib.request
import WeatherConditions

# Class that manages loading and parsing YahooWeather XML
class WeatherSystem:

    def __init__(self, woeid):
        self.woeid = woeid
        self.xmlDoc = 0
        self.weatherLocation = 0
        self.weatherCode = 0
        self.weatherType = 0
        self.weatherDescription = 0
        self.lowTemp, self.highTemp = 0, 0

    # Loads Yahoo Weather XML dependant on woeid passed on init
    # Defaulting to celcius
    # Call this again if you change woeid etc
    def loadWeather(self):
        url = 'http://weather.yahooapis.com/forecastrss?u=c&w=' + self.woeid
        print('Url:', url)

        # Loads up the xml and parses it
        xmlFile = urllib.request.urlopen(url)
        self.xmlDoc = minidom.parse(xmlFile)

        # Gathers all the relevant data from the xml loaded above
        self.gatherData()

    # Gathers each bit of useful data
    def gatherData(self):
        self.gatherWeatherLocation()
        self.gatherWeatherCode()
        self.gatherWeatherType()
        self.gatherWeatherDescription()
        self.lowTemp, self.highTemp = self.gatherWeatherTempLowHigh()

    # Location from woeid, in City format
    def gatherWeatherLocation(self):
        yweatherForecastList = self.xmlDoc.getElementsByTagName('yweather:location') 
        self.weatherLocation = yweatherForecastList[0].attributes['city'].value

    # Weather code from XML
    def gatherWeatherCode(self):
        yweatherForecastList = self.xmlDoc.getElementsByTagName('yweather:forecast') 
        self.weatherCode = yweatherForecastList[0].attributes['code'].value

    # Generic weather description
    def gatherWeatherType(self):
        self.weatherType = WeatherConditions.getWeatherCondition((int)(self.weatherCode))[1]

    # Yahoo's specific weather description
    def gatherWeatherDescription(self):
        self.weatherDescription = WeatherConditions.getWeatherCondition((int)(self.weatherCode))[0]

    # Returns a tuple of temperature, low/high
    def gatherWeatherTempLowHigh(self):
        yweatherForecastList = self.xmlDoc.getElementsByTagName('yweather:forecast') 
        weatherTempHigh = yweatherForecastList[0].attributes['high'].value
        weatherTempLow = yweatherForecastList[0].attributes['low'].value

        return weatherTempLow, weatherTempHigh

    # Simple data dump to display gathered data
    def displayWeather(self):
        print('Weather code:', self.weatherCode)
        if(self.weatherCode == 3200):
            print('Weather info unavailable')
        else:
            print('Weather location:', self.weatherLocation)
            print('Weather description:', self.weatherDescription)
            print('Weather type:', self.weatherType)
            print('Weather temp low:', self.lowTemp)
            print('Weather temp high:', self.highTemp)
