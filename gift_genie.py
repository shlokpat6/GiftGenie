import logging
import streamlit as st
from openai import OpenAI
from genie import find_gifts

logger = logging.getLogger(__name__)
client = OpenAI()

# Page
st.title("🎁 Gift Genie")

st.write(
    "Tell me about someone you're shopping for, "
    "and I'll suggest some gifts."
)

# User input
person = st.text_area(
    "Tell me about the person",
    placeholder=(
        "Example: My brother is 32, loves hiking, "
        "cooking, and photography..."
    )
)

budget = st.text_input(
    "What's your budget?",
    placeholder="$75"
)

occasion = st.text_input(
    "What's the occasion?",
    placeholder="Birthday"
)

# Generate gifts
if st.button("✨ Find Gift Ideas"):

    if not person:

        st.warning("Please tell me about the person first.")

    else:

        try:
            logger.info("Starting gift search")
            with st.spinner("Finding some great ideas..."):
                gifts = find_gifts(person, budget, occasion, client)
        except Exception:
            logger.exception("Gift search failed")
            st.error("Sorry, something went wrong. Please try again.")
        else:
            logger.info("Gift search completed successfully")
            st.subheader("✨ Gift Ideas")

            for gift in gifts.gifts:
                st.markdown(f"### 🎁 {gift.name}")
                st.write(f"**Why:** {gift.reason}")
                st.write(f"**Price:** {gift.price}")
                st.divider()