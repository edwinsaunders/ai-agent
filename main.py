import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    verbose = False
        
    if len(sys.argv) > 2:
        prompt = sys.argv[1]
        if sys.argv[2] == "--verbose":
            verbose = True
    elif len(sys.argv) > 1:
        prompt = sys.argv[1]
    else:
        print("No prompt provided")
        sys.exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
    )
    
    if verbose == True:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print(response.text)


if __name__ == "__main__":
    main()
