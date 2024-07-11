import requests


urls = ['http://example.com', 'http://testsite.com']


security_headers = [
    'Strict-Transport-Security', 'X-Frame-Options', 'X-Content-Type-Options',
    'Content-Security-Policy', 'X-XSS-Protection', 'Referrer-Policy'
]

def check_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        print(f"Checking {url}")
        for header in security_headers:
            if header in headers:
                print(f"  {header}: {headers[header]}")
            else:
                print(f"  {header}: NOT FOUND")
    except requests.RequestException as e:
        print(f"Failed to retrieve {url}: {str(e)}")


for url in urls:
    check_security_headers(url)
