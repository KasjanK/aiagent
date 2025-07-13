import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    absolute_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file_path.startswith(absolute_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    final_string = ""

    try:
        run_file = subprocess.run(
            [f"python3", f"{target_file_path}"], 
            timeout=30,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            encoding="utf-8"
            )
        if len(run_file.stdout) > 0:
            final_string += f"STDOUT: {run_file.stdout}\n"

        if len(run_file.stderr) > 0:
            final_string += f"STDERR: {run_file.stderr}\n"

        code = f"Process exited with code {run_file.returncode}"

        if run_file.returncode != 0:
            final_string += code

        if len(final_string) == 0:
            return f"No output produced"
    except Exception as e:
        return f"Error: executing Python file: {e}"
    return final_string

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file that's inside the specified working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the desired file, relative to the working directory."
            )
        },
        required=["file_path"]
    )
)