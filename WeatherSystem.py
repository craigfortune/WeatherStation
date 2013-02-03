from xml.dom import minidom
import urllib.request
import WeatherConditions

class WeatherSystem:

    def __init__(self, woeid):
        self.woeid = woeid
        self.xmlDoc = 0
        self.weatherLocation = 0
        self.weatherCode = 0
        self.weatherType = 0
        self.weatherDescription = 0
        self.lowTemp, self.highTemp = 0, 0

    def loadWeather(self):
        url = 'http://weather.yahooapis.com/forecastrss?u=c&w=' + self.woeid
        print('Url:', url)

        xmlFile = urllib.request.urlopen(url)
        self.xmlDoc = minidom.parse(xmlFile)

        self.gatherData()

    def gatherData(self):
        self.gatherWeatherLocation()
        self.gatherWeatherCode()
        self.gatherWeatherType()
        self.gatherWeatherDescription()
        self.lowTemp, self.highTemp = self.gatherWeatherTempLowHigh()

    def gatherWeatherLocation(self):
        yweatherForecastList = self.xmlDoc.getElementsByTagName('yweather:location') 
        self.weatherLocation = yweatherForecastList[0].attributes['city'].value
        
    def gatherWeatherCode(self):
        yweatherForecastList = self.xmlDoc.getElementsByTagName('yweather:forecast') 
        self.weatherCode = yweatherForecastList[0].attributes['code'].value

    def gatherWeatherType(self):
        self.weatherType = WeatherConditions.getWeatherCondition((int)(self.weatherCode))[1]

    def gatherWeatherDescription(self):
        self.weatherDescription = WeatherConditions.getWeatherCondition((int)(self.weatherCode))[0]

    def gatherWeatherTempLowHigh(self):
        yweatherForecastList = self.xmlDoc.getElementsByTagName('yweather:forecast') 
        weatherTempHigh = yweatherForecastList[0].attributes['high'].value
        weatherTempLow = yweatherForecastList[0].attributes['low'].value

        return weatherTempLow, weatherTempHigh

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
