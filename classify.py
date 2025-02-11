from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-pro')

def classify_query(query):
    classifier_prompt = (
        "## Query Classification\n"
        "Please classify the following query as 'Indian Legal' or 'Non-Indian Legal':\n"
        "Query: '{}'\n"
        "Classification:"
    )

    # Compose prompt with the given query
    prompt = classifier_prompt.format(query)

    # Use Google Gen AI to generate a response based on the prompt
    response = model.generate_content(prompt)

    # Extract the generated classification from the response
    classification = response.text.strip()

    return classification

