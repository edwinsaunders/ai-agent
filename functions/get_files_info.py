import os

def get_files_info(working_directory, directory="."):
    # check if working_dir + dir exists
        # get abs path of joined path
    # check if 

    # set home path: /home/edwin2/Documents/bootdev/ai-agent
    # check final abs path starts with that
    # make sure neither working dir or dir starts with / or contains ..
    guard_path = '/home/edwin2/Documents/bootdev/ai-agent'
    joined_path = os.path.join(working_directory, directory)

    abs_path = os.path.abspath(joined_path)

    # safe_path = False

    conditions_met = False

    if not('..' in working_directory or '..' in directory or working_directory.startswith('/') or directory.startswith('/')):
        conditions_met = True

    if not abs_path.startswith(guard_path) or not conditions_met:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'

    dir_list = os.listdir(abs_path)
    string_list = []
    for item in dir_list:
        temp_path = os.path.join(abs_path, item)
        string_list.append(f'- {item}: file_size={os.path.getsize(temp_path)} bytes, is_dir={os.path.isdir(temp_path)}')

    return '\n'.join(string_list)
