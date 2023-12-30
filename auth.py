import click
import getpass
from utils import retry_request, save_token, remove_token

@click.group()
def auth():
    pass

@click.option('--username', help='Username for authentication', required=True)
@click.option('--password-stdin', is_flag=True, help='Read password from stdin')
@auth.command()
def login(username, password_stdin):
    password_stdin = getpass.getpass()

    payload = {
        'username': username,
        'password': password_stdin
    }

    result = retry_request('/auth/login', payload)
    if result:
        access_token = result.get('token')
        save_token(access_token)
        click.echo('User successfully authenticated')
    else:
        click.echo('Authentication failed after multiple attempts')


@auth.command()
def register():
    username = click.prompt('Enter your username')
    password = getpass.getpass(prompt='Enter your password: ')
    confirm_password = getpass.getpass(prompt='Confirm your password: ')

    if password != confirm_password:
        click.echo('Passwords do not match')
        return

    payload = {
        'username': username,
        'password': password
    }

    result = retry_request('/auth/register', payload)
    if result:
        click.echo('Registration successful')
    else:
        click.echo('Registration failed after multiple attempts')


@auth.command()
def logout():
    remove_token()
    click.echo('User logged out successfully')