import click
from utils import retry_request, load_token


@click.group()
def deck():
    pass

@deck.command()
@click.option('--name', help='Deck name')
def create(name):
    payload = {'name': name}

    result = retry_request(
        '/deck',
        payload,
        token=load_token(),
    )
    if result:
        click.echo('Deck created successfully')
    else:
        click.echo('Failed to create deck after multiple attempts')


@deck.command()
@click.option('--deck-id', help='Deck ID')
def describe(deck_id):
    result = retry_request(
        f'/deck/{deck_id}',
        token=load_token(),
        method='GET',
    )
    if result:
        click.echo(result)
    else:
        click.echo('Failed to describe deck after multiple attempts')


@deck.command()
def list():
    result = retry_request(
        '/deck',
        token=load_token(),
        method='GET',
    )

    if result:
        click.echo(result)
    else:
        click.echo('Failed to fetch deck list after multiple attempts')


@deck.command()
@click.option('--deck-id', help='Deck ID')
def remove(deck_id):
    result = retry_request(
        f'/deck/{deck_id}',
        method='DELETE',
        token=load_token(),
    )
    if result:
        click.echo('Deck removed successfully')
    else:
        click.echo('Failed to remove deck after multiple attempts')

@deck.command()
@click.option('--deck-id', help='Deck ID')
@click.option('--name', help='Deck new name')
def update(deck_id, name):
    payload = {'name': name}
    
    result = retry_request(
        f'/deck/{deck_id}',
        payload,
        method='PUT',
        token=load_token(),
    )
    if result:
        click.echo('Deck updated successfully')
    else:
        click.echo('Failed to update deck after multiple attempts')
