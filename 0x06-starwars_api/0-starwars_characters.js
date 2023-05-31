#!/usr/bin/node
const argv = process.argv;
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, (err, resp, body) => {
  if (err) console.log(err);
  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  const characterNames = {};
  let received = 0;
  for (const character of filmData.characters) {
    request(character, (err, resp, body) => {
      if (err) console.log(err);
      characterNames[character] = JSON.parse(body).name;
      received += 1;
      if (received === characters.length) {
        characters.forEach((url) => { console.log(characterNames[url]); });
      }
    });
  }
});
