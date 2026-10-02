from openai import OpenAI
from pydantic import BaseModel
import streamlit as st

#Describes the structure of a gift suggestion
class Gift(BaseModel):
    name: str
    reason: str
    price: str

#Describes the structure of a list of gift suggestions
class GiftList(BaseModel):
    gifts: list[Gift]

# Create the OpenAI client
client = OpenAI()

st.title("🧞 Gift Genie")
st.write("Welcome to Gift Genie! Let's find the perfect gift for that magical person.")

# Get user input for gift suggestions
person = st.text_area("Tell me about the person you're shopping for.", placeholder="My brother who loves hiking and photography.")
budget = st.text_input("What's your approximate budget?", placeholder="$50-$100")
occassion = st.text_input("Is there a special occasion? ", placeholder="Birthday, Anniversary, none, etc.")

# Generate gift suggestions using the OpenAI API, but parsing the response into a structured GiftList object
if st.button("✨ Rub the lamp"):
    with st.spinner("✨ This wise genie is thinking hard..."):
        response = client.responses.parse(
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

            For each gift:
                -Give it a gift name
                -Explain why it would be a good fit for the person
                -Give an approximate price range
            """,

            text_format=GiftList
        )

        # Output the gift suggestions to the user
        st.subheader("Gift Genie Says")
        for gift in response.output_parsed.gifts:
            st.markdown(f"🎁 {gift.name}")
            st.write(f"{gift.reason}")
            st.write(f"{gift.price}")