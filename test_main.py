import pytest
import main


@pytest.mark.parametrize(
    "login, email, password",
    [
        ("test_horob6", "test6@email.com", "password123")
    ],
)
def test_authorization_user_data(login, email, password):
    main.create_user(login, email, password)
    # Create session and get a token
    user_token = main.create_session(login, password)['User-Token']
    user_info = main.get_user_info(login, user_token)
    # Delete session
    main.delete_session()

    assert user_info['login'] == login
    assert user_info['account_details']['email'] == email


@pytest.mark.parametrize(
    "login, password, new_login, new_email",
    [
        ("test_horob4", "password123", "test_horob5", "test5@email.com"),
        ("test_horob5", "password123", "test_horob4", "test4@email.com")
    ],
)
def test_update_user_data(login, password, new_login, new_email):
    # Create session and get a token
    user_token = main.create_session(login, password)['User-Token']
    main.update_user_info(login, new_login, new_email, user_token)
    # Delete session
    main.delete_session()

    # Create session and get a token
    user_token = main.create_session(new_login, password)['User-Token']
    user_info = main.get_user_info(new_login, user_token)
    # Delete session
    main.delete_session()

    assert user_info['login'] == new_login
    assert new_email == user_info['account_details']['email']
