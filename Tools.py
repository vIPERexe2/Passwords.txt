import subprocess

def install_tool(tool):
    try:
        subprocess.run(['pkg', 'install', tool], check=True)
        print(f"{tool} installed successfully!")
    except subprocess.CalledProcessError:
        print(f"Error installing {tool}. Please check your internet connection and try again.")

def install_all_tools():
    tools = ['tool1', 'tool2', 'tool3']  # Replace with the actual names of the tools you want to install
    
    for tool in tools:
        install_tool(tool)

def main():
    choice = input("Enter 'all' to install all tools or enter the name of a specific tool: ")
    
    if choice.lower() == 'all':
        install_all_tools()
    else:
        install_tool(choice)

if __name__ == "__main__":
    main()
