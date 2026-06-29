import os
import sys
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from functions.get_file_info import get_files_info



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    
    

    parser = argparse.ArgumentParser(description="Your description here")
    parser.add_argument("user_prompt", type=str, help="Your help message here")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    
    messages: list[types.Content] = [
    types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

    # response=client.models.generate_content(model="gemini-2.5-flash", contents=messages)
    response = "Hello response."
    # if response is None or response.usage_metadata is None:
    #     print("response is malformed")
    #     return
    
    # print(response.text)
    get_files_info(".","./calculator/pkg")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        # print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        # print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

main()

