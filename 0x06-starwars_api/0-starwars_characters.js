#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

let people = [];
const names = [];

const requestCharacters = async () => {
  await new Promise((resolve) =>
    request(filmEndPoint, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        console.error(`Error fetching film data: ${err || res.statusCode}`);
      } else {
        const jsonBody = JSON.parse(body);
        people = jsonBody.characters;
        resolve();
      }
    })
  );
};

const requestNames = async () => {
  if (people.length > 0) {
    for (const p of people) {
      await new Promise((resolve) =>
        request(p, (err, res, body) => {
          if (err || res.statusCode !== 200) {
            console.error(
              `Error fetching character data: ${err || res.statusCode}`
            );
          } else {
            const jsonBody = JSON.parse(body);
            names.push(jsonBody.name);
            resolve();
          }
        })
      );
    }
  } else {
    console.error(`No characters found for movie ID ${movieId}`);
  }
};

const getCharNames = async () => {
  await requestCharacters();
  await requestNames();

  for (const n of names) {
    if (n === names[names.length - 1]) {
      process.stdout.write(n);
    } else {
      process.stdout.write(n + '\n');
    }
  }
};

getCharNames();
