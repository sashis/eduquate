import axios from 'axios';

async function getPeople(id, render) {
  const response = await fetch(`https://swapi.dev/api/people/`);
  const human = await response.json();
  render(human)
}

async function getStarship(id) {
  let response;
  try {
    response = await axios.get(`https://swapi.dev/api/starships/`);
  } catch (e) {
    return "Can't fetch data from server"
  }
  return response.data
}

getPeople(1, h => console.log(h));
getStarship(2).then(data => console.log(data));