import React, {Component} from 'react';
import axios from 'axios';
import './App.css';

export default class App extends Component {
  state = {
    courses: {}
  }

  componentDidMount() {
    axios.get()
  }

  render() {
    return <div>Hello World!</div>
  }
}
