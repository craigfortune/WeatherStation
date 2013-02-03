import WeatherSystem

woeid = '27550089'
weatherObject = WeatherSystem.WeatherSystem(woeid)
weatherObject.loadWeather()
weatherObject.displayWeather()
