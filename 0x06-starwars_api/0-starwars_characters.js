#!/usr/bin/node
const argv = process.argv
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, (err, resp, body) => {
  const film_data = JSON.parse(body);
  const characters = film_data.characters;
  const character_names = {};
  let received = 0;
  for (const character of film_data["characters"]) {
    request(character, (err, resp, body) => {
      character_names[character] = JSON.parse(body).name;
      received += 1;
      if (received === characters.length) {
        characters.map((url) => { console.log(character_names[url]); });
      }
    });
  }
});
