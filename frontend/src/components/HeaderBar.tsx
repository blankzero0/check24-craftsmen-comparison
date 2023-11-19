import React from 'react';
import logo from "../check24.svg";
import {Link} from "react-router-dom";

function HeaderBar() {
  return (
    <nav className="navbar navbar-expand py-3 mb-4" style={{backgroundColor: '#063773'}}>
        <div className="container">
        <img src={logo} alt='CHECK24 Logo' width='98' height='24' className='me-3' />
        
          <form>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item dropdown">
                <a className="nav-link dropdown-toggle text-white" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Übersicht
                </a>
                <ul className="dropdown-menu">
                  <li><a className="dropdown-item" href="/searchingCraftsman">Handwerker ändern</a></li>
                  <li><a className="dropdown-item" href="#">Under construction</a></li>
                </ul>
              </li>
              <li className="nav-item">
                <a className="nav-link text-white active" aria-current="page" href="/">Home</a>
              </li>
            </ul>
          </div>
            </form>
        </div>
      </nav>
  );
}

export default HeaderBar;