import pprint
import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print("\n------- status/headers/encoding ---------")
print(r.status_code)    # 200
print(r.headers['content-type'])    # application/json; charset=utf-8
print(r.encoding)   # utf-8

print("\n----------------- text ------------------")
print(r.text)

print("\n----------------- json ------------------")
print(pprint.pprint(r.json()))

print("\n---------------- headers ----------------")
for key, value in r.headers.items():
    print(key, ' => ', value)

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

# Run mitmproxy to use
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://localhost:8080",
}

data = {
    "title": "this_is_my_title",
    "body": "this is body text for this test request",
    "userId": 1,
}

headers = {
    "Content-type": "application/json; charset=UTF-8"
}

# json, data
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    headers=headers,
    json=data,
    verify=False
)

print(response.text)

