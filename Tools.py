import subprocess

def install_tool(tool_name):
    try:
        subprocess.check_output(['apt', 'install', tool_name, '-y'])
        print(f"{tool_name} installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {tool_name}: {e}")

def run_tool(tool_name):
    try:
        subprocess.check_output([tool_name])
    except FileNotFoundError:
        print(f"{tool_name} not found. Please make sure it is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {tool_name}: {e}")

def install_and_run_tools(tools):
    for tool in tools:
        install_tool(tool)
        run_tool(tool)

if __name__ == "__main__":
    # List of tools to install and run
    tools = [
        "setoolkit",
        "hydra",
        "aircrack-ng",
        "sqlmap",
        "john",
        "hashcat",
        "wireshark",
        "nmap",
        "owasp-zap",
        "msfconsole"
    ]

    # Install and run each tool
    install_and_run_tools(tools)
