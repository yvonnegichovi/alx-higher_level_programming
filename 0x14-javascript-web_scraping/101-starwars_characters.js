#!/usr/bin/node
const request = require('request');

async function fetchMovieData(movieId) {
    const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

    return new Promise((resolve, reject) => {
        request.get(apiUrl, (error, response, body) => {
            if (error) {
                reject(error);
                return;
            }

            if (response.statusCode === 200) {
                const movieData = JSON.parse(body);

                const characterPromises = movieData.characters.map(characterUrl => {
                    return new Promise((resolveCharacter, rejectCharacter) => {
                        request.get(characterUrl, (err, resp, body) => {
                            if (err) {
                                rejectCharacter(err);
                            } else {
                                const characterData = JSON.parse(body);
                                resolveCharacter(characterData.name);
                            }
                        });
                    });
                });

                Promise.all(characterPromises)
                    .then(characters => resolve(characters))
                    .catch(error => reject(error));
            } else {
                reject(`Failed to fetch movie data. Status code: ${response.statusCode}`);
            }
        });
    });
}

const movieId = process.argv[2];

if (!movieId) {
    console.error('Usage: node 101-starwars_characters.js <Movie_ID>');
} else {
    fetchMovieData(movieId)
        .then(characters => {
            characters.forEach(character => console.log(character));
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
