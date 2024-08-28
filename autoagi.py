
# autoagi.py
# Main script to run the AutoAGI program
# This script integrates the Ollama model with various logic systems and tools to create an autonomous AI agent.

from ollama import OllamaModel  # Import the Ollama model
from tools import code_execution_tool, file_save_tool, file_load_tool, tool_generation_tool, internet_browsing_tool

def brainstorming_logic_system(prompt):
    """
    This function will brainstorm multiple methods to solve the user's prompt.
    It uses the Ollama model to generate methods.
    """
    # Initialize the Ollama model
    ollama_model = OllamaModel()
    
    # Generate methods using the Ollama model
    methods = ollama_model.generate_methods(prompt)
    
    return methods

def planning_logic_system(methods):
    """
    This function will review all methods and determine the best plan.
    It uses the Ollama model to select the best plan.
    """
    # Initialize the Ollama model
    ollama_model = OllamaModel()
    
    # Select the best plan using the Ollama model
    best_plan = ollama_model.select_best_plan(methods)
    
    return best_plan

def task_generation_logic_system(plan):
    """
    This function will break down the plan into detailed tasks.
    It uses the Ollama model to generate tasks.
    """
    # Initialize the Ollama model
    ollama_model = OllamaModel()
    
    # Generate tasks using the Ollama model
    tasks = ollama_model.generate_tasks(plan)
    
    return tasks

def task_execution_logic_system(tasks):
    """
    This function will execute the tasks.
    It uses the Ollama model and various tools to execute tasks.
    """
    # Initialize the Ollama model
    ollama_model = OllamaModel()
    
    # Execute each task using the Ollama model and appropriate tools
    for task in tasks:
        ollama_model.execute_task(task)
        
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
    # Initialize the Ollama model
    ollama_model = OllamaModel()
    
    # Generate methods using the brainstorming logic system
    methods = brainstorming_logic_system(prompt)
    
    # Select the best plan using the planning logic system
    best_plan = planning_logic_system(methods)
    
    # Generate tasks using the task generation logic system
    tasks = task_generation_logic_system(best_plan)
    
    # Execute tasks using the task execution logic system
    task_execution_logic_system(tasks)
    
    # Check if more tasks are needed using the Ollama model
    more_tasks_needed = ollama_model.check_more_tasks_needed()
    
    if more_tasks_needed:
        task_loop_logic_system(prompt)

def task_finalization_logic_system(prompt):
    """
    This function will finalize the tasks and generate a report.
    It uses the Ollama model to generate the final report.
    """
    # Initialize the Ollama model
    ollama_model = OllamaModel()
    
    # Generate methods using the brainstorming logic system
    methods = brainstorming_logic_system(prompt)
    
    # Select the best plan using the planning logic system
    best_plan = planning_logic_system(methods)
    
    # Generate tasks using the task generation logic system
    tasks = task_generation_logic_system(best_plan)
    
    # Execute tasks using the task execution logic system
    task_execution_logic_system(tasks)
    
    # Generate final report using the Ollama model
    final_report = ollama_model.generate_final_report(prompt, methods, best_plan, tasks)
    
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
