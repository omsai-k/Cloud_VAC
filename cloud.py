import requests
import time


thingspeak_url = 'https://api.thingspeak.com/update'
api_key = 'D2J7V989ZP20PBO1' 


with open('C:/Users/omsai/Downloads/sensor_data.txt', 'r') as file:
    lines = file.readlines()

for line in lines:

    data = line.strip()
    try:
        temperature, gas_level = map(float, data.split(','))
        

        payload = {
            'api_key': api_key,
            'field1': temperature,
            'field2': gas_level
        }
        response = requests.post(thingspeak_url, params=payload)
        
        if response.status_code == 200:
            print(f'Data sent successfully: Temperature={temperature}, Gas Level={gas_level}')
        else:
            print(f'Failed to send data: {response.status_code}')
        
        
        #time.sleep(2)
    except ValueError:
        print("Invalid data format.")
