from typing import List
import requests
import resend

resend.api_key = "re_PSLZ9rLZ_71Ti2M3RFsy1YBJ3smiVjMNk"

# importing random quotes via API
URL: str = "https://api.quotable.io/random"


class Quote:
    content: str
    author: str

    def __init__(self, content, author) -> None:
        self.content = content
        self.author = author


quotes: List[Quote] = []

# Runs script 3 times
for api in range(3):
    response = requests.get(URL).json()
    quotes.append(Quote(content=response["content"], author=response["author"]))

# Editing the email content
email_template = "<strong>Here are your quotes: </strong>"
for quote in quotes:
    email_template += f"<p>{quote.content}</p> <p> — {quote.author}</p>"

params = {
    "from": "Acme <onboarding@resend.dev>",
    "to": ["techlifeinnovation10@gmail.com"],
    "subject": "Motivation Quote List Demo",
    "html": email_template,
}
resend.Emails.send(params)
