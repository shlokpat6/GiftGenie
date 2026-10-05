from openai import OpenAI
from pydantic import BaseModel


# Data structures
class Gift(BaseModel):
    name: str
    reason: str
    price: str


class GiftList(BaseModel):
    gifts: list[Gift]


# OpenAI client
client = OpenAI()

# Gift Genie
def find_gifts(person, budget, occasion):

    response = client.responses.parse(
        model="gpt-5.6-luna",

        input=f"""
        You are Gift Genie, an expert gift recommendation assistant.

        The shopper is looking for a gift for:

        PERSON:
        {person}

        BUDGET:
        {budget}

        OCCASION:
        {occasion}

        Suggest exactly 5 thoughtful gift ideas.

        Make the ideas personal and specific.
        Consider the person's interests and hobbies.
        Respect the stated budget.
        Avoid generic suggestions when possible.
        Don't recommend things the person clearly already owns.

        For each gift:
        - Give it a name.
        - Explain why it fits the person.
        - Give an approximate price.
        """,

        text_format=GiftList
    )

    return response.output_parsed
