import click
from utils import retry_request, load_token


@click.group()
def review():
    pass

@review.command()
@click.option('--delay-response', help='Delay for response')
@click.option('--card-id', help='Card ID for the review')
@click.option('--review-answer', help='Answer for the review')
def create(delay_response, card_id, review_answer):
    payload = {
        'delay_response': delay_response,
        'card_id': card_id,
        'review_answer': review_answer
    }

    response = retry_request(
        '/review',
        payload,
        token=load_token(),
    )

    if response:
        click.echo('Review created successfully')
    else:
        click.echo('Failed to create review')

@review.command()
def list():
    response = retry_request(
        '/review',
        method='GET',
        token=load_token(),
    )

    if response:
        click.echo(response)
    else:
        click.echo('Failed to retrieve reviews')

@review.command()
@click.option('--review-id', help='Review ID to describe')
def describe(review_id):
    response = retry_request(
        f'/review/{review_id}',
        method='GET',
        token=load_token(),
    )

    if response:
        click.echo(response)
    else:
        click.echo('Failed to describe review')
