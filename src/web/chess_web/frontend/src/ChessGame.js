import { useState } from 'react';
import { w3cwebsocket as W3CWebSocket } from "websocket";

export default function ChessGame({username, game, client}) {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [userId, setUserId] = useState('');
  
  const updateNewMessage = (e) => setNewMessage(e.target.value);
  
  setupSocket(client);
  
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

function setupSocket(client) {
  if (typeof client !== "undefined") {
    client.onopen = () => {
      console.log('Websocket client connected.')
    };
    
    client.onmessage = (message) => {
      const dataFromServer = JSON.parse(message.data);
      if (dataFromServer) {
        processServerResponse(dataFromServer);
      }
    };
    
    client.onerror = () => {
      console.log('Connection error.');
    };
  }
}

function processServerResponse(data) {
  switch (data["type"]) {
    case 'init':
      console.log('Init');
      break;
    case 'error':
      console.log('Error');
      break;
    case 'join':
      console.log('Join');
      break;
    case 'leave':
      console.log('Leave');
      break;
    case 'start':
      console.log('Start');
      break;
    case 'game_state':
      console.log('Game state');
      break;
    case 'chat':
      console.log('Chat');
      break;
    case 'note':
      console.log('Note');
      break;
    case 'end_of_game':
      console.log('End of game');
      break;
    case 'close':
      console.log('Close match');
      break;
    default:
      console.log('Error: Unsupported server response type.');
      break;
  }
  console.log(data);
}
