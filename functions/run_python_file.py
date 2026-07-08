import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
    if os.path.commonpath([abs_working_dir, target_path]) != abs_working_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    
    try:
        final_args = ["python3",file_path]
        final_args.extend(args)
        output = subprocess.run(final_args, cwd=abs_working_dir, timeout=30, capture_output=True)
        final_string = f"""STDOUT: {output.stdout} STDERR: {output.stderr}"""
        
        if output.stdout == "" and output.stderr == "":
            final_string = "No output produced. \n"
        if output.returncode != 0:
            final_string += f'Process exited with returncode {output.returncode}'
        
        return final_string
    
    except Exception as e:
        return f'Error: executing Python file: {e}'
        