import requests
from logger import logger
import time
import pickle
import os
import sys

def make_request(uri, payload, method = 'POST', token=None):
    BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000/api/v1')
    url = f'{BASE_URL}/{uri}'
    headers = {}
    response = None

    if token:
        headers['Authorization'] = f'Bearer {token}'

    data = {
        'url': url,
        'json': payload,
        'headers': headers
    }

    try:
        if method == 'POST':
            response = requests.post(**data)
        elif method == 'GET':
            response = requests.get(**data)
        elif method == 'PUT':
            response = requests.put(**data)
        elif method == 'DELETE':
            response = requests.delete(**data)
        elif method == 'PATCH':
            response = requests.patch(**data)
        
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        if 500 <= e.response.status_code:
            logger().error(e)
            return None
        else:
            logger().error(e.response.json())
            sys.exit(1)

def retry_request(url, payload={}, token=None, method='POST'):
    retries = 0
    while retries < 3:
        result = make_request(url, payload, token=token, method=method)
        if result:
            return result
        retries += 1
        print(f"Retrying... Attempt {retries}")
        time.sleep(1)

    return None

def save_token(token):
    directory = os.path.expanduser('~/.fc')
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, 'token.pkl')

    with open(file_path, 'wb') as file:
        pickle.dump(token, file)

def load_token():
    directory = os.path.expanduser('~/.fc')
    file_path = os.path.join(directory, 'token.pkl')

    if not os.path.exists(file_path):
        logger().error('The token was not found. Please login using `fc auth login --username <username> --password-stdin`.')
        sys.exit(1)

    with open(file_path, 'rb') as file:
        token = pickle.load(file)
        return token

def remove_token():
    directory = os.path.expanduser('~/.fc')
    file_path = os.path.join(directory, 'token.pkl')

    if os.path.exists(file_path):
        os.remove(file_path)
