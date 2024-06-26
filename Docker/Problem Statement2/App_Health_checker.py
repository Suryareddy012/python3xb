import requests

application_url = "http://example.com"

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return 'up'
        else:
            return 'down'
    except requests.exceptions.RequestException as e:
        return 'down'


status = check_application_status(application_url)

# Print the application status
print(f"The application at {application_url} is {status}")