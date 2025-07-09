import os

def get_files_info(working_directory, directory=None):
    working_directory_abspath = os.path.abspath(working_directory)
    target_directory_abspath = working_directory

    # make absolute path to directory if chosen
    if directory:
        target_directory_abspath = os.path.abspath(os.path.join(working_directory, directory))

    # if target directory isn't in working directory
    if target_directory_abspath.startswith(working_directory_abspath) is False:
        return f"    Error: Cannot list '{directory}' as it is outside the permitted working directory"
    
    if not os.path.isdir(target_directory_abspath):
        return f"    Error: '{directory}' is not a directory"
    
    full_string = []

    try:
        for file in os.listdir(target_directory_abspath):
            full_string.append(f" - {file}: file_size={os.path.getsize(os.path.join(target_directory_abspath, file))} bytes, is_dir={os.path.isdir(os.path.join(target_directory_abspath, file))}")
    except Exception as e:
        return f"Error: {e}"

    return f"\n".join(full_string)