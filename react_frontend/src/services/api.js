import axios from 'axios';

const API_ROOT = 'http://127.0.0.1:8000/api/v1';

class Api {
  constructor(root_url) {
    this.root_url = root_url;
  }

  async getCourses() {
    const {data} = await axios.get(`${this.root_url}/courses/`);
    return data;
  }

  async getTopCourses(top_count = 3) {
    const courses = await this.getCourses();
    return courses.slice(0, top_count);
  }
}

export default new Api(API_ROOT);