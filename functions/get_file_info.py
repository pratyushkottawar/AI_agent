import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        print(f'Result for {directory if directory!="." else "current"} directory:')
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
            print(f'\tError: Cannot list "{directory}" as it is outside the permitted working directory')
            return
        if not os.path.isdir(target_dir):
            print(f'\tError: "{directory}" is not a directory')
            return
        # return f'Success: "{directory}" is within the working directory'

        contents=os.listdir(target_dir)
        for content in contents:
            curr=os.path.join(target_dir,content)
            print(f"  - {content}: file_size={os.path.getsize(curr)} bytes, is_dir={os.path.isdir(curr)}")
        
        
    except Exception as e:
        return f"Error: {e}"