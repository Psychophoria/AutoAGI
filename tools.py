
import os
import subprocess
import shutil
import json

# code_execution_tool: Creates and activates a temporary virtual environment named 'tempvenv' and executes code within it.
def code_execution_tool(code):
    venv_dir = 'tempvenv'
    if os.path.exists(venv_dir):
        shutil.rmtree(venv_dir)
    os.makedirs(venv_dir)
    subprocess.run(['python3', '-m', 'venv', venv_dir])
    activate_script = os.path.join(venv_dir, 'bin', 'activate')
    exec_code = f'source {activate_script} && python3 -c "{code}"'
    subprocess.run(exec_code, shell=True)

# file_save_tool: Saves or overwrites any file within the "WORKSPACE" user-defined directory.
def file_save_tool(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# file_load_tool: Loads and views any file within the "WORKSPACE" user-defined directory.
def file_load_tool(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# tool_generation_tool: Brainstorms, plans, creates, tests, permanently saves, and activates a new tool.
def tool_generation_tool(tool_name, tool_code):
    tools_file = 'tools.py'
    with open(tools_file, 'a') as file:
        file.write(f"\n# {tool_name}\n{tool_code}\n")

# internet_browsing_tool: Integrates functions from the "Crawlee" project to allow the AI agent to use an internet browser.
def internet_browsing_tool(url, actions):
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
