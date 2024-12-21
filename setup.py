# setup.py
from setuptools import setup, find_packages

setup(
    name="todo_app",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'todo=todo.main:main',
        ],
    },
    description="A simple to-do list application",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Vedp9984",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)
