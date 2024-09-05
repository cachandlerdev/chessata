import { useState } from 'react';
import dashboard_logo from './assets/dashboard_logo.png';
import { w3cwebsocket as W3CWebSocket } from "websocket";

import './Dashboard.css';

/**
 * Displays the dashboard from which players can host or join games.
 */
export default function Dashboard({ setUsername, setGameCode, client, setClient }) {
  const [isHost, setIsHost] = useState(true);

  return (
    <>
    <div className='bg'>
    </div>
      <div className='center-children'>
        <StartGame setUsername={setUsername} setGameCode={setGameCode}
          client={client} setClient={setClient} />
      </div>
    </>
  );
}

/**
 * Displays the host/join game screen.
 */
function StartGame({ setUsername, setGameCode, client, setClient }) {
  const [tempUsername, setTempUsername] = useState("");
  const [tempGameCode, setTempGameCode] = useState("");

  const maxUsernameLength = 16;
  const joinCodeLength = 5;

  const updateTempUsername = (e) => setTempUsername(e.target.value);
  const updateTempGameCode = (e) => setTempGameCode(e.target.value);

  function submitHost(e) {
    console.log('Submit host.');
    setUsername(tempUsername);
    const code = generateGameCode(joinCodeLength);
    setGameCode(code);
    
    createSocket(setClient, code);
    
    e.preventDefault();
  }

  function submitJoin(e) {
    console.log('Submit join.');
    setUsername(tempUsername);
    setGameCode(tempGameCode);
    
    createSocket(setClient, tempGameCode);

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
  
}

/**
 * Sets up the websocket for this client.
 */
function createSocket(setClient, gameCode) {
  const gameCodeEncoded = encodeURIComponent(gameCode);
  const address = 'ws://127.0.0.1:8000/ws/api/game_code/' + gameCodeEncoded + '/'
  setClient(new W3CWebSocket(address));
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