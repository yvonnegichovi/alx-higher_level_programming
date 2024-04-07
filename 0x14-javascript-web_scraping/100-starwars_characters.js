#!/usr/bin/node
const request = require('request');

function fetchCharacters (movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);

      movieData.characters.forEach(characterUrl => {
        request.get(characterUrl, (err, resp, body) => {
          if (err) {
            console.error('Error fetching character:', err);
          } else {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          }
        });
      });
    } else {
      console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    }
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 100-starwars_characters.js <Movie_ID>');
} else {
  fetchCharacters(movieId);
}
