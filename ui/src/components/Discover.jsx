import React from 'react'
import './Discover.css'
import SideBar from './SideBar'
import Topics2 from './Topics2'
import ArticleList from './ArticleList'
import TopicInventoryChart from './TopicInventoryChary'
const Discover = () => {
  return (
    <div className='Discover'>
      <SideBar className='discover-sidebar-component'/>
      <div className='discover-right'>
        <div className='discover-right-main'>
            <Topics2/>
            <ArticleList/>
        </div>
        <div className='discover-right-sidebar'>
            <TopicInventoryChart/>
        </div>
      </div>
    </div>
  )
}

export default Discover
