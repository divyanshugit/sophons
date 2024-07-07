import React from 'react';
import './SearchBar.css'; // Import the CSS file for styling

const SearchBar = () => {
  return (
    <div className="search-bar">
      <input type="text" placeholder="Search your topics here..." className='search-bar-discover'/>
    </div>
  );
}

export default SearchBar;
