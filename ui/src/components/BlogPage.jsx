import React from 'react'
import SideBar from './SideBar'
import BellIcon from '../assets/bell_icon.svg'
import AuthorImage from '../assets/AuthorImage.png'
import './BlogPage.css'
import ArticleDetails from './ArticleDetails'
const BlogPage = () => {
  return (
    <div className='BlogPage'>
      <SideBar/>
      <ArticleDetails/>
      <div className='BlogPage-right'>
        <div className='BlogPage-right-top'>
            <div className='BlogPage-right-top-time'>7 July, 19:45</div>
            <img src={BellIcon} style={{height:'25px',width:'25px'}}/>
            <img src={AuthorImage} alt="Sam Pablo" className="author-image" />
        </div>
        <div className='BlogPage-right-bottom'>
            <div className='BlogPage-right-bottom-top'>
                <img className='author-image' src={AuthorImage}/>
                <div className='author-image-text'>Sam Pablo</div>
            </div>
            <div className='BlogPage-right-bottom-top-bottom'>Sam Pablo posted this link on the channel about 7 mins ago.</div>
        </div>
      </div>
    </div>
  )
}

export default BlogPage
