import openai
import subprocess
import os
import re
import ast
import openai

# Set up your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def capture_terminal_output(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return f"Error capturing terminal output: {str(e)}"

def analyze_and_fix_django_project(project_path):
    # Placeholder for Django project analysis and fixing
    files = get_all_files(project_path)

    for file_path in files:
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Actual code analysis logic
        detected_issues = analyze_code(file_content)

        if detected_issues:
            print(f"Detected Issues in {file_path}:")

            for issue in detected_issues:
                print(f" - {issue}")

                # Suggest fixes using OpenAI GPT-3
                suggested_fix = suggest_fix(issue)
                print(f"   Suggested Fix: {suggested_fix}")

    # Execute necessary commands based on detected issues
    execute_necessary_commands(project_path, detected_issues)


def analyze_code(code):
    tree = ast.parse(code)

    # Placeholder for detected issues
    detected_issues = []

    # Check for unused imports
    for node in ast.walk(tree):
        if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if alias.asname is not None:
                    # Report an import with an alias (asname) as unused
                    detected_issues.append(f"Unused import: {alias.asname}")
                else:
                    # Report an import without an alias as unused
                    detected_issues.append(f"Unused import: {alias.name}")

    # Check for unused variables
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Ignore variables in function definitions for simplicity
            continue

        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variable_name = target.id
                    if not is_variable_used(variable_name, tree):
                        detected_issues.append(f"Unused variable: {variable_name}")
        # Check for undefined variables
    undefined_variables = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            variable_name = node.id
            if not is_variable_defined(variable_name, tree):
                undefined_variables.add(variable_name)

    for variable_name in undefined_variables:
        detected_issues.append(f"Undefined variable: {variable_name}")

    return detected_issues



def is_variable_used(variable_name, tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id == variable_name:
            # Variable is used
            return True
    return False



def is_variable_defined(variable_name, tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Ignore variables defined in function definitions for simplicity
            continue

        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == variable_name:
                    # Variable is defined
                    return True
    return False




def get_all_files(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                all_files.append(os.path.join(root, file))
    return all_files


def detect_errors(detected_error):
    # Placeholder for error detection logic
    explanation_prompt = f"Explain the error: '{detected_error}'"
    error_explanation = get_gpt3_response(explanation_prompt)
    return error_explanation

def execute_necessary_commands():
    # Placeholder for executing necessary commands
    print("Executing necessary commands to resolve issues.")


def suggest_fix(issue):
    # Use OpenAI GPT-3 to suggest a fix for the detected issue
    prompt = f"Suggest a fix for the issue: '{issue}'"
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        
        suggested_fix = response.choices[0].text.strip()
        return suggested_fix
    except Exception as e:
        # Handle API request errors
        print(f"Error communicating with OpenAI API: {str(e)}")
        return f"Unable to suggest a fix for the issue: '{issue}'"
    


def get_gpt3_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()


def execute_necessary_commands(file_path, detected_issues):
    # Placeholder for executing necessary commands to automatically fix issues
    for issue in detected_issues:
        if "Django specific issue" in issue:
            # Placeholder for executing Django management commands
            django_command = "python manage.py your_django_command"
            result = run_command(django_command)

            if result.success:
                print(f"Successfully executed Django command: {django_command}")
            else:
                print(f"Error executing Django command: {django_command}")
                print(f"Command Output:\n{result.output}")

        elif "Other type of issue" in issue:
            # Placeholder for handling other types of issues and their fixes
            pass

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        return CommandResult(success=(result.returncode == 0), output=result.stdout)
    except Exception as e:
        return CommandResult(success=False, output=f"Error executing command: {str(e)}")

class CommandResult:
    def __init__(self, success, output):
        self.success = success
        self.output = output

def remove_unused_imports(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if "Unused import" not in line:
                file.write(line)

def remove_unused_variables(file_path, unused_variable_issue):
    # Placeholder logic for removing unused variables
    # For demonstration purposes, you can implement more sophisticated logic here
    print(f"Removing unused variable: {unused_variable_issue}")


if __name__ == "__main__":
    # Run the analyzer for a Django project in the current directory
    analyze_and_fix_django_project(".")

