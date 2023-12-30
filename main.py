import click
from auth import auth
from card import card
from deck import deck
from review import review

@click.group()
def flashcard():
    pass

flashcard.add_command(auth)
flashcard.add_command(review)
flashcard.add_command(card)
flashcard.add_command(deck)

if __name__ == '__main__':
    flashcard()
