import search from '../assets/search.svg';
import './Home.css';
import SideBar from './SideBar'
import seeMore from '../assets/seemore_arrow.svg'
import Calender from './Calender'
import StatsGraph from './StatsGraph'
import RealTime from './RealTime'
import Topics from './Topics'
function Home() {
  return (
    <div className="App">
    <SideBar className='app-sidebar-component'/>
      <div className='app-right'>
        <div className='app-right-main'>
        <div className='app-right-main-top'>
            <div className='app-right-main-top-top'>
              <div className='greetings'>
                <div className='greetings1'>Welcome back,</div>
                <div className='greetings2'>Enkrypters</div>
              </div>
              <div className='timings'><RealTime/></div>
            </div>
            <div className='app-right-main-top-search'>
              <div className='search-icon'>
                <img src={search} style={{width:'22px',height:'22px'}}></img>
              </div>
              <input className='search-search' placeholder='Search your topics here...'></input>
            </div>
            
        </div>
            <Topics />
          <div className='app-right-main-bottom'>
            <div className='app-right-main-bottom-text'>Trendy Topics</div>
            <div className='app-right-main-bottom-content'></div>
          </div>
        </div>
        <div className='app-right-side'>
          <div className='app-right-calender'><Calender/></div>
          <div className='app-right-status'><StatsGraph/></div>
        </div>
      </div> 
    </div>
  );
}

export default Home;
