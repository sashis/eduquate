import React, {Component} from 'react';
import axios from 'axios';
import AppBar from './AppBar';
import Footer from './Footer';
import MainPage from '../pages/MainPage';

export default class App extends Component {
  state = {
    courses: [],
  };

  async componentDidMount() {
    try {
      const {data} = await axios.get('http://127.0.0.1:8000/api/v1/courses/');
      this.setState({courses: data});
    } catch (e) {
      this.setState({courses: []});
    }
  }

  render() {
    return (
        <>
          <AppBar />
          <MainPage />
          <Footer />
        </>
    );
  }
}
