import requests
from twilio.rest import Client
end_point ='http://api.openweathermap.org/data/2.5/forecast'
api_key = '2219e948758596432162abd48e48d0f2'
account_sid = 'ACce8bbe9b70198532eba9529fefab8df4'
auth_token = 'c5f6b4d4ddead246410d89ecdd4f0671'
weather_params = {
    'lat':17.385044,
    'lon':78.486671,
    'appid':api_key,
     'cnt' : 4
}
response = requests.get(end_point,params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code)>700:
        will_rain = True
if will_rain:
    #print('Bring an Umbrella')
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella ☂️ , because it's  raining outside ☔",
        from_='+14783758467',
        to='+91 9704383985'
    )
    print(message.sid)