import React, { useRef, useState } from 'react';
import './Topics.css';
import image1 from '../assets/image1.png';
import image2 from '../assets/image2.png';
import image3 from '../assets/Image3.png';
import image4 from '../assets/Image4.png';
import DropUp from '../assets/drop_up.svg';

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

const Topics2 = () => {
  const scrollRef = useRef(null);
  const [heading, setHeading] = useState("Today's Topics");

  const scrollRight = () => {
    scrollRef.current.scrollBy({ left: 300, behavior: 'smooth' });
  };

  const handleSelect = (event) => {
    const option = event.target.value;
    switch (option) {
      case 'option1':
        setHeading("Your daily digest is here!");
        break;
      case 'option2':
        setHeading("Yesterday's leftover is here!");
        break;
      case 'option3':
        setHeading("Weekly digest is here!");
        break;
      case 'option4':
        setHeading("Monthly digest is here!");
        break;
      default:
        setHeading("Today's Topics");
    }
  };

  return (
    <div className="topics-container">
      <div className="header">
        <h2>{heading}</h2>
        <div className="dropdown-container">
          <select className="dropdown-toggle-input" onChange={handleSelect}>
            <option value="option1">Today</option>
            <option value="option2">Yesterday</option>
            <option value="option3">Last week</option>
            <option value="option4">Last month</option>
          </select>
          <button className="see-more" onClick={scrollRight}>see more</button>
        </div>
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

export default Topics2;
