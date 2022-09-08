import requests
location_url="https://api.openweathermap.org/data/2.5/onecall?"
Api_key="4755325982738c34a9c35db12e244a18"
my_lat=-33.959976
my_long=18.504797
parameters={
    "lat":my_lat,
    "lon":my_long,
    "appid":Api_key,
    "exclude":"current,minutely,daily",
}
response=requests.get(url=location_url,params=parameters)
if response!=200:
    print(response.raise_for_status())
data=response.json()
weather_sliced=data["hourly"][:12]

will_rain=False

for hourly_data in weather_sliced:
    condition_code=hourly_data["weather"][0]["id"]
    if int(condition_code)>=700:
        will_rain=True
if will_rain==True:
    print("Please carry an umbrella")