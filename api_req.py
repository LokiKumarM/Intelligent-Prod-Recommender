import requests

def search_res(user_query):
    url = "https://www.searchapi.io/api/v1/search"
    params = {
      "engine": "google_shopping",
       "gl": "in",
      "q": user_query,
      "api_key" :  "YOUR_API_KEY"
    }

    response = requests.get(url, params = params)
    results_json = response.json()
    return results_json['shopping_results']
