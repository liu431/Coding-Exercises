### [Requests](https://docs.python-requests.org/en/latest/)

[Json response content](https://docs.python-requests.org/en/master/user/quickstart/#json-response-content)
```python
import requests
url = 'https://api.github.com/events'
x = requests.get(url, 'GET').json()
actotLoginName = [r['actor']['login'] for r in x]
```
