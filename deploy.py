import os
import subprocess

project_folder = "oops_i_did_it_again2"
dir_names = ["static", "template", "lib"]
base_path = f"./{project_folder}/src/my_app/"
mark_down_files = ["README.md", "CONTRIBUTORS.md", "TASK.md", ".gitignore"]
tool_list = ["nginx", "python3", "python3-pip", "nginx-extras", "curl"]

# ADD USER INPUT TO ASK FOR A PROJECt FOLDER NAME!


def main():
    create_filesystem()
#    install_tools()
    

#Creates the file system and placeholders
def create_filesystem():
    for name in dir_names:
        full_path = os.path.join(base_path, name)
        os.makedirs(full_path, exist_ok=True)
        placeholder_path = os.path.join(full_path, ".Placeholder")
        with open(placeholder_path, "w") as f:
            pass

    os.makedirs((f"./{project_folder}/automation"), exist_ok=True)
    with open(f"./{project_folder}/automation/.Placeholder", "w") as f:
        pass

    os.makedirs((f"./{project_folder}/config"), exist_ok=True)
    with open(f"./{project_folder}/config/.Placeholder", "w") as f:
        pass

    for mark_down_name in mark_down_files:
        with open(f"./{project_folder}/{mark_down_name}", "w") as f:
            pass

# Checks if tool installed
def is_installed(tool):
    try:
        subprocess.run([tool, "-version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

#Intalls tool if not installed
def install_tools():
    subprocess.run(['sudo', 'apt-get', 'update'])
    for tool_name in tool_list:
        if is_installed(tool_name):
            print(f"{tool_name} is already insalled..")
        else:
            print(f"{tool_name} is not installed. installing...")
            subprocess.run(["sudo", "apt-get", "install", "-y", tool_name], check=True)
    if not is_installed("poetry"):       
        subprocess.run(["curl", "-sSL", "https://install.python-poetry.org", "|", "python3", "-"], shell=True, check=True)
    else:
        return 0


if __name__ == "__main__":
    main()
