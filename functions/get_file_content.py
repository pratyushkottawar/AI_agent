import os

MAX_CHARACTERS=10000

def get_file_content(working_directory: str, file_path: str) -> str:
    
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
    if os.path.commonpath([abs_working_dir, target_path]) != abs_working_dir:
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        return
    
    if not os.path.isfile(target_path):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        return
    
    with open(target_path, 'r') as f:
        file_content_string = f.read(MAX_CHARACTERS)
        # After reading the first MAX_CHARS...
        if f.read(1):
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARACTERS} characters]'
        return file_content_string
    
    