#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Status code ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);

  const films = data.results;

  const numberOfFilms = films.reduce((count, film) => {
    if (film.characters.some(char => char.endsWith(`/${characterId}/`))) {
      return count + 1;
    }
    return count;
  }, 0);

  console.log(numberOfFilms);
});
