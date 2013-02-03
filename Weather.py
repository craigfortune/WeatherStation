import WeatherSystem

# Where On Earth ID (Default is Manchester, UK)
woeid = '27550089'
# Create WeatherSystem object and pass woeid
weatherObject = WeatherSystem.WeatherSystem(woeid)
#Load and then display weather data
weatherObject.loadWeather()
weatherObject.displayWeather()
