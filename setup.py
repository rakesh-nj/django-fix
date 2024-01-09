from setuptools import setup, find_packages

setup(
    name='django-fix',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'openai==0.27.0',  
    ],
    entry_points={
        'console_scripts': [
            'django-fix = main:main',
        ],
    },
)
