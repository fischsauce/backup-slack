
## A little python script to make a dictionary of channels and their unique ID.

# import package to deal with the JSON file we got from the Slack API:
# see: https://www.w3schools.com/python/python_json.asp
import json

# Create a dicitonary:
channels = {}

# open the file with the 'r' (Read only) flag:
with open('channel_list.json', 'r') as json_file:

# Deserialize the JSON data into a new python object:
    channel_list = json.load(json_file)

# Iterate through the new list object and add to the dicitonary:
    for channel in channel_list:
        channels[channel['name']]=channel['id']

# Print the dicitonary:
print(channels)
