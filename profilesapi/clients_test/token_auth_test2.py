import requests


def client():

    # data = {
    #     "username": "wembio2",
    #     "email": "test@test.com",
    #     "password1": "rootuser123",
    #     "password2": "rootuser123",
    # }

    # response = requests.post(
    #     "http://127.0.0.1:8000/api/rest-auth/registration/", data=data
    # )

    token_h = "Token b03fd519259b9c604637d92c5c6987c551624e58"
    credentials = {"username": "wembio", "password": "root"}

    response = requests.post(
        "http://127.0.0.1:8000/api/rest-auth/login/", data=credentials
    )
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
