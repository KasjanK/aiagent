import os

def get_files_info(working_directory, directory=None): 
    # getting root directory no matter where we are
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)

    dir_path = os.path.join(working_directory, directory)
    full_path = os.path.join(project_root, dir_path)

    # absolute paths of target directories
    target_directory_abspath = os.path.abspath(full_path)
    working_directory_abspath = os.path.abspath(os.path.join(project_root, working_directory))

    # if target directory isn't in working directory
    if target_directory_abspath.startswith(working_directory_abspath) is False:
        return f"    Error: Cannot list '{directory}' as it is outside the permitted working directory"
    
    if not os.path.isdir(full_path):
        return f"    Error: '{directory}' is not a directory"
    
    full_string = []

    try:
        for file in os.listdir(full_path):
            full_string.append(f" - {file}: file_size={os.path.getsize(os.path.join(full_path, file))} bytes, is_dir={os.path.isdir(os.path.join(full_path, file))}")
    except Exception as e:
        return f"Error: {e}"

    return f"\n".join(full_string)