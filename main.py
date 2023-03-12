import requests


api_url = 'https://api.open-meteo.com/v1/forecast?latitude=42.13&longitude=24.73&hourly=temperature_2m,apparent_temperature,rain,showers,snowfall'
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()

    temperature = data['hourly']['temperature_2m'].pop()
    apparent_temperature = data['hourly']['apparent_temperature'].pop()
    rain = data['hourly']['rain'].pop()
    showers = data['hourly']['showers'].pop()
    snowfall = data['hourly']['snowfall'].pop()

    print(temperature)
    print(apparent_temperature)
    print(rain)
    print(showers)