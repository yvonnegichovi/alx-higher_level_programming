0x13. JavaScript - Objects, Scopes and Closures

Description

This project contains solutions to various tasks related to JavaScript objects, scopes, and closures. Each task is implemented in a separate JavaScript file and covers topics such as class definition, inheritance, instance methods, function definition, and more.

Requirements

All files are interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x).
All files must end with a new line.
The first line of each file must be #!/usr/bin/node.
All files must be executable.
All files must be semistandard compliant.
Code must follow Standard JavaScript style with semicolons.

Installation
To run the scripts in this project, make sure you have Node.js installed on your system. If not, you can install it by running:

$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

You also need to install the semistandard package globally to ensure your code follows the required style:

$ sudo npm install semistandard --global

Usage
Each task is implemented in a separate JavaScript file. To run a specific task, use the following command:

$ ./file_name.js


Replace file_name.js with the name of the JavaScript file containing the solution code for the task you want to execute.

Tasks

Rectangle #0: Define an empty class Rectangle.
Rectangle #1: Define a class Rectangle with a constructor that initializes width and height.
Rectangle #2: Extend the Rectangle class to handle cases where width or height is not a positive integer.
Rectangle #3: Extend the Rectangle class with an instance method to print the rectangle using 'X'.
Rectangle #4: Extend the Rectangle class with instance methods to manipulate the rectangle.
Square #0: Define a class Square that inherits from Rectangle and initializes a square with a single argument.
Square #1: Extend the Square class with an instance method to print the square using a specified character.
Occurrences: Write a function to return the number of occurrences of a specific element in a list.
Esrever: Write a function to reverse the elements of a list without using the built-in reverse() method.
Log me: Write a function to print the number of arguments already printed and the new argument value.
Number conversion: Write a function to convert a number from base 10 to another base passed as an argument.

Author
Yvonne Ng'endo

License
This project is licensed under the MIT License.
