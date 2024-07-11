import requests


urls = ['http://example.com', 'http://testsite.com']


methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']

def test_http_methods(url):
    print(f"Testing HTTP methods for {url}")
    responses = {}
    for method in methods:
        try:
            
            if method == 'GET':
                response = requests.get(url)
            elif method == 'POST':
                response = requests.post(url, data={'data': 'value'})
            elif method == 'PUT':
                response = requests.put(url, data={'data': 'value'})
            elif method == 'DELETE':
                response = requests.delete(url)
            elif method == 'OPTIONS':
                response = requests.options(url)
            
            
            responses[method] = response.status_code
        except requests.RequestException as e:
            responses[method] = f"Error: {str(e)}"

    
    print(f"Responses for {url}:")
    for method, status in responses.items():
        print(f"  {method}: {status}")


for url in urls:
    test_http_methods(url)
