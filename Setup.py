import requests

def locate_phone(api_key, phone_number):
    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}'
    headers = {'content-type': 'application/json'}
    data = {'considerIp': 'false',
            'wifiAccessPoints': [],
            'cellTowers': [{'cellId': 42, 'locationAreaCode': 21, 'mobileCountryCode': 510, 'mobileNetworkCode': 11}]}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        location = response.json()['location']
        accuracy = response.json()['accuracy']
        print(f'Phone {phone_number} is at ({location["lat"]}, {location["lng"]}), accuracy: {accuracy} meters')
    else:
        print('Unable to locate phone')
