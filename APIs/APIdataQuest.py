import requests

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Print the content of the response (the data the server returned)
# print(response.content)

# This gets the same data as the command above
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
# print(response.content)

parameters = {"lat":37.78, "lon":-122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
content = response.content
# print(content)

# Get the response data as a Python object.  Verify that it's a dictionary.
json_data = response.json()
print(type(json_data))
print(json_data)

# Get the duration value of the ISS's first pass over San Francisco and assign the value to first_pass_duration.
first_pass_duration = json_data["response"][0]["duration"]
''''
response': [{'duration': 648, 'risetime': 1607052251}, {'duration': 569, 'risetime': 1607058081}
'''
# will print 648 as it is first element inside list, and we are getting key "duration"
print(first_pass_duration)

'''The server sends more than a status code and the data when it generates a response. 
It also sends metadata with information on how it generated the data and how to decode it. 
This information appears in the response headers. We can access it using the .headers property.
The headers will appear as a dictionary. For now, the content-type within the headers is 
the most important key. It tells us the format of the response, and how to decode it. 
For the OpenNotify API, the format is JSON, which is why we were able to decode it with JSON earlier.'''

# headers is a dict
print(response.headers)

# Get content-type from response.headers
# Assign the content type to the content_type variable.
content_type = response.headers["content-type"]