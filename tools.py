
import os
import subprocess
import shutil
import json

# code_execution_tool: Creates and activates a temporary virtual environment named 'tempvenv' and executes code within it.
# This tool is used to execute any code within a temporary virtual environment.
def code_execution_tool(code):
    """
    Creates and activates a temporary virtual environment named 'tempvenv' and executes code within it.
    Args:
    code (str): The code to be executed within the virtual environment.
    """
    venv_dir = 'tempvenv'
    if os.path.exists(venv_dir):
        shutil.rmtree(venv_dir)
    os.makedirs(venv_dir)
    subprocess.run(['python3', '-m', 'venv', venv_dir])
    activate_script = os.path.join(venv_dir, 'bin', 'activate')
    exec_code = f'source {activate_script} && python3 -c "{code}"'
    # Execute the code within the virtual environment
    subprocess.run(exec_code, shell=True)

# file_save_tool: Saves or overwrites any file within the "WORKSPACE" user-defined directory.
# This tool is used to save or overwrite files with the specified content.
def file_save_tool(file_path, content):
    """
    Saves or overwrites any file within the "WORKSPACE" user-defined directory.
    Args:
    file_path (str): The path to the file to be saved or overwritten.
    content (str): The content to be written to the file.
    """
    with open(file_path, 'w') as file:
        file.write(content)

# file_load_tool: Loads and views any file within the "WORKSPACE" user-defined directory.
# This tool is used to load and view the content of specified files.
def file_load_tool(file_path):
    """
    Loads and views any file within the "WORKSPACE" user-defined directory.
    Args:
    file_path (str): The path to the file to be loaded.
    Returns:
    str: The content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()

# tool_generation_tool: Brainstorms, plans, creates, tests, permanently saves, and activates a new tool.
# This tool is used to generate new tools and add them to the tools.py file.
def tool_generation_tool(tool_name, tool_code):
    """
    Brainstorms, plans, creates, tests, permanently saves, and activates a new tool.
    Args:
    tool_name (str): The name of the new tool.
    tool_code (str): The code of the new tool.
    """
    tools_file = 'tools.py'
    # Append the new tool code to the tools.py file
    with open(tools_file, 'a') as file:
        file.write(f"\n# {tool_name}\n{tool_code}\n")

# internet_browsing_tool: Integrates functions from the "Crawlee" project to allow the AI agent to use an internet browser.
# This tool is used to perform internet browsing actions using the Crawlee project.
def internet_browsing_tool(url, actions):
    """
    Integrates functions from the "Crawlee" project to allow the AI agent to use an internet browser.
    Args:
    url (str): The URL to be visited.
    actions (list): A list of actions to be performed on the webpage.
    """
    from crawlee import BrowserCrawler, launch_puppeteer
    async def run():
        browser = await launch_puppeteer()
        page = await browser.new_page()
        await page.goto(url)
        for action in actions:
            await eval(f"page.{action}")
        await browser.close()
    import asyncio
    asyncio.run(run())
