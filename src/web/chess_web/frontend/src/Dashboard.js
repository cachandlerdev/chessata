import { useState } from 'react';
import dashboard_logo from './assets/dashboard_logo.png';
import { w3cwebsocket as W3CWebSocket } from "websocket";

import './Dashboard.css';

/**
 * Displays the dashboard from which players can host or join games.
 */
export default function Dashboard({ setUsername, setGameCode, setClient, setIsHost }) {
  
  return (
    <>
    <div className='bg'></div>
      <div className='center-children'>
        <div className='dashboard-banner center-children'>
          <StartGame setUsername={setUsername} setGameCode={setGameCode} setClient={setClient} setIsHost={setIsHost} />
        </div>
      </div>
    </>
  );
}

/**
 * Displays the host/join game screen.
 */
function StartGame({ setUsername, setGameCode, setClient, setIsHost}) {
  const [tempUsername, setTempUsername] = useState("");
  const [tempGameCode, setTempGameCode] = useState("");

  const maxUsernameLength = 16;
  const joinCodeLength = 5;

  const updateTempUsername = (e) => {
    const stripped = sanitizeInput(e.target.value);
    setTempUsername(stripped);
  };
  const updateTempGameCode = (e) => {
    const stripped = sanitizeInput(e.target.value);
    setTempGameCode(stripped);
  };

  function submitHost(e) {
    setUsername(tempUsername);
    const code = generateGameCode(joinCodeLength);
    setGameCode(code);
    setIsHost(true);
    
    createSocket(setClient, code, tempUsername);
    
    e.preventDefault();
  }

  function submitJoin(e) {
    setUsername(tempUsername);
    setGameCode(tempGameCode);
    setIsHost(false);
    
    createSocket(setClient, tempGameCode, tempUsername);

    e.preventDefault();
  }


  return (
    <>
        <img id='dashboard-logo' src={dashboard_logo} alt="Logo" />
        <form noValidate onSubmit={e => submitHost(e)}>
          <div className='floating-box center-children'>
            <h1>Host</h1>
            <hr />
            <input type='text' name='host-username' placeholder='Username'
              value={tempUsername}
              onChange={updateTempUsername}
              maxLength={maxUsernameLength}
              autoFocus />
            <button className='blue-button' type='submit'>Play!</button>
          </div>
        </form>
        <form noValidate onSubmit={e => submitJoin(e)}>
          <div className='floating-box center-children'>
            <h1>Join</h1>
            <hr />
            <input type='text' name='friend-username' placeholder='Username'
              value={tempUsername}
              onChange={updateTempUsername}
              maxLength={maxUsernameLength}
            />
            <input type='text' placeholder='Join code'
              value={tempGameCode}
              onChange={updateTempGameCode}
              maxLength={joinCodeLength}
            />
            <button className='blue-button' type='submit'>Play!</button>
          </div>
        </form>
    </>
  )
}

/**
 * Sets up the websocket for this client.
 */
function createSocket(setClient, gameCode, username) {
  const gameCodeEncoded = encodeURIComponent(gameCode);
  const usernameEncoded = encodeURIComponent(username);
  
  var location = window.location, new_uri;
  if (location.protocol === 'https:') {
    new_uri = 'wss:';
  } else {
    new_uri = 'ws:';
  }
  const serverAddress = '127.0.0.1';
  new_uri += '//' + serverAddress + ':8000/';
  //const serverAddress = 'chessata-django.onrender.com/';
  //new_uri += '//' + serverAddress;
  new_uri += 'ws/api/' + usernameEncoded + '/' + gameCodeEncoded + '/';
  const socket = new W3CWebSocket(new_uri);
  console.log(new_uri);
  setClient(socket);
}

/**
 * Remove all non-alphanumberic characters from a string.
 */
function sanitizeInput(input) {
  return input.replace(/\W/g, '');
}

/**
 * Generates a game code of length n.
 */
function generateGameCode(length) {
  const chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  let result = '';
  for (var i = length; i > 0; --i) {
    result += chars[Math.floor(Math.random() * chars.length)];   
  } 
  return result;
}