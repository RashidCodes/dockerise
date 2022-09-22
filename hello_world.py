from art import tprint 
import os 
import requests

def main():

   # requester 
    name = os.environ.get("NAME")

   
    # get the temperature in your city 
    city = os.environ.get("CITY")
    api_key = os.environ.get("API_KEY")
    units = "metric"

    params = {
        "q": city,
        "units": units,
        "appid": api_key 
    }


    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather", params=params)


    if response.status_code == 200:
        weather_data = response.json()

        print("Hello World!")
        print("It's a wonderful day today")

        tprint(name)

        print(f"It is currently {weather_data.get('main').get('temp')} degrees celcius")

    else:
        raise Exception("Extracting weather api data failed")



if __name__ == '__main__':

    main()


