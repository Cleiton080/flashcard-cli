import click
from utils import retry_request, load_token


@click.group()
def card():
    pass


@card.command()
@click.option('--deck-id', help='Deck ID for the card')
@click.option('--front', help='Front side of the card')
@click.option('--back', help='Back side of the card')
def create(deck_id, front, back):
    payload = {'deck_id': deck_id, 'front': front, 'back': back}

    response = retry_request(
        '/card',
        payload,
        token=load_token(),
    )
    if response:
        click.echo('Card created successfully')
    else:
        click.echo('Failed to create card')

@card.command()
@click.option('--card-id', help='Card ID to describe')
def describe(card_id):
    response = retry_request(
        f'/card/{card_id}',
        method='GET',
        token=load_token(),
    )
    if response:
        click.echo(response)
    else:
        click.echo('Failed to describe card')

@card.command()
@click.option('--review', is_flag=True, help='Filter cards that require review')
def list(review):
    review_query = 'true' if review else 'false'

    response = retry_request(
        f'/card?review={review_query}',
        method='GET',
        token=load_token(),
    )
    if response:
        click.echo(response)
    else:
        click.echo('Failed to describe card')

@card.command()
@click.option('--card-id', help='Card ID to remove')
def remove(card_id):
    response = retry_request(
        f'/card/{card_id}',
        method='DELETE',
        token=load_token(),
    )
    if response:
        click.echo('Card removed successfully')
    else:
        click.echo('Failed to remove card')

@card.command()
@click.option('--card-id', help='Card ID to update')
@click.option('--front', help='New front side of the card')
@click.option('--back', help='New back side of the card')
def update(card_id, front, back):
    payload = {'front': front, 'back': back}

    response = retry_request(
        f'/card/{card_id}',
        payload,
        token=load_token(),
        method='PUT',
    )
    if response:
        click.echo('Card updated successfully')
    else:
        click.echo('Failed to update card')
