import requests

url = "https://www.flickr.com/services/rest"

params = {
    "method":"flickr.photos.getPopular",
    "api_key":"43f96d80a69679c5488eb420eb7fd5aa",
    "user_id":"195799282@N04",
    "format":"json",
    "nojsoncallback":1
}

r=requests.get(url=url, params=params)
print(r.status_code)
json_response = r.json()
print(json_response)

if (r.status_code == 200 and json_response["stat"]=="ok"):
    print("API working")
else:
    print("Not working")
    print("Error found:",json_response["message"])