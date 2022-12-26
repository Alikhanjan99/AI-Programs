import requests

# Set the URL of the service and the phone number to track
service_url = 'https://example.com/api/track'
phone_number = '+1234567890'

# Make a request to the service to track the phone number
response = requests.get(service_url, params={'number': phone_number})

# Check the status code of the response to make sure the request was successful
if response.status_code == 200:
    # Parse the response to get the location information
    location = response.json()['location']
    print(f'The location of {phone_number} is {location}')
else:
    print('An error occurred while trying to track the phone number')
