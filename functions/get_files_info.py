import os

def get_files_info(working_directory, directory=None): 
    full_path = os.path.join(working_directory, directory)
    