// Topics.js
import React, { useRef } from 'react';
import './Topics.css';
import image1 from '../assets/image1.png';
import image2 from '../assets/image2.png';
import image3 from '../assets/Image3.png';
import image4 from '../assets/Image4.png';
const topicsData = [{
    id: 1,
    time: '5 minutes ago',
    readTime: '4 min read',
    title: 'Unlocking the Power of LLMs: Tips to Build Your Own Agent',
    description: 'Unleash the power of AI by following these tips and tricks to build your own personalized LLM agent.',
    author: 'Sam Pablo',
    image: image1,
    authorImage:image3,
  },
  {
    id: 2,
    time: '1 hour ago',
    readTime: '3 min read',
    title: 'Escape Reality: Dive into the Future of VR',
    description: 'VR lets you escape reality, explore new worlds, and experience the future of technology.',
    author: 'Nathalia',
    image: image2,
    authorImage: image4, 
  },
  {
    id: 3,
    time: '5 minutes ago',
    readTime: '4 min read',
    title: 'Unlocking the Power of LLMs: Tips to Build Your Own Agent',
    description: 'Unleash the power of AI by following these tips and tricks to build your own personalized LLM agent.',
    author: 'Sam Pablo',
    image: image1,
    authorImage:image3,
  },
  {
    id: 4,
    time: '1 hour ago',
    readTime: '3 min read',
    title: 'Escape Reality: Dive into the Future of VR',
    description: 'VR lets you escape reality, explore new worlds, and experience the future of technology.',
    author: 'Nathalia',
    image:image2, 
    authorImage: image4, 
  },
  {
    id: 5,
    time: '1 hour ago',
    readTime: '3 min read',
    title: 'Escape Reality: Dive into the Future of VR',
    description: 'VR lets you escape reality, explore new worlds, and experience the future of technology.',
    author: 'Nathalia',
    image:image2, 
    authorImage: image4, 
  },
  {
    id: 6,
    time: '1 hour ago',
    readTime: '3 min read',
    title: 'Escape Reality: Dive into the Future of VR',
    description: 'VR lets you escape reality, explore new worlds, and experience the future of technology.',
    author: 'Nathalia',
    image:image2, 
    authorImage: image4, 
  },
  {
    id: 7,
    time: '1 hour ago',
    readTime: '3 min read',
    title: 'Escape Reality: Dive into the Future of VR',
    description: 'VR lets you escape reality, explore new worlds, and experience the future of technology.',
    author: 'Nathalia',
    image:image2, 
    authorImage: image4, 
  }
];

const Topics = () => {
  const scrollRef = useRef(null);

  const scrollRight = () => {
    scrollRef.current.scrollBy({ left: 300, behavior: 'smooth' });
  };

  return (
    <div className="topics-container">
      <div className="header">
        <h2>Today's Topics</h2>
        <button className="see-more" onClick={scrollRight}>see more</button>
      </div>
      <div className="topics" ref={scrollRef}>
        {topicsData.map((topic) => (
          <div key={topic.id} className="topic-card">
            <img src={topic.image} alt={topic.title} className="topic-image" />
            <div className="topic-details">
              <div className="time-info">
                <span className="time">{topic.time}</span>
                <span className="read-time">{topic.readTime}</span>
              </div>
              <h3 className="title">{topic.title}</h3>
              <p className="description">{topic.description}</p>
              <div className="author-info">
                <img src={topic.authorImage} alt={topic.author} className="author-image" />
                <span className="author-name">{topic.author}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Topics;
