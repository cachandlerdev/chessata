import { useState } from 'react';

import './App.css';
import Dashboard from './Dashboard';
import ChessGame from './ChessGame';

export default function App() {
  const [isHost, setIsHost] = useState(true);

  const [username, setUsername] = useState("");
  const [gameCode, setGameCode] = useState("");
  const [client, setClient] = useState();
  
  function shouldShowDashboard() {
    return (username === "") || (gameCode === "");
  }
  
  if (shouldShowDashboard()) {
    return <Dashboard setUsername={setUsername} setGameCode={setGameCode}
      client={client} setClient={setClient} setIsHost={setIsHost} />
  } else {
    return <ChessGame isHost={isHost} username={username} setUsername={setUsername}
      gameCode={gameCode} setGameCode={setGameCode} client={client} />
  }
}