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

        self.windChill = 0
        self.windDirection = 0
        self.windSpeed = 0

        self.atmosphereHumidity = 0
        self.atmospherePressure = 0
        self.atmosphereVisibility = 0
        self.atmosphereRising = 0

        self.astronomySunrise = 0
        self.astronomySunset = 0

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
        self.gatherWind()
        self.gatherAtmosphere()
        self.gatherAstronomy()
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

    # Data on wind conditions
    def gatherWind(self):
        yweatherWindList = self.xmlDoc.getElementsByTagName('yweather:wind')
        self.windChill = yweatherWindList[0].attributes['chill'].value
        self.windDirection = yweatherWindList[0].attributes['direction'].value
        self.windSpeed = yweatherWindList[0].attributes['speed'].value

    # Atmospherics information
    def gatherAtmosphere(self):
        yweatherAtmosphereList = self.xmlDoc.getElementsByTagName('yweather:atmosphere')

        self.atmosphereHumidity = yweatherAtmosphereList[0].attributes['humidity'].value
        self.atmosphereVisibility= yweatherAtmosphereList[0].attributes['visibility'].value
        self.atmospherePressure = yweatherAtmosphereList[0].attributes['pressure'].value
        self.atmosphereRising = yweatherAtmosphereList[0].attributes['rising'].value

    # Sunrise and sunset times
    def gatherAstronomy(self):
        yweatherAstronomyList = self.xmlDoc.getElementsByTagName('yweather:astronomy')

        self.astronomySunrise = yweatherAstronomyList[0].attributes['sunrise'].value
        self.astronomySunset = yweatherAstronomyList[0].attributes['sunset'].value

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

            print('Weather wind chill:', self.windChill)

            print('Weather wind direction:', self.windDirection)
            print('Weather wind speed:', self.windSpeed)

            print('Weather atmosphere humidity', self.atmosphereHumidity)
            print('Weather atmosphere pressure', self.atmospherePressure)
            print('Weather atmosphere visibility', self.atmosphereVisibility)
            print('Weather atmosphere rising', self.atmosphereRising)

            print('Weather astronomy sunrise', self.astronomySunrise)
            print('Weather astronomy sunset', self.astronomySunset)
