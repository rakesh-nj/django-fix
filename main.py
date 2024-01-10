# # main.py

# import argparse
# from analyzer import analyze_and_fix_django_project

# def main():
#     parser = argparse.ArgumentParser(description='Django CLI Debugger - Django-Fix')
#     parser.add_argument('project_path', type=str, help='Path to the Django project')
#     args = parser.parse_args()

#     analyze_and_fix_django_project(args.project_path)

# if __name__ == "__main__":
#     main()

# main.py

from analyzer import analyze_and_fix_django_project

def main():
    # Your main execution logic here
    analyze_and_fix_django_project("path/to/your/django/project")

if __name__ == "__main__":
    main()

