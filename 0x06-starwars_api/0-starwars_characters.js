#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters (filmId) {
  const endpt = 'https://swapi-api.hbtn.io/api/films/' + filmId;
  let answer = await (await request(endpt)).body;
  answer = JSON.parse(answer );
  const characters = answer .characters;

  for (let i = 0; i < characters.length; i++) {
    const urlChar = characters[i];
    let character = await (await request(urlChar)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

starwarsCharacters(filmID);
