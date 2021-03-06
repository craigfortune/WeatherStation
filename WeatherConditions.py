# Weather conditions
# Index is Yahoo Weather Code
# Each element is a tuple of the Yahoo Weather description for the code and
# a more 'generic type', useful for knowing what icon to display etc
condition = [0] * 48
condition[0]='tornado', 'wind'
condition[1]='tropical storm', 'wind'
condition[2]='hurricane', 'wind'
condition[3]='severe thunderstorms', 'rain'
condition[4]='thunderstorms' 'rain'
condition[5]='mixed rain and snow', 'snow'
condition[6]='mixed rain and sleet' 'rain'
condition[7]='mixed snow and sleet' 'snow'
condition[8]='freezing drizzle', 'rain'
condition[9]='drizzle', 'rain'
condition[10]='freezing rain', 'rain'
condition[11]='showers', 'rain'
condition[12]='showers', 'rain'
condition[13]='snow flurries', 'snow'
condition[14]='light snow showers', 'snow'
condition[15]='blowing snow', 'snow'
condition[16]='snow' ,' snow'
condition[17]='hail', 'snow'
condition[18]='sleet', 'rain'
condition[19]='dust', 'fog'
condition[20]='foggy', 'fog'
condition[21]='haze', 'fog'
condition[22]='smoky', 'fog'
condition[23]='blustery', 'wind'
condition[24]='windy', 'wind'
condition[25]='cold', 'clear'
condition[26]='cloudy', 'cloud'
condition[27]='mostly cloudy (night)', 'cloud'
condition[28]='mostly cloudy (day)', 'cloud'
condition[29]='partly cloudy (night)', 'cloud'
condition[30]='partly cloudy (day)', 'cloud'
condition[31]='clear (night)', 'clear'
condition[32]='sunny', 'clear'
condition[33]='fair (night)', 'clear'
condition[34]='fair (day)', 'clear'
condition[35]='mixed rain and hail', 'rain'
condition[36]='hot', 'clear'
condition[37]='isolated thunderstorms', 'rain'
condition[38]='scattered thunderstorms', 'rain'
condition[39]='scattered thunderstorms', 'rain'
condition[40]='scattered showers', 'rain'
condition[41]='heavy snow', 'snow'
condition[42]='scattered snow showers', 'snow'
condition[43]='heavy snow', 'snow'
condition[44]='partly cloudy', 'cloud'
condition[45]='thundershowers', 'rain'
condition[46]='snow showers', 'snow'
condition[47]='isolated thundershowers', 'rain'

# Returns whole conditions list
def getWeatherConditionsList():
    return condition

# Returns a tuple taking Yahoo Weather ID as argument
def getWeatherCondition(code):
    return condition[code]
