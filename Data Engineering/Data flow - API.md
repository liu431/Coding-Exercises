## Notes

### Tutoiral references
[Dataquest - Python API Tutorial: Getting Started with APIs](https://www.dataquest.io/blog/python-api-tutorial/)

[Real Python - Python & APIs: A Winning Combo for Reading Public Data](https://realpython.com/python-api/)


#### Public API to play with
[The Dog API - Dogs as a Service](https://www.thedogapi.com/)

[Public APIs](https://github.com/public-apis/public-apis)

### API basics
* API: a server that you can use to retrieve and send data to using code
* API enables you make a request to a remote web server, and retrieve the data you need
* Also called as `endpoints` when there are multiple


### API Types
* SOAP (Simple Object Access Protocol): typically associated with the enterprise world, has a stricter contract-based usage, and is mostly designed around actions.
* REST (Representational State Transfer): typically used for public APIs and is ideal for fetching data from the web. It’s much lighter and closer to the HTTP specification than SOAP.
* GraphQL: created by Facebook; a very flexible query language for APIs, where the clients decide exactly what they want to fetch from the server instead of the server deciding what to send.

### HTTP Methods
CRUD operations : create, read, update and delete resources

|HTTP Method|	Description|	Requests method|
|-|-|-|
|POST|	Create a new resource.	|requests.post()|
|GET|	Read an existing resource. |requests.get()|
|PUT|	Update an existing resource.	|requests.put()|
|DELETE|	Delete an existing resource.	|requests.delete()|

### [Requests and Response](https://docs.python-requests.org/en/latest/)
* Requests: relevant data regarding your API request call, such as the base URL, the endpoint, the method used, the headers, and so on.
* Responses: contain relevant data returned by the server, including the data or content, the status code, and the headers.

#### `GET` request: retrieve data

```python
import requests # need to install first
url = 'https://api.github.com/events'
x = requests.get(url, 'GET').json()
actotLoginName = [r['actor']['login'] for r in x]
```

##### [Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
* 200: Everything went okay, and the result has been returned (if any).
* 201: Your request was accepted and the resource was created.
* 301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
* 400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
* 401: The server thinks you’re not authenticated. Request requires some additional permissions 
* 403: The resource you’re trying to access is forbidden: you don’t have the right perlessons to see it.
* 404: The resource you tried to access wasn’t found on the server.
* 405: The endpoint does not allow for that specific HTTP method.
* 500: Your request wasn't expected and probably broke something on the server side.
* 503: The server is not ready to handle the request.

```python
response = requests.get("https://api.thedogapi.com/v1/breeds")
response.status_code # 200
response.text # returns the response contents in Unicode format
response.content # returns the response contents in bytes
request.url # 'https://api.thedogapi.com/v1/breeds'
request.path_url # '/v1/breeds'
request.method # 'GET'
response.reason # 'OK'
```

##### HTTP Headers
* `Accept`: What type of content the client can accept
* `Content-Type`: What type of content the server will respond with
* `User-Agent`: What software the client is using to communicate with the server
* `Server`: What software the server is using to communicate with the client
* `Authentication`: Who is calling the API and what credentials they have

```python
response.headers # with the response headers
response.request.headers # with the request headers

# Return specific attributes in the headers
response.headers.get('x-response-time')
response.headers.get('Content-Type')

# Save content as an image
response = requests.get("http://placegoat.com/200/200")
file = open("goat.jpeg", "wb")
file.write(response.content)
file.close()
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

##### Query Parameters
Fetch more specific data from an API to tailor the needs
```python
query_params = {"q": "labradoodle"}
endpoint = "https://api.thedogapi.com/v1/breeds/search"
requests.get(endpoint, params=query_params).json()
```

##### Pagination
 Split large amounts of data into multiple smaller pieces

* `page` attribute: defines which page you’re currently requesting
* `size` attribute: defines the size of each page

```python
# per_page=: number of items to return
# page=: allows you to paginate through multiple results
response = requests.get("https://api.github.com/events?per_page=1&page=0")
response.json()[0]['id']
```    

##### Rate Limiting
Restricts the number of requests that users can make in a given time frame.


### Example: Get COVID cases in Hampshire County, MA in last week
```python
from datetime import date, timedelta
today = date.today()
startday = today - timedelta(days=7)
country = "united-states"
endpoint = f"https://api.covid19api.com/country/{country}/status/confirmed"
params = {"from": str(startday), "to": str(today)}

response = requests.get(endpoint, params=params).json()
for r in response:
    if r['Province'] == 'Massachusetts' and r['City'] == 'Hampshire':
        print(f"Hampshire county case numbers on {r['Date'].split('T')[0]}: {r['Cases']}")
```

#### `POST` request: send data











