# Gift Genie – AI-Powered Gift Recommendation App

A small AI-powered gift recommendation app built with Python, OpenAI, and Streamlit. Tell Gift Genie who you're shopping for, what they enjoy, your budget, and the occasion. It searches the web for current product ideas and returns five personalized gift recommendations, including the product name, why it suits the recipient, and an approximate price.

This project was built as a hands-on way to learn how to develop an AI-powered Python application, work with structured LLM outputs, organize application code, handle errors, write automated tests, and set up continuous integration with GitHub Actions.

## What you need

- Python 3.10 or newer
- An OpenAI API key ([https://platform.openai.com/api-keys](https://platform.openai.com/api-keys))
- An internet connection (gift recommendations and web searches use the OpenAI API)
- Git (optional, if you want to clone the repository)

**Privacy note:** Information entered about the gift recipient is sent to OpenAI as part of the recommendation request. Do not enter sensitive personal information. Keep your API key private and never commit it to GitHub.

## Setup (Windows)

1. Install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/). During installation, check **Add Python to PATH**.
2. Download or clone this repository into a folder you can find, such as `Desktop\GiftGenie`.
3. Open that folder in File Explorer.
4. Click the address bar, type `cmd`, and press Enter.
5. Create and activate a virtual environment, then install the dependencies:

```bash
py -m venv .venv
.venv\Scripts\activate
py -m pip install --upgrade pip
pip install -r requirements.txt
```

6. Create a .env file and add set the OpenAI api key

```
OPENAI_API_KEY=sk-your-key-here
```

7. Start the app:

```bash
streamlit run gift_genie.py
```

## Setup (Mac)

1. Install Python 3.10 or newer from [https://www.python.org/downloads/](https://www.python.org/downloads/) if you don't already have it.
2. Download or clone this repository.
3. Open Terminal and move into the project folder. For example:

```bash
cd ~/Desktop/GiftGenie
```

4. Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

5. Create a .env file and add set the OpenAI api key

```
OPENAI_API_KEY=sk-your-key-here
```

6. Start the app:

```bash
streamlit run gift_genie.py
```

## Use it

- Streamlit opens the app in your browser, usually at `http://localhost:8501`.
- Enter a description of the person you're shopping for, including their interests, hobbies, and any other useful details.
- Enter your budget.
- Enter the occasion, such as a birthday, anniversary, or holiday.
- Click **Find Gift Ideas**.
- Gift Genie searches for current product ideas and generates five personalized recommendations.
- Review each recommendation, including its name, explanation, and approximate price.

## How it works

1. **User input:** The Streamlit interface collects information about the recipient, budget, and occasion.
2. **Application logic:** The UI passes the information and an OpenAI client to the `find_gifts()` function in `genie.py`.
3. **Web search:** The OpenAI API uses its web search tool to find current product information.
4. **Structured output:** The model generates gift recommendations using a predefined Pydantic schema.
5. **Validation and parsing:** OpenAI's structured-output parsing converts the response into Pydantic objects matching the `GiftList` and `Gift` models.
6. **Display:** The application displays the parsed recommendations in the Streamlit interface.
7. **Error handling and logging:** Errors are logged, and users receive a friendly error message rather than an unhandled application crash.

## Project structure

```text
GiftGenie/
│
├── gift_genie.py          # Streamlit user interface
├── genie.py               # AI recommendation logic and Pydantic models
├── test_genie.py          # Automated tests
├── requirements.txt       # Python dependencies
├── .env.txt               # Holds the Open AI API Key
│
└── .github/
    └── workflows/
        └── tests.yml      # GitHub Actions CI workflow
```

The application separates the user interface from the AI/business logic. This makes the code easier to maintain and allows the recommendation function to be tested independently of the Streamlit interface.

## Tech stack

- **Python** – Main programming language
- **OpenAI API** – AI-powered gift recommendations and web search
- **Pydantic** – Defines and validates the structure of AI-generated recommendations
- **Streamlit** – Interactive web interface
- **Pytest** – Automated tests for application logic
- **unittest.mock** – Mock objects for testing without making real API calls
- **Logging** – Records application events and errors
- **Git and GitHub** – Source control and project hosting
- **GitHub Actions** – Automatically runs tests when code is pushed to GitHub

## Testing

The project includes automated tests written with Pytest.

The tests cover:

- Creating valid `Gift` objects.
- Checking that required fields are present.
- Testing the `find_gifts()` function.
- Verifying that the recommendation function returns the expected structured data.

The OpenAI client is injected into the recommendation function, allowing tests to use mock objects instead of making real API requests. This keeps tests fast, predictable, and free of API usage costs.

Run the tests locally with:

```bash
pytest
```

## Continuous Integration (GitHub Actions)

The project includes a GitHub Actions workflow that automatically runs the test suite whenever code is pushed to the repository.

The workflow:

1. Starts an Ubuntu environment.
2. Checks out the repository.
3. Sets up Python.
4. Installs the dependencies from `requirements.txt`.
5. Runs the Pytest test suite.

A successful workflow run confirms that the automated tests pass in the GitHub environment.

## Notes

- The OpenAI API key is read from the `OPENAI_API_KEY` environment variable. It is not hardcoded in the application.
- The virtual environment folder (`.venv`) and the `.env` file should not be committed to GitHub.
- The application currently runs locally using Streamlit.
- Gift recommendations and prices are generated using AI and web search. Product availability and prices can change, so verify details with the retailer before purchasing.
- Pydantic validates the structure and types of the returned data. It does not guarantee that product details, prices, or recommendations are factually correct.
- The application currently uses a mock OpenAI client in its automated tests, so running tests does not require an API key.
- GitHub Actions provides continuous integration (CI) by automatically running tests. It does not currently deploy the application.