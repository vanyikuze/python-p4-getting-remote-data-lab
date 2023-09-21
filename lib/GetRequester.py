import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):

        response = requests.get(self.url)
        return response.content
    

    def load_json(self):
        response_body = self.get_response_body()
        try:
            json_data = json.loads(response_body)
            return json_data
        except json.JSONDecodeError as e :
            print(f"Failed to parse JSON: {e}")
            return None
        
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
requester = GetRequester(url)

json_data = requester.load_json()

if json_data:
    print(json_data)