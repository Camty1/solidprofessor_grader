import requests

LOGIN_URL = 'https://www.solidprofessor.com/account/login'

LOGIN_INFO_FILENAME = '.login'

def get_login_info_dict(filename):
    with open(filename, 'r') as file:
        username = file.readline()
        password = file.readline()

    return {
        'username': username,
        'password': password
    }
    

get_login_info_dict(LOGIN_INFO_FILENAME)


