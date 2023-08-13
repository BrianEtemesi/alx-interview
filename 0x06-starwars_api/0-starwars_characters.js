#!/usr/bin/node
/* star wars api */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const data = [];

// Make a request to the Star Wars API
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    // Parse the response body and retrieve character URLs
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      // Initialize data array with character URLs and placeholder for names
      data.push({ url: characters[i], name: '' });

      // Make requests to retrieve character names
      request(characters[i], function (error, resp, body2) {
        if (error) {
          console.log(error);
        }
        // Update data array with character names
        data[i].name = JSON.parse(body2).name;

        // If all names are retrieved, print the character names
        if (checkdata(data)) {
          for (let j = 0; j < data.length; j++) {
            console.log(data[j].name);
          }
        }
      });
    }
  }
});

// Function to check if all character names are retrieved
function checkdata(data) {
  for (let i = 0; i < data.length; i++) {
    if (data[i].name === '') {
      return false;
    }
  }
  return true;
}
