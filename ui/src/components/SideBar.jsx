import React from 'react'
import sophonsLogo from '../assets/sophons_logo.svg'
import dashBoard from '../assets/dashboard.svg'
import overview from '../assets/overview.svg'
import settings from '../assets/settings.svg'
import logout from '../assets/logout.svg'
import { useNavigate } from 'react-router-dom';
import './SideBar.css'
const SideBar = () => {
  const navigate = useNavigate();
  const handleButtonClick1 = () => {
    navigate('/discover');
  };
  const handleButtonClick2 = () => {
    navigate('/topic');
  };
  return (
    <div className='sideBar-main'>
      <div className='sidebar-top'>
        <div className='sidebar-top-logo'>
        <div className='sidebar-top-logo-image' src={sophonsLogo}>
          <img src={sophonsLogo} style={{width: '49px', height: '49px', color:'#6E63E5',margin:'0px 0px 0px 12px'}}/>
        </div>
            <div className='sidebar-top-logo-text'>Sophons</div>
        </div>
        <div className='sidebar-top-overview'>
            <div className='sidebar-top-overview-text'>OVERVIEW</div>
            <div className='sidebar-top-overview-options'>
                <div className='sidebar-top-overview-option'>
                    <div className='sidebar-overview-option-image' src={dashBoard}>
                      <img src={dashBoard} style={{width: '22.75px', height: '22.75px', color:'#6E63E5',margin:'0px 10px 0px 5px'}}onClick={handleButtonClick2}/>
                    </div>
                    <div className='sidebar-overview-option-text'onClick={handleButtonClick2}>Dashboard</div>
                </div>
                <div className='sidebar-top-overview-option'>
                    <div className='sidebar-overview-option-image' src={overview}>
                      <img src={overview} style={{width: '27px', height: '27px', color:'#6E63E5',margin:'0px 8px 0px 2px'}} onClick={handleButtonClick1}/>
                    </div>
                    <div className='sidebar-overview-option-text'onClick={handleButtonClick1}>Discover</div>
                </div>
            </div>
        </div>
      </div>
      <div className='sidebar-bottom'>
        <div className='sidebar-bottom-settings-text'>SETTINGS</div>
        <div className='sidebar-bottom-settings-options'>
            <div className='sidebar-bottom-settings-option'>
                <div className='sidebar-bottom-settings-option-image' src={settings}>
                  <img src={settings} style={{width: '25px', height: '25px', color:'#404040',margin:'0px 10px 0px 0px'}}/>
                </div>
                <div className='sidebar-bottom-settings-option-text'>Settings</div>
            </div>
            <div className='sidebar-bottom-settings-option'>
                <div className='sidebar-bottom-settings-option-image' src={logout}>
                  <img src={logout} style={{width: '25px', height: '28px', color:'#FF6969',margin:'0px 10px 0px 0px'}}/>
                </div>
                <div className='sidebar-bottom-settings-option-text2'>Log out</div>
            </div>
        </div>
      </div>
    </div>
  )
}

export default SideBar
