#!/usr/bin/env python3
"""
AWESOME-EMU-V1 - Setup Script
"""

from setuptools import setup, find_packages
import os

# Read README
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "AWESOME-EMU-V1 - Ultimate Cybersecurity Command & Control Platform"

# Read requirements
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(req_path):
        with open(req_path, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="awesome-emu",
    version="1.0.0",
    author="Ian Carter Kulani",
    author_email="ian.carter@awesome-emu.com",
    description="Ultimate Cybersecurity Command & Control Platform",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/iancarterkulani/awesome-emu",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'awesome-emu=awesome_emu:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['*.txt', '*.md', '*.json', '*.html', '*.css', '*.js'],
    },
    zip_safe=False,
)
