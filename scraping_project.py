import requests
from bs4 import BeautifulSoup
from random import shuffle
from sys import exit

def spam(guess, author, guesses_remaining, bio_url, requests_get, beautiful_soup):
    if guess == author:
        guesses_remaining = 0
        print("Correct! Good job.")
        return guesses_remaining
    guesses_remaining -= 1
    print(f"Wrong! You have {guesses_remaining} guesses remaining.\nHere is a clue:")
    if guesses_remaining == 3:
        response = requests.get(bio_url)
        soup = beautiful_soup(response.text, "html.parser")
        author_born_date = soup.select(".author-born-date")[0].text
        author_born_location = soup.select(".author-born-location")[0].text
        print(f"This person was born on {author_born_date} {author_born_location}.")
        return guesses_remaining
    elif guesses_remaining == 2:
        author_first_name = author.split()[0]
        print(f"This person's first name is {author_first_name}.")
        return guesses_remaining
    elif guesses_remaining == 1:
        author_last_name = author.split()[-1]
        print(f"This person's last name is {author_last_name}.")
        return guesses_remaining
    else:
        print("You lose.")
        return guesses_remaining

quotes = []
page = 1

while True:
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.select(".quote"):
        quotes += soup.select(".quote")
        page += 1
    else:
        break

quote_data = [{"text": quote.span.text, "author": quote.small.text, "bio_url": "http://quotes.toscrape.com" + quote.a["href"]} for quote in quotes]
shuffle(quote_data)

while True:
    for quote in quote_data:
        print("Who said this?")
        print(quote["text"])
        guesses_remaining = 4
        while guesses_remaining > 0:
            guess = input(": ")
            guesses_remaining = spam(guess, quote["author"], guesses_remaining, quote["bio_url"], requests.get, BeautifulSoup)
        print("Enter q to quit, or anything else to play again.")
        play_again = input(": ")
        if play_again == "q":
            exit()
