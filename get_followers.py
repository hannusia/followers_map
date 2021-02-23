import requests
import json


def create_url(nickname):
    usernames = "usernames=" + nickname
    user_fields = "user.fields=id"
    url = "https://api.twitter.com/2/users/by?{}&{}".format(
        usernames, user_fields)
    return url


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_user_id(nickname: str, bearer_token: str):
    try:
        url = create_url(nickname)
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        json_response = connect_to_endpoint(url, headers)
    except:
        print('enter a valid nickname')
    return int(json_response['data'][0]['id'])


def connect_to_endpoint_1(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_followers(user, bearer_token):
    user_id = get_user_id(user, bearer_token)
    url = "https://api.twitter.com/2/users/{}/followers".format(user_id)
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    params = {"user.fields": "location"}
    json_response = connect_to_endpoint_1(url, headers, params)
    with open('followers_loc.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_response, json_file, indent=4,
                  sort_keys=True, ensure_ascii=False)
