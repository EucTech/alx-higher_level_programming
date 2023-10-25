#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body).results;
    const filmNum = movie.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log(`${filmNum.length}`);
  }
});
