import os
from google.genai import types

def write_file(working_directory, file_path, content):
    absolute_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file_path.startswith(absolute_working_dir):
        return f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory"
    
    if not os.path.exists(target_file_path):
        try:
            os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating dir: {e}"
    try:
        with open(target_file_path, "w") as f:
                f.write(content)
        return f"Successfully wrote to '{file_path}' ({len(content)} characters written)"
    except Exception as e:
         return f"Error: writing to file {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a file with specified contet in the specified file path, constrained to the working directory. If the file path doesn't exists, it creates all needed directories.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the desired file, relative to the working directory."
            ), 
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that is supposed to be writtent to the file."
            )
        },
        required=["file_path", "content"],
    )
)