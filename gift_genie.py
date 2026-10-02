from openai import OpenAI

client = OpenAI()

print("==================================")
print("   🎁 Welcome to Gift Genie!     ")
print("==================================")
print("Let's find the perfect gift for that magical person")
print()

person = input("Tell me about the person you're shopping for. ")
budget = input("What's your approximate budget? ")
occassion = input("Is there a special occasion? ")

print("\n✨ Finding some gift ideas...\n")

response = client.responses.create(
    model="gpt-5.6-luna",
    input=f"""
    You are gift genie, a whimsical and creative gift suggestion assistant. 
    You are tasked with providing thoughtful gift ideas.

    The shopper is looking for a gift for:

    Person:{person}

    Budget:{budget}

    Occasion: {occassion}

    Suggest 3 thoughtful gifts.

    Guidelines: 
    - Make the ideas personal and specific. 
    - Consider the person's interests and hobbies. 
    - Respect the stated budget. 
    - Avoid generic suggestions when possible. 
    - Don't recommend things the person clearly already owns. 
    - Include a mix of practical, fun, and unexpected ideas. 
    - Explain why each gift fits this particular person. 
    - Give an approximate price range.

    Format the answer as: But do not write these words in the output:
        -Gift name
        -What the product is and why it fits the person
        -The price

    """
)

print("\n Gift Genie says:\n")
print(response.output_text)