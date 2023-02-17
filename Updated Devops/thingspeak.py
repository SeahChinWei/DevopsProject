import requests

url = "https://api.thingspeak.com/update.json"
api_key = "WPWE7B2G1V5C4J5O"
data = {'field1': 25, 'field2': 50}

response = requests.post(url, params={'api_key': api_key}, json=data)

if response.status_code == 200:
    print("Data sent to ThingSpeak successfully.")
else:
    print("Error sending data to ThingSpeak.")

url2 = "https://api.thingspeak.com/apps/thingtweet/1/statuses/update"
api_key2 = "HL2SN9W4BK45PQ9K"
message = "Hello from ThingTweet!"

response2 = requests.post(url2, data={'api_key': api_key2, 'status': message})

if response2.status_code == 200:
    print("Tweet sent to ThingTweet successfully.")
else:
    print("Error sending tweet to ThingTweet.")
