import { useState } from 'react';
import dashboard_logo from './assets/dashboard_logo.png';

import './Dashboard.css';

export default function Dashboard({ setUsername, setGame }) {
  const [tempUsername, setTempUsername] = useState("");
  const [tempGameCode, setTempGameCode] = useState("");

  function handleSubmit(e) {
    setUsername(tempUsername);
    setGame(tempGameCode);
    e.preventDefault();
  }
  
  function submitHost(e) {
    console.log('Submit host.');
    setUsername(tempUsername);
    e.preventDefault();
  }

  function submitJoin(e) {
    console.log('Submit join.');
    setUsername(tempUsername);
    setTempGameCode(tempGameCode);
    e.preventDefault();
  }
  
  const updateTempUsername = (e) => setTempUsername(e.target.value);
  const updateTempGameCode = (e) => setTempGameCode(e.target.value);

  return (
    <>
    <div className='bg'>
    </div>
      <div className='center-children'>
        <img id='dashboard-logo' src={dashboard_logo} alt="Logo" />
        <form noValidate onSubmit={e => submitHost(e)}>
          <div className='floating-box center-children'>
            <h1>Host</h1>
            <hr />
            <input type='text' name='host-username' placeholder='Username'
              value={tempUsername}
              onChange={updateTempUsername}
              autoFocus />
            <button type='submit'>Play!</button>
          </div>
        </form>
        <form noValidate onSubmit={e => submitJoin(e)}>
          <div className='floating-box center-children'>
            <h1>Join</h1>
            <hr />
            <input type='text' name='friend-username' placeholder='Username'
              value={tempUsername}
              onChange={updateTempUsername}
            />
            <input type='text' placeholder='Join code'
              value={tempGameCode}
              onChange={updateTempGameCode}
            />
            <button type='submit'>Play!</button>
          </div>
        </form>
      </div>
    </>
  );
}