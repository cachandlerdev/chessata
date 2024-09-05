import { useState } from 'react';
import { w3cwebsocket as W3CWebSocket } from "websocket";

import './App.css';

export default function App() {
  const [username, setUsername] = useState("");
  const [game, setGame] = useState("");
  
  if (!username || !game) {
    return <LoginPage setUsername={setUsername} setGame={setGame} />
  } else {
    return <ChatPage username={username} game={game} />
  }
}

function LoginPage({ setUsername, setGame }) {
  const [tempUsername, setTempUsername] = useState("");
  const [tempGame, setTempRoom] = useState("");

  function handleSubmit(e) {
    setUsername(tempUsername);
    setGame(tempGame);
    e.preventDefault();
  }

  return (
    <form noValidate
      onSubmit={(e) => handleSubmit(e)}
    >
      <input type='text' name='username' autoFocus
        placeholder='Username'
        onChange={e => {
          setTempUsername(e.target.value);
        }}
      />
      <input type='text' name='room'
        placeholder='Game name'
        onChange={e => {
          setTempRoom(e.target.value);
        }}
      />
      <button type="submit">Submit</button>
    </form>
  )
}

function ChatPage({username, game}) {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [client, setClient] = useState();
  
  const updateNewMessage = (e) => setNewMessage(e.target.value);
  
  if (!client) {
    setClient(new W3CWebSocket('ws://127.0.0.1:8000/ws/api/' + game + '/'));
  }
  
  if (client) {
    client.onopen = () => {
      console.log('Websocket client connected.')
    };
    
    client.onmessage = (message) => {
      const dataFromServer = JSON.parse(message.data);
      if (dataFromServer) {
        setMessages([
          ...messages,
          { name: dataFromServer.sender, msg: dataFromServer.text, }
        ]);
      }
    };
    
    client.onerror = () => {
      console.log('Connection error.');
    };
  }
  
  
  function sendMessage(e) {
    client.send(
      JSON.stringify({
        type: "message",
        text: newMessage,
        sender: username,
      })
    );
    setNewMessage('');
    e.preventDefault();
  }

  return (
    <>
      <h1>Game Name: {game}</h1>
      <h4>Username: {username}</h4>
      <hr />
      <h2>Messages</h2>
      {messages.map((message, index) => (
        <div key={index}>
          <b>{message.name}: </b>{message.msg}
        </div>
      ))}
      <form noValidate onSubmit={(e) => sendMessage(e)}>
        <input type="text" autoFocus placeholder='Type a message...' value={newMessage}
          onChange={updateNewMessage}
        />
        <button type='submit'>Send</button>
      </form>
    </>
  )
}
