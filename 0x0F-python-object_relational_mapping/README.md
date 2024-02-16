# 0x0F. Python - Object-relational mapping

## Description

This project focuses on integrating two significant domains: databases and Python, through Object-Relational Mapping (ORM) using SQLAlchemy. The project entails various tasks related to MySQL databases, ORM concepts, and practical implementations using SQLAlchemy in Python.

## Background Context

In this project, you will delve into the integration of databases with Python, emphasizing the Object-Relational Mapping (ORM) concept. SQLAlchemy, a Python SQL toolkit and Object-Relational Mapper, will be the primary tool used to abstract the storage layer from the application logic.

## Learning Objectives

By the end of this project, you should be able to explain:

- Why Python programming is beneficial for database interactions
- How to establish connections to MySQL databases from Python scripts
- How to perform SELECT and INSERT operations in MySQL tables using Python
- The concept of Object-Relational Mapping (ORM) and its advantages
- How to map Python classes to MySQL database tables using SQLAlchemy
- Creating and managing Python Virtual Environments for dependency isolation

## Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- MySQLdb version 2.0.x and SQLAlchemy version 1.4.x are required
- Files must be executable and end with a new line
- The first line of all files must be `#!/usr/bin/python3`
- Code must comply with `pycodestyle` (version 2.8.*)
- All modules, classes, and functions must have documentation strings
- Documentation must be meaningful, explaining the purpose of the module, class, or function
- No direct use of `execute` with SQLAlchemy
- Length of files will be tested using `wc`
- Virtual Environment creation and activation required for dependency isolation
- No plagiarism or unauthorized publication of project content

## Tasks

The project consists of several tasks focusing on different aspects of ORM with SQLAlchemy, including database interactions, model creation, querying, filtering, and more.

## Resources

- Object-relational mappers
- MySQLdb documentation (mysqlclient)
- SQLAlchemy documentation and tutorials
- Python Virtual Environments: A primer
- Python SQLAlchemy Cheatsheet
- SQLAlchemy ORM Tutorial

## Repository Structure

The project repository follows a specific structure:

0x0F-python-object_relational_mapping/
|-- 0-select_states.py
|-- 1-filter_states.py
|-- 2-my_filter_states.py
|-- 3-my_safe_filter_states.py
|-- ...
|-- model_state.py
|-- model_city.py
|-- README.md


Each task is implemented as a separate Python script within the project directory. Additionally, `model_state.py` and `model_city.py` contain the class definitions for the State and City objects, respectively.

## Usage

Each Python script in the repository corresponds to a specific task and can be executed directly from the command line, providing the required arguments as described in the task instructions.

Example usage:

$ ./0-select_states.py root root hbtn_0e_0_usa

Environment Setup
Installing MySQLdb Version 2.0.x
MySQLdb is installed alongside MySQL. Follow these steps to ensure the correct version:

bash
Copy code
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
Installing SQLAlchemy Version 1.4.x
Ensure SQLAlchemy is installed with the correct version:

bash
Copy code
$ sudo pip3 install SQLAlchemy
Credits
This project was developed by Guillaume as part of the ALX Software Engineering Program.

This README.md file provides an overview of the project, its learning objectives, requirements, tasks, resources, repository structure, usage instructions, environment setup, and credits. It serves as a comprehensive guide for anyone working on or reviewing the project.
