import requests
from termcolor import colored
from pyfiglet import figlet_format
from random import choice

title = colored(figlet_format("DAD JOKES"), "yellow")
print(title)

while True:
    term = input("Let me tell you a joke! Give me a topic: ")
    url = "https://icanhazdadjoke.com/search"
    headers = {"Accept": "application/json"}
    params = {"term": term}

    r = requests.get(url, headers=headers, params=params)

    # r = requests.get("https://icanhazdadjoke.com/search", headers={"Accept": "text/plain"}, params={"term": "cat"})

    results = r.json()["results"]
    if results:
        print(f"I've got {len(results)} joke(s) about {term}. Here's one:")
        print(colored((choice(results)["joke"]), "yellow"))
    else:
        print(
            f"Sorry, I don't have any results about {term}. Please try again.")
