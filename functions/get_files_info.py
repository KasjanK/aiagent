import os

def get_files_info(working_directory, directory=None):
    absolute_working_dir = os.path.abspath(working_directory)
    target_file_path = working_directory

    # make absolute path to directory if chosen
    if directory:
        target_file_path = os.path.abspath(os.path.join(working_directory, directory))

    # if target directory isn't in working directory
    if target_file_path.startswith(absolute_working_dir) is False:
        return f"    Error: Cannot list '{directory}' as it is outside the permitted working directory"
    
    if not os.path.isdir(target_file_path):
        return f"    Error: '{directory}' is not a directory"
    
    full_string = []

    try:
        for file in os.listdir(target_file_path):
            full_string.append(f" - {file}: file_size={os.path.getsize(os.path.join(target_file_path, file))} bytes, is_dir={os.path.isdir(os.path.join(target_file_path, file))}")
    except Exception as e:
        return f"Error: {e}"

    return f"\n".join(full_string)