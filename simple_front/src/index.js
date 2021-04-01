import axios from 'axios';

const api_root = API_URL;

async function getAccount(id = 1) {
  try {
    const response = await fetch(`${api_root}/accounts/${id}/`);
    return await response.json();
  } catch (e) {
    return 'Can\'t fetch data from server';
  }
}

async function getCourses() {
  try {
    const res = await axios.get(`${api_root}/courses/`);
    return res.data;
  } catch (e) {
    return 'Can\'t fetch data from server';
  }
}

function initPanel(panelElement, fetchFunction) {
  const [button, plane] = panelElement.children;
  button.onclick = () => {
    fetchFunction().then(data => {
      plane.innerHTML = JSON.stringify(data, null, 2);
    });
  };
}

initPanel(document.getElementById('axios-panel'), getCourses);
initPanel(document.getElementById('fetch-panel'), getAccount);
