import os
import subprocess


dir_names = ["static", "template", "lib"]
base_path = "./Project_folder/src/my_app/"
mark_down_files = ["README.md", "CONTRIBUTORS.md", "TASK.md", ".gitignore"]

def main():
    create_filesystem()
    install_tools()
    

#Creates the file system and placeholders
def create_filesystem():
    for name in dir_names:
        full_path = os.path.join(base_path, name)
        os.makedirs(full_path, exist_ok=True)
        placeholder_path = os.path.join(full_path, ".Placeholder")
        with open(placeholder_path, "w") as f:
            pass

    os.makedirs(("./Project_folder/automation"), exist_ok=True)
    with open("./Project_folder/automation/.Placeholder", "w") as f:
        pass

    os.makedirs(("./Project_folder/config"), exist_ok=True)
    with open("./Project_folder/config/.Placeholder", "w") as f:
        pass

    for mark_down_name in mark_down_files:
        with open(f"./Project_folder/{mark_down_name}", "w") as f:
            pass

# Checks if tool installed
def is_installed(tool):
    try:
        subprocess.run([tool, "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

#Intalls tool if not installed
def install_tools():
    tool_list = ["nginx", "nginx-extras", "poetry"]
    subprocess.run(['sudo', 'apt-get', 'update', 'y'])
    for tool_name in tool_list:
        if is_installed(tool_name):
            print(f"{tool_name} is already insalled..")
        else:
            print(f"{tool_name} is not installed. installing...")
            subprocess.run("sudo", "apt-get", "install", "-y", tool_name, check=True)


if __name__ == "__main__":
    main()