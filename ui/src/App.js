import React from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import './App.css'

import Home from '../src/components/Home'
import Discover from '../src/components/Discover'
import BlogPage from '../src/components/BlogPage'
import Topic from '../src/components/Topic'
import ChatPage from '../src/components/ChatPage'
const App = () => {
  return (
    <Router>
        <Routes>
          <Route exact path="/" element={<Home/>}/>
          <Route exact path="/discover" element={<Discover/>}/>
          <Route exact path="/blogpage" element={<BlogPage/>}/>
          <Route exact path="/topic" element={<Topic/>}/>
          <Route exact path="/chatpage" element={<ChatPage/>}/>
        </Routes>
    </Router>
  );
}

export default App;