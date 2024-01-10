from setuptools import setup, find_packages

setup(
    name='django-fix',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        # Other dependencies
    ],
    entry_points={
        'console_scripts': [
            'django-fix=analyzer:main',
        ],
    },
)
