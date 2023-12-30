import time
import click
from utils import retry_request, load_token

@click.group()
def review():
    pass

@review.command()
@click.option('--card-id', help='Card ID for the review', required=True)
def create(card_id):
    def display_card(label, value):
        click.clear()
        click.echo("╔════════════════════╗")
        click.echo(f"║       {label}       ║")
        click.echo("╠════════════════════╣")
        click.echo(f"║ {value:<18} ║")
        click.echo("╠════════════════════╣")
        
    def get_review_option():
        options = ["EASY", "GOOD", "HARD", "AGAIN"]

        while True:
            chosen_option = click.prompt(
                '\n'.join(f"{i+1}. {option}" for i, option in enumerate(options)),
                type=int,
                default=1,
                show_default=False,
                prompt_suffix='\nEnter your choice: ',
                show_choices=False
            )

            if chosen_option in range(1, len(options) + 1):
                return options[chosen_option - 1]
            else:
                click.echo("Invalid option. Please enter a valid choice.")


    response = retry_request(
        f'/card/{card_id}',
        method='GET',
        token=load_token(),
    )
    if response:
        start_time = time.time()
        click.echo(display_card('PROMPT', response['front']))
        input("Press enter to see the answer...")
        end_time = time.time()
        response_time = end_time - start_time
        click.echo(display_card('ANSWER', response['back']))

        review_answer = get_review_option()

        payload = {
            'delay_response': f'{response_time} seconds',
            'card_id': card_id,
            'review_answer': review_answer
        }

        response = retry_request(
            '/review',
            payload,
            token=load_token(),
        )

        if response:
            click.echo(response)
        else:
            click.echo('Failed to create review')
    else:
        click.echo('Failed to describe card')

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
@click.option('--review-id', help='Review ID to describe', required=True)
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
