import { useState } from 'react';
import dashboard_logo from './assets/dashboard_logo.png';
import { w3cwebsocket as W3CWebSocket } from "websocket";

import './Dashboard.css';

/**
 * Displays the dashboard from which players can host or join games.
 */
export default function Dashboard({ setUsername, setGameCode, client, setClient, shouldStartGame }) {
  const [isHost, setIsHost] = useState(true);
  const [hasSubmitted, setHasSubmitted] = useState(false);
  
  const startPage = <StartGame setUsername={setUsername}
    setGameCode={setGameCode} setClient={setClient}
    setIsHost={setIsHost} setHasSubmitted={setHasSubmitted} />

  const waitingPage = <WaitingForGame />
  
  let mainPage;
  if (hasSubmitted) {
    mainPage = waitingPage;
  } else {
    mainPage = startPage;
  }
  
  return (
    <>
    <div className='bg'>
    </div>
      <div className='center-children'>
        {mainPage}
      </div>
    </>
  );
}

/**
 * Displays the host/join game screen.
 */
function StartGame({ setUsername, setGameCode, setClient, setIsHost, setHasSubmitted}) {
  const [tempUsername, setTempUsername] = useState("");
  const [tempGameCode, setTempGameCode] = useState("");

  const maxUsernameLength = 16;
  const joinCodeLength = 6;

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
    setHasSubmitted(true);
    
    createSocket(setClient, code, tempUsername);
    
    e.preventDefault();
  }

  function submitJoin(e) {
    setUsername(tempUsername);
    setGameCode(tempGameCode);
    setIsHost(false);
    setHasSubmitted(true);
    
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
              maxLength={maxUsernameLength}
            />
            <input type='text' placeholder='Join code'
              value={tempGameCode}
              onChange={updateTempGameCode}
              maxLength={joinCodeLength}
            />
            <button type='submit'>Play!</button>
          </div>
        </form>
    </>
  )
}

/**
 * Displays the waiting screen for hosts before someone else has joined.
 */
function WaitingForGame() {
  return (
    <>
        <img id='dashboard-logo' src={dashboard_logo} alt="Logo" />
          <div className='floating-box center-children'>
            <h1>Waiting...</h1>
            <hr />
            <p>Send a friend your join code!</p>
            <div className='blue-widget'>ch36dg</div>
          </div>
          <div className='floating-box center-children'>
            <div className='tip-box'>
              The game will start when two players have joined and the board is loaded.
            </div>
          </div>
    </>
  )
}

/**
 * Sets up the websocket for this client.
 */
function createSocket(setClient, gameCode, username) {
  const gameCodeEncoded = encodeURIComponent(gameCode);
  const usernameEncoded = encodeURIComponent(username);
  const address = 'ws://127.0.0.1:8000/ws/api/' + usernameEncoded + '/' + gameCodeEncoded + '/';
  setClient(new W3CWebSocket(address));
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
function generateGameCode(n) {
  const chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  let code = '';
  for (let i = 0; i < n; i++) {
    code += chars[Math.floor(Math.random() * chars.length)];
  }
  return code;
}