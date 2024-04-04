#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Make a GET request to the Star Wars API
request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (error, response, body) => {
  // Check for errors
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Check if the response status code is 200 (OK)
  if (response.statusCode !== 200) {
    console.error('Error:', `Status code ${response.statusCode}`);
    return;
  }

  // Parse the JSON response body
  const movieData = JSON.parse(body);

  // Print the title of the movie
  console.log(movieData.title);
});
