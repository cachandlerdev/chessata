import { useState } from 'react';

import './App.css';
import Dashboard from './Dashboard';
import ChessGame from './ChessGame';

export default function App() {
  const [username, setUsername] = useState("");
  const [gameCode, setGameCode] = useState("");
  const [client, setClient] = useState();
  
  const showDashboard = (username === "") && (gameCode === "");
  
  if (showDashboard) {
    return <Dashboard setUsername={setUsername} setGameCode={setGameCode}
      client={client} setClient={setClient} />
  } else {
    return <ChessGame username={username} game={gameCode} client={client} />
  }
}