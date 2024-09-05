import { useState } from 'react';

import './App.css';
import Dashboard from './Dashboard';
import ChessGame from './ChessGame';

export default function App() {
  const [username, setUsername] = useState("");
  const [gameCode, setGameCode] = useState("");
  
  if (!username || !gameCode) {
    return <Dashboard setUsername={setUsername} setGame={setGameCode} />
  } else {
    return <ChessGame username={username} game={gameCode} />
  }
}

