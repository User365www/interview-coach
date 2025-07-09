import React, { Component } from "react";
import LoginPage from "./LoginPage";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return <p>This is the home page</p>
  }
}