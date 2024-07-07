import React from 'react'
import SideBar from './SideBar'
import "./Topic.css"
import DashBoard from './DashBoard'
const Topic = () => {
  return (
    <div className='Topic-main'>
      <SideBar/>
      <DashBoard/>
    </div>
  )
}

export default Topic
