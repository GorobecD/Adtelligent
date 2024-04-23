import requests
from typing import Dict, Union


API_KEY = "312cf4f2edba1b4daf9fa19686b2db7a"


# Function to create user account
def create_user(login: str, email: str, password: str) -> Dict[str, str]:
    response = requests.post(
        "https://favqs.com/api/users",
        json={"user": {"login": login, "email": email, "password": password}},
        headers={"Authorization": f"Token token={API_KEY}"}
    )
    response.raise_for_status()
    return response.json()


# Function to get user information
def get_user_info(login: str, user_token: str) -> Dict[str, Union[str, Dict[str, str]]]:
    response = requests.get(
        f"https://favqs.com/api/users/{login}",
        headers={"Authorization": f"Token token={API_KEY}",
                 "User-Token": f"{user_token}"}
    )
    response.raise_for_status()
    return response.json()


# Function to update user information
def update_user_info(login: str, new_login: str, new_email: str, user_token: str) -> Dict[str, str]:
    response = requests.put(
        f"https://favqs.com/api/users/{login}",
        json={"user": {"login": new_login, "email": new_email}},
        headers={"Authorization": f"Token token={API_KEY}",
                 "User-Token": f"{user_token}"}
    )
    response.raise_for_status()
    return response.json()


# Function to create a user session
def create_session(login: str, password: str) -> Dict[str, str]:
    response = requests.post(
        "https://favqs.com/api/session",
        json={"user": {"login": login, "password": password}},
        headers={"Authorization": f"Token token={API_KEY}"}
    )

    response.raise_for_status()
    return response.json()


# Function to delete a user session
def delete_session():
    requests.delete(
        "https://favqs.com/api/session",
        headers={"Authorization": f"Token token={API_KEY}"}
    )
