import os
import openai
from dotenv import load_dotenv
from api_call.api_call import get_user

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def should_call_api(user_prompt):
    """
    Use GPT-3 to determine if the user prompt indicates a need to call the API.
    """
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Answer 'yes' or 'no': Does the following user prompt indicate a need to access user data from an API? Prompt: '{user_prompt}'\n\n API: get_user_data",
            max_tokens=10
        )
        return "yes" in response.choices[0].text.strip().lower()
    except Exception as e:
        print(f"Error in should_call_api: {e}")
        return False

def get_response_from_gpt3(user_input, api_res):
    """
    Function to call the GPT-3 API and get a response.
    """
    if len(api_res) > 0:
        prompt = f"You need to complete the task based on the user data provided:\nTask Description: {user_input}\nUser Data: {api_res}\n"
    else:
        prompt = f"You need to complete the task based on the user data provided:\nTask Description: {user_input}\n"
    
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=200
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error in get_response_from_gpt3: {e}"

def main():
    user_input = input("Enter your prompt: ")

    api_res = ""
    if should_call_api(user_input):
        api_res = get_user()
    else:
        print("No need to call the user data API for this input.")

    gpt3_response = get_response_from_gpt3(user_input, api_res)
    print("GPT-3 Response:", gpt3_response)

if __name__ == "__main__":
    main()

