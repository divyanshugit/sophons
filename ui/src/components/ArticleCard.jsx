import React from 'react';
import './ArticleCard.css'; 
import { useNavigate } from 'react-router-dom';
const ArticleCard = ({ article }) => {
  const navigate = useNavigate();
  const handleButtonClick1 = () => {
    navigate('/blogpage');
  };
  return (
    <div className="article-card">
      <div className="article-info">
        <h2 className='article-card-title'>{article.title}</h2>
        <p className='article-card-desc'>{article.description}</p>
        <div className="author">
          <img src={article.image} alt={article.author} className="author-image" />
          <span className='article-card-author'>{article.author}</span>
        </div>
      </div>
      <div className="article-image">
        <img src={article.image} alt={article.title} />
      </div>
      <div className="read-more">
        <button className='read-more-button' onClick={handleButtonClick1}>→</button>
      </div>
    </div>
  );
}

export default ArticleCard;
