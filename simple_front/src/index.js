import axios from 'axios';

const api_root = API_URL;

async function getAccount(id) {
  const response = await fetch(`${api_root}/accounts/${id}/`);
  return await response.json();
}

async function getCourses() {
  try {
    const res = await axios.get(`${api_root}/courses/`);
    return res.data;
  } catch (e) {
    return 'Can\'t fetch data from server';
  }
}

getAccount(1).then(account => console.log(account));
getCourses().then(data => console.log(data));