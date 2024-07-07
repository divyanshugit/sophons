import React from 'react';
import './DashBoard.css';
import Image1 from '../assets/image1.png'
const Dashboard = () => {
  return (
<div style={{ display: 'flex', flexDirection: 'column', padding: '20px', fontFamily: 'Arial, sans-serif',overflowX:'hidden' }}>
<header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
<input
          type="text"
          placeholder="Search for interesting topics here!"
          className='dashboard-search'
          style={{ padding: '10px 20px', width: '50%' ,borderRadius:'20px'}}
        />
<div style={{ display: 'flex', alignItems: 'center' }}>
<span>7 July, 19:45</span>
<div style={{ marginLeft: '20px' }}>
<img src={Image1} alt="Profile" style={{ borderRadius: '50%', width: '40px' }} />
</div>
</div>
</header>
<div style={{ marginTop: '20px' }}>
<button className='dashboard-buttons'>AI</button>
<button className='dashboard-buttons'>LLM Agents</button>
<button className='dashboard-buttons'>How to build an Agent</button>
<button className='dashboard-buttons'>Security</button>
</div>
 
      <div style={{ display: 'flex', marginTop: '20px' }}>
<div style={{ flex: 3, marginRight: '20px' }}>
<section style={{ marginBottom: '40px' }}>
<h2>Read Blogs out here!</h2>
<div style={{ display: 'flex' }}>
<div style={{ marginRight: '20px' ,width:'200px',backgroundColor:'#fff',padding:'10px',borderRadius:'20px'}}>
<img src={Image1} alt="Blog" style={{ width: '90%', borderRadius: '10px',margin:'0px 0px 10px 0px' }} />
<div className='h-dashboard'>Unlocking the Power of LLMs: Tips to Build Your Own Agent</div>
<p className='p-dashboard'>Unleash the power of AI by following these tips and tricks to build your own personalized LLM agent.</p>
</div>
<div style={{ marginRight: '20px' ,width:'200px',backgroundColor:'#fff',padding:'10px',borderRadius:'20px'}}>
<img src={Image1} alt="Blog" style={{ width: '90%', borderRadius: '10px',margin:'0px 0px 10px 0px'  }} />
<div className='h-dashboard'>Unlocking the Power of LLMs: Tips to Build Your Own Agent</div>
<p className='p-dashboard'>Unleash the power of AI by following these tips and tricks to build your own personalized LLM agent.</p>
</div>
<div style={{ marginRight: '20px' ,width:'200px',backgroundColor:'#fff',padding:'10px',borderRadius:'20px'}}>
<img src={Image1} alt="Blog" style={{ width: '90%', borderRadius: '10px',margin:'0px 0px 10px 0px'  }} />
<div className='h-dashboard'>Unlocking the Power of LLMs: Tips to Build Your Own Agent</div>
<p className='p-dashboard'>Unleash the power of AI by following these tips and tricks to build your own personalized LLM agent.</p>
</div>
<div style={{ marginRight: '20px' ,width:'200px',backgroundColor:'#fff',padding:'10px',borderRadius:'20px'}}>
<img src={Image1} alt="Blog" style={{ width: '90%', borderRadius: '10px',margin:'0px 0px 10px 0px'  }} />
<div className='h-dashboard'>Unlocking the Power of LLMs: Tips to Build Your Own Agent</div>
<p className='p-dashboard'>Unleash the power of AI by following these tips and tricks to build your own personalized LLM agent.</p>
</div>
</div>
</section>
 
          <section style={{ marginBottom: '40px' }}>
<h2>Watch your videos here!</h2>
<div style={{ display: 'flex', overflowX: 'hidden' }}>
<div style={{ marginRight: '20px' ,backgroundColor:'#fff',padding:'10px',borderRadius:'20px'}}>
<img src={Image1} alt="Video" style={{ width: '100%', borderRadius: '10px' }} />
<p>1h 16m 24s</p>
</div>
<div style={{ marginRight: '20px',backgroundColor:'#fff',padding:'10px',borderRadius:'20px' }}>
<img src={Image1} alt="Video" style={{ width: '100%', borderRadius: '10px' }} />
<p>1h 16m 24s</p>
</div>
<div style={{ marginRight: '20px',backgroundColor:'#fff',padding:'10px',borderRadius:'20px' }}>
<img src={Image1} alt="Video" style={{ width: '100%', borderRadius: '10px' }} />
<p>1h 16m 24s</p>
</div>
</div>
</section>
 
          <section>
<h2>Read deep-research papers here!</h2>
<div style={{ display: 'flex', overflowX: 'scroll' }}>
<div style={{ marginRight: '20px',backgroundColor:'#fff',padding:'10px',borderRadius:'20px' }}>
<h3>The Rise and Potential of Large Language Model Based Agents</h3>
<p>124 citations</p>
<p>This paper surveys the rapidly developing field of LLM-based agents...</p>
</div>
<div style={{ marginRight: '20px',backgroundColor:'#fff',padding:'10px',borderRadius:'20px' }}>
<h3>Reflexion: Language Agents with Verbal Reinforcement Learning</h3>
<p>52 citations</p>
<p>Reflexion proposes a framework for LLM agents that utilizes verbal reinforcement...</p>
</div>
<div style={{ marginRight: '20px',backgroundColor:'#fff',padding:'10px',borderRadius:'20px' }}>
<h3>Expel: LLM Agents Are Experiential Learners</h3>
<p>38 citations</p>
<p>This research introduces Expel, a novel approach for training LLM agents...</p>
</div>
</div>
</section>
</div>
 
        <aside style={{ flex: 1 }}>
{/* <div style={{ textAlign: 'center', padding: '20px', borderRadius: '10px', backgroundColor: '#f0f0f0' }}>
<h2>Artificial Intelligence</h2>
<p>14 shared blogs</p>
<p>4 shared videos</p>
<p>12 shared papers</p>
</div> */}
</aside>
</div>
</div>
  );
};
 
export default Dashboard;