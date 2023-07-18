import os

if __name__ == "__main__":
    
    print("STARTING PROJECT SETUP PROCESS")
    print("==============================")

    # get the current directory name to use as the project name
    project_name = os.path.basename(os.getcwd())

    # verify that the project name is valid
    if not project_name.isidentifier():
        # remove any non-alphanumeric characters
        project_name = "".join([c for c in project_name if c.isalnum()])
        # add an underscore if the project name starts with a number
        if project_name[0].isnumeric():
            project_name = "_" + project_name
    
    # ask user to confirm project name
    while True:
        confirm = input("Project name will be {}. Proceed? (y/n) ".format(project_name))
        if confirm.lower() == "y":
            break
        elif confirm.lower() == "n":
            # ask user to enter a new project name
            while True:
                project_name = input("Please enter a new project name: ")
                if project_name.isidentifier():
                    break
                else:
                    print("Invalid project name. Please enter a valid project name.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
      
    # change rpytemplate to the project name
    print("Setting project name to {}...".format(project_name),end="")
    os.rename("rpytemplate", project_name)
    # change name in pyproject.toml
    with open("pyproject.toml", "r") as f:
        lines = f.readlines()
    with open("pyproject.toml", "w") as f:
        for line in lines:
            f.write(line.replace("rpytemplate", project_name))
    print("done.")

    # set directory.path as the place where the project is located
    print("Setting directory.path as the place where the project is located...",end="")
    with open("directory.path", "w") as f:
        f.write(os.getcwd())
    print("done.")

    rdp_client_web = "https://raw.githubusercontent.com/neurorishika/rdp-standard/main/rdp_client.py"

    # download latest rdp_client.py into package folder
    print("Downloading latest rdp_client.py into package folder...")
    os.system("curl {} -o {}/rdp_client.py".format(rdp_client_web, project_name))
    print("Download complete.")
    
    print("Project {} created! Please run 'poetry run python utils/build.py' to finish installation.".format(project_name))
    

