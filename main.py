import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import schema_run_python_file, schema_get_file_content, schema_get_files_info, schema_write_file
from functions.call_function import call_function

def main():
    if len(sys.argv) < 2:
        print("No arguments provided")
        exit(1)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
        ]
    )
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    verbose = "--verbose" in sys.argv

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    if not response.function_calls:
        return response.text
    
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose=verbose)

        if not function_call_result.parts[0].function_response.response:
            sys.exit("fatal error")
        
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
            
if __name__ == "__main__":
    main()
