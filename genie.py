from openai import OpenAI
from pydantic import BaseModel


# Data structures
class Gift(BaseModel):
    name: str
    reason: str
    price: str


class GiftList(BaseModel):
    gifts: list[Gift]

# Gift Genie
def find_gifts(person, budget, occasion, client):
    response = client.responses.parse(
        model="gpt-5.6-luna",
        tools=[
            {"type": "web_search"}
        ],
        input=f"""
        You are Gift Genie, an expert gift recommendation assistant.

        The shopper is looking for a gift for:

        PERSON:
        {person}

        BUDGET:
        {budget}

        OCCASION:
        {occasion}

        Search the web for current products that would make good gifts.

        Suggest exactly 5 thoughtful gift ideas.

        Make the ideas personal and specific.
        Consider the person's interests and hobbies.
        Respect the stated budget.
        Avoid generic suggestions when possible.

        For each gift:
        - Give the specific product name.
        - Explain why it fits the person.
        - Give the approximate current price.
        """,
        text_format=GiftList
    )

    return response.output_parsed
