import React from 'react'
import SideBar from './SideBar'
import './SideBar.css'
import ChatBot from './ChatBot'
import './ChatPage.css'
const ChatPage = () => {
  return (
    <div className='ChatPage'>
      <SideBar/>
      <ChatBot/>
    </div>
  )
}

export default ChatPage
