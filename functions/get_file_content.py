import os
from config import MAX_CHARS
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    absolute_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file_path.startswith(absolute_working_dir):
        return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory"
    
    if not os.path.isfile(target_file_path):
        return f"Error: File not found or is not a regular file: '{file_path}'"
    
    try:
        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            
        if len(file_content_string) >= MAX_CHARS:
            file_content_string += f"[...File '{file_path}' truncated at 10000 characters]"
    except Exception as e:
        return f"Error: {e}"
    
    return file_content_string

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads a file from the specified file path in the working directory and prints the content from it, up to {MAX_CHARS} characters .",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the desired file, relative to the working directory."
            )
        },
        required=["file_path"],
    )
)
