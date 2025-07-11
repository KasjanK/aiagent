import os

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