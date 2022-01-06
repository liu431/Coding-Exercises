## Notes

### Tutoiral references
[Dataquest - Python API Tutorial: Getting Started with APIs](https://www.dataquest.io/blog/python-api-tutorial/)

[Real Python - Python & APIs: A Winning Combo for Reading Public Data](https://realpython.com/python-api/)
### API basics
* API: a server that you can use to retrieve and send data to using code
* API enables you make a request to a remote web server, and retrieve the data you need
* Also called as `endpoints` when there are multiple 

### Public API to play with
[The Dog API - Dogs as a Service](https://www.thedogapi.com/)

[Public APIs](https://github.com/public-apis/public-apis)

### [Requests](https://docs.python-requests.org/en/latest/)
##### `GET` request: retrieve data

```python
import requests
url = 'https://api.github.com/events'
x = requests.get(url, 'GET').json()
actotLoginName = [r['actor']['login'] for r in x]
```

##### [Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
* 200: Everything went okay, and the result has been returned (if any).
* 301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
* 400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
* 401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
* 403: The resource you’re trying to access is forbidden: you don’t have the right perlessons to see it.
* 404: The resource you tried to access wasn’t found on the server.
* 503: The server is not ready to handle the request.

```python
response = requests.get("https://api.thedogapi.com/v1/breeds")
print(response.status_code) # 200
```

##### JSON (JavaScript Object Notation)
* A way to encode data structures that ensures that they are easily readable by machines
* [JSON response content](https://docs.python-requests.org/en/master/user/quickstart/#json-response-content)
* Functions
  - json.dumps() — Takes in a Python object, and converts (dumps) it to a string. (use it to print a formatted string)
  - json.loads() — Takes a JSON string, and converts (loads) it to a Python object.

```python
jsondata = response.json()

# Print the data as a diagram
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(jsondata)
```

##### Parameters


