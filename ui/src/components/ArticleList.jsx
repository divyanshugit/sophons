import React from 'react';
import SearchBar from './SearchBar';
import ArticleCard from './ArticleCard';
import './ArticleList.css'; // Import the CSS file for styling
import ArticleImage from '../assets/image1.png';
const articles = [
  {
    id: 1,
    title: 'Unlocking the Power of LLMs: Tips to Build Your Own Agent',
    description: 'Unleash the power of AI by following these tips and tricks to build your own personalized LLM agent.',
    author: 'Sam Pablo',
    image: ArticleImage
  },
  {
    id: 2,
    title: 'Unlocking the Power of LLMs: Tips to Build Your Own Agent',
    description: 'Unleash the power of AI by following these tips and tricks to build your own personalized LLM agent.',
    author: 'Sam Pablo',
    image: ArticleImage
  },
  {
    id: 3,
    title: 'Unlocking the Power of LLMs: Tips to Build Your Own Agent',
    description: 'Unleash the power of AI by following these tips and tricks to build your own personalized LLM agent.',
    author: 'Sam Pablo',
    image: ArticleImage
  }
];

const ArticleList = () => {
  
  return (
    <div className="article-list">
      <SearchBar />
      <div className="tags">
        <button className="ArticleList-buttons">AI</button>
        <button className="ArticleList-buttons">LLM Agents</button>
        <button className="ArticleList-buttons">How to build an Agent</button>
        <button className="ArticleList-buttons">Security</button>
      </div>
      <div className="articles">
        {articles.map(article => (
          <ArticleCard key={article.id} article={article}  />
        ))}
      </div>
    </div>
  );
}

export default ArticleList;
