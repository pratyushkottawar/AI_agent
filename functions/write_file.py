import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
    if os.path.commonpath([abs_working_dir, target_path]) != abs_working_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isdir(target_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    try:
        parent_dir=os.path.dirname(target_path)
        os.makedirs(parent_dir, exist_ok=True)
        
    except exception as e:
        return f'Could not make the necessary directories for {target_path}.'
    
    with open(target_path, 'w') as f:
        f.write(content)
    
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'