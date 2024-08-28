
# autoagi.py
# Main script to run the AutoAGI program

from ollama import OllamaModel  # Import the Ollama model
from tools import code_execution_tool, file_save_tool, file_load_tool, tool_generation_tool, internet_browsing_tool

def brainstorming_logic_system(prompt):
    """
    This function will brainstorm multiple methods to solve the user's prompt.
    It uses the Ollama model to generate methods.
    """
    # This function will brainstorm multiple methods to solve the user's prompt
    ollama_model = OllamaModel()  # Initialize the Ollama model
    methods = ollama_model.generate_methods(prompt)  # Generate methods using the Ollama model
    return methods

def planning_logic_system(methods):
    """
    This function will review all methods and determine the best plan.
    It uses the Ollama model to select the best plan.
    """
    # This function will review all methods and determine the best plan
    ollama_model = OllamaModel()  # Initialize the Ollama model
    best_plan = ollama_model.select_best_plan(methods)  # Select the best plan using the Ollama model
    return best_plan

def task_generation_logic_system(plan):
    """
    This function will break down the plan into detailed tasks.
    It uses the Ollama model to generate tasks.
    """
    # This function will break down the plan into detailed tasks
    ollama_model = OllamaModel()  # Initialize the Ollama model
    tasks = ollama_model.generate_tasks(plan)  # Generate tasks using the Ollama model
    return tasks

def task_execution_logic_system(tasks):
    """
    This function will execute the tasks.
    It uses the Ollama model and various tools to execute tasks.
    """
    # This function will execute the tasks
    ollama_model = OllamaModel()  # Initialize the Ollama model
    for task in tasks:
        ollama_model.execute_task(task)  # Execute task using the Ollama model
        if "code" in task.lower():
            code_execution_tool("print('Executing code')")
        elif "save" in task.lower():
            file_save_tool("workspace/example.txt", "Example content")
        elif "load" in task.lower():
            content = file_load_tool("workspace/example.txt")
            print(f"Loaded content: {content}")
        elif "generate tool" in task.lower():
            tool_generation_tool("example_tool", "def example_tool():\n    pass")
        elif "browse" in task.lower():
            internet_browsing_tool("https://example.com", ["wait_for_selector('h1')"])

def task_loop_logic_system(prompt):
    """
    This function will loop through tasks until the prompt is fully addressed.
    It uses the Ollama model to check if more tasks are needed.
    """
    # This function will loop through tasks until the prompt is fully addressed
    ollama_model = OllamaModel()  # Initialize the Ollama model
    methods = brainstorming_logic_system(prompt)
    best_plan = planning_logic_system(methods)
    tasks = task_generation_logic_system(best_plan)
    task_execution_logic_system(tasks)
    # Check if more tasks are needed
    more_tasks_needed = ollama_model.check_more_tasks_needed()  # Check if more tasks are needed using the Ollama model
    if more_tasks_needed:
        task_loop_logic_system(prompt)

def task_finalization_logic_system(prompt):
    """
    This function will finalize the tasks and generate a report.
    It uses the Ollama model to generate the final report.
    """
    # This function will finalize the tasks and generate a report
    ollama_model = OllamaModel()  # Initialize the Ollama model
    methods = brainstorming_logic_system(prompt)
    best_plan = planning_logic_system(methods)
    tasks = task_generation_logic_system(best_plan)
    task_execution_logic_system(tasks)
    # Generate final report
    final_report = ollama_model.generate_final_report(prompt, methods, best_plan, tasks)  # Generate final report using the Ollama model
    return final_report

def main():
    """
    Main function to run the AutoAGI program.
    It takes user input for the prompt and generates the final report.
    """
    prompt = input("Enter your prompt: ")
    final_report = task_finalization_logic_system(prompt)
    print(final_report)

if __name__ == "__main__":
    main()
