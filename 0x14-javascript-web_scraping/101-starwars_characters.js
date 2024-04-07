#!/usr/bin/node
const request = require('request');

// Function to fetch movie data by movie ID
async function fetchMovieData (movieId) {
  // Constructing the API URL
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  // Making a GET request to the API URL
  return new Promise((resolve, reject) => {
    request.get(apiUrl, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }

      // Checking if the request was successful (status code 200)
      if (response.statusCode === 200) {
        // Parsing the JSON response body
        const movieData = JSON.parse(body);

        // Fetching characters in the order they appear in the movie data
        const characterPromises = movieData.characters.map(characterUrl => {
          return new Promise((resolveCharacter, rejectCharacter) => {
            // Making a GET request to the character URL
            request.get(characterUrl, (err, resp, body) => {
              if (err) {
                rejectCharacter(err);
              } else {
                // Parsing the JSON response body
                const characterData = JSON.parse(body);
                // Resolving with the character name
                resolveCharacter(characterData.name);
              }
            });
          });
        });

        // Resolving with the array of character names
        Promise.all(characterPromises)
          .then(characters => resolve(characters))
          .catch(error => reject(new Error(error))); // Reject with Error object
      } else {
        reject(new Error(`Failed to fetch movie data. Status code: ${response.statusCode}`));
      }
    });
  });
}

// Retrieving command line arguments
const movieId = process.argv[2];

// Checking if the movie ID is provided as argument
if (!movieId) {
  console.error('Usage: node 101-starwars_characters.js <Movie_ID>');
} else {
  // Calling the function to fetch movie data and characters
  fetchMovieData(movieId)
    .then(characters => {
      // Printing character names
      characters.forEach(character => console.log(character));
    })
    .catch(error => {
      console.error('Error:', error.message); // Output only the error message
    });
}
