import requests


def client():
    token_h = "Token de22c4c7d10b3eed9269e36a87eb275e977bf3d5"
    # credentials = {"username": "wembio", "password": "root"}

    # response = requests.post(
    #     "http://127.0.0.1:8000/api/rest-auth/login/", data=credentials
    # )
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)
    print("Status code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
