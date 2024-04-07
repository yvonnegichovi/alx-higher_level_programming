#!/usr/bin/node
const request = require('request');

function countCompletedTasks(apiUrl) {
    request.get(apiUrl, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
            return;
        }

        if (response.statusCode === 200) {
            const todos = JSON.parse(body);

            const completedTasksByUser = {};

            todos.forEach(todo => {
                if (todo.completed) {
                    if (completedTasksByUser[todo.userId]) {
                        completedTasksByUser[todo.userId]++;
                    } else {
                        completedTasksByUser[todo.userId] = 1;
                    }
                }
            });

            // Printing the result
            console.log(completedTasksByUser);
        } else {
            console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
        }
    });
}

// Retrieving command line arguments
const apiUrl = process.argv[2];

// Checking if the API URL is provided as argument
if (!apiUrl) {
    console.error('Usage: node 6-completed_tasks.js <API_URL>');
} else {
    // Calling the function to compute completed tasks by user id
    countCompletedTasks(apiUrl);
}
