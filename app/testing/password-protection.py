import requests


def test_api_endpoint(method, url):
    if method == "get":
        answer = requests.get(url)
    if method == "put":
        answer = requests.put(url)
    if method == "post":
        answer = requests.post(url)
    if method == "delete":
        answer = requests.delete(url)

    evaluation = "[WARNING]"
    if answer.status_code == 401:
        evaluation = "[OK]"
    print(evaluation, method, url, answer.status_code)
    return evaluation


server = "http://localhost:4000/"
api_url_prefix = "api/1.0/"
endpoints = [
    # administration
    {
        "method": "post",
        "url": server + api_url_prefix + "users"
    },
    {
        "method": "put",
        "url": server + api_url_prefix + "users"
    },
    {
        "method": "delete",
        "url": server + api_url_prefix + "users/test"
    },
    {
        "method": "get",
        "url": server + api_url_prefix + "users"
    },
    {
        "method": "get",
        "url": server + api_url_prefix + "users/test"
    },
    # collections
    {
        "method": "get",
        "url": server + api_url_prefix + "collections"
    },
    {
        "method": "get",
        "url": server + api_url_prefix + "collections/test"
    },
    {
        "method": "post",
        "url": server + api_url_prefix + "collections"
    },
    {
        "method": "put",
        "url": server + api_url_prefix + "collections/test"
    },
    {
        "method": "delete",
        "url": server + api_url_prefix + "collections/test"
    },
    # items
    {
        "method": "get",
        "url": server + api_url_prefix + "items/test"
    },
    {
        "method": "post",
        "url": server + api_url_prefix + "items/test"
    },
    {
        "method": "put",
        "url": server + api_url_prefix + "items/test"
    },
    {
        "method": "delete",
        "url": server + api_url_prefix + "items/test/test"
    },
    {
        "method": "get",
        "url": server + api_url_prefix + "test/test/annotations.json"
    },
    # images
    {
        "method": "get",
        "url": server + api_url_prefix + "images/test"
    },
    {
        "method": "post",
        "url": server + api_url_prefix + "images"
    },
    {
        "method": "post",
        "url": server + api_url_prefix + "images/test/test"
    },
    {
        "method": "post",
        "url": server + api_url_prefix + "images/test/annotations"
    }
]

evaluations = []
for endpoint in endpoints:
    evaluation = test_api_endpoint(endpoint["method"], endpoint["url"])
    evaluations.append(evaluation)

if "[WARNING]" in evaluations:
    print("Warning! Check the test results.")
else:
    print("All tests OK")
