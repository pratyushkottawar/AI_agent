import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    abs_working_dir=os.path.abspath(working_directory)
    abs_directory=os.path.abspath(directory)
    if not os.path.commonpath([abs_directory,abs_working_dir])==abs_working_dir:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    else:
        if not os.path.isdir(abs_directory):
            print(f'Error: "{directory}" is not a directory')
        else:
            print(f'Success: "{directory}" is within the working directory')
    # contents = os.listdir(abs_directory)
    # for content in contents:
    #     is