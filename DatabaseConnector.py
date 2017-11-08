import requests

class DBconnector:
    def start(query_string):
        try:
            connectURL = "put the url here"
            payload = {'query_string': query_string}

            request = requests.post(connectURL, data=payload)
            print(payload)
            return request.text
        except requests.RequestException as e:
            print(e)
