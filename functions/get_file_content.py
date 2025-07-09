import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)

    dir_path = os.path.join(working_directory, file_path)

    absolute_working_dir = os.path.abspath(os.path.join(project_root, working_directory))
    target_file_path = os.path.abspath(os.path.join(project_root, dir_path))

    if not target_file_path.startswith(absolute_working_dir):
        return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory"
    
    if not os.path.isfile(target_file_path):
        return f"Error: File not found or is not a regular file: '{file_path}'"
    
    try:
        with open(target_file_path, "r+") as f:
            file_content_string = f.read(MAX_CHARS)
            
        if len(file_content_string) >= MAX_CHARS:
            file_content_string += f"[...File '{file_path}' truncated at 10000 characters]"
    except Exception as e:
        return f"Error: {e}"
    
    return file_content_string
