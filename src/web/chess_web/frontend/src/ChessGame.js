import { useState } from 'react';
import { w3cwebsocket as W3CWebSocket } from "websocket";
import dashboard_logo from './assets/dashboard_logo.png';

import './Dashboard.css';
import './ChessGame.css';

export default function ChessGame({ isHost, username, setUsername, gameCode, setGameCode, client }) {
  const [userId, setUserId] = useState('');
  const [userRole, setUserRole] = useState('');
  const [color, setColor] = useState('');

  const [numOfPlayers, setNumOfPlayers] = useState(0);
  const [boardData, setBoardData] = useState([]);
  const [isYourTurn, setIsYourTurn] = useState(false);
  const [isOver, setIsOver] = useState(false);
  const [matchState, setMatchState] = useState('');

  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [showMatch, setShowMatch] = useState(false);

  const updateNewMessage = (e) => setNewMessage(e.target.value);

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
        processInit(data);
        break;
      case 'error':
        processError(data);
        break;
      case 'join':
        processJoin(data);
        break;
      case 'leave':
        processLeave(data);
        break;
      case 'start':
        processStart(data);
        break;
      case 'game_state':
        processGameState(data);
        break;
      case 'chat':
        processChat(data);
        break;
      case 'note':
        processNote(data);
        break;
      case 'end_of_game':
        console.log('End of game');
        break;
      case 'close':
        processClose(data);
        break;
      default:
        console.log('Error: Unsupported server response type.');
        break;
    }
    console.log(data);
  }

  /**
   * Handles init packets from the server.
   */
  function processInit(data) {
    setUserId(data['user_id']);
    setUserRole(data['role']);
  }

  /**
   * Handles error packets from the server.
   */
  function processError(data) {
    console.log('Error');
  }

  /**
   * Handles join packets from the server.
   */
  function processJoin(data) {
    console.log('Join');
    setNumOfPlayers(data['num_of_players']);
    if (data['num_of_players'] < 2 && !isHost) {
      // Exit match.
      setShowMatch(false);
      setGameCode('');
      setUsername('');
    } else if (data['num_of_players'] === 2) {
      setShowMatch(true);
    }
  }

  /**
   * Handles leave packets from the server.
   */
  function processLeave(data) {
    console.log('Leave');
  }

  /**
   * Handles start packets from the server.
   */
  function processStart(data) {
    console.log('Start');
    setColor(data['color']);
    setShowMatch(true);
  }

  /**
   * Processes game state updates from the server.
   */
  function processGameState(data) {
    console.log('Game state');
    const state = data['state'];
    setIsYourTurn(state['your_turn']);
    setMatchState(state['match_state']);
    setBoardData(state['board']);
  }

  /**
   * Processes chat packets from the server.
   */
  function processChat(data) {
    console.log('Chat');
  }

  /**
   * Processes note updates from the server.
   */
  function processNote(data) {
    console.log('Note');
  }

  /**
   * Processes close packets from the server.
   */
  function processClose(data) {
    console.log('Close match');
  }

  setupSocket(client);


  if (showMatch) {
    //return (
    //  <>
    //    <h1>Game Name: {gameCode}</h1>
    //    <h4>Username: {username}</h4>
    //    <hr />
    //    <h2>Messages</h2>
    //    {messages.map((message, index) => (
    //      <div key={index}>
    //        <b>{message.name}: </b>{message.msg}
    //      </div>
    //    ))}
    //    <form noValidate onSubmit={(e) => sendMessage(e)}>
    //      <input type="text" autoFocus placeholder='Type a message...' value={newMessage}
    //        onChange={updateNewMessage}
    //      />
    //      <button type='submit'>Send</button>
    //    </form>
    //  </>
    //);
    return (
      <>
        <div className='board-container'>
          <BoardPage color={color} boardData={boardData} />
        </div>
      </>
    );
  } else {
    return (
      <>
        <div className='bg'>
        </div>
        <div className='center-children'>
          <WaitingPage gameCode={gameCode} />
        </div>
      </>
    );
  }

}

/**
 * Displays the waiting screen for hosts before someone else has joined.
 */
function WaitingPage({ gameCode }) {
  return (
    <>
      <img id='dashboard-logo' src={dashboard_logo} alt="Logo" />
      <div className='floating-box center-children'>
        <h1>Waiting...</h1>
        <hr />
        <p>Send a friend your join code!</p>
        <div className='blue-widget'>{gameCode}</div>
      </div>
      <div className='floating-box center-children'>
        <div className='tip-box'>
          The game will start when two players have joined and the board is loaded.
        </div>
      </div>
    </>
  )
}

function BoardPage({ color, boardData }) {
  return <Board playerColor={color} boardData={boardData} />
}

function Board({ playerColor, boardData }) {

  function boardIndexToPos(index) {
    const column = String.fromCharCode((index % 8) + 97);
    const row = 8 - Math.floor(index / 8);
    return `${column}${row}`;
  }

  if (typeof (boardData) === 'undefined') {
    return;
  }

  const boardLen = 8;
  let isWhiteSquare = true; // Top left square is always white
  const boardSquares = Array(boardLen * boardLen);
  for (let i = 0; i < boardLen; i++) {
    // For each row
    for (let j = 0; j < boardLen; j++) {
      // For each square
      let index;
      let position;

      // Calculate square position, and determine whether num/letter should be 
      // shown.
      let displayRowText = false;
      let displayColumnText = false;

      if (playerColor === 'black') {
        index = 63 - ((boardLen * i) + j);
        position = boardIndexToPos(index);

        if (position[1] === '8') {
          displayColumnText = true;
        }
        if (position[0] === 'a') {
          displayRowText = true;
        }
      } else {
        index = (boardLen * i) + j;
        position = boardIndexToPos(index);

        if (position[1] === '1') {
          displayColumnText = true;
        }
        if (position[0] === 'h') {
          displayRowText = true;
        }
      }
      
      console.log(index);

      const pieceType = boardData[index];

      let rowText = '';
      let columnText = '';
      if (displayRowText) {
        rowText = position[1];
      }
      if (displayColumnText) {
        columnText = position[0];
      }

      const square = <Square is_white={isWhiteSquare} pieceType={pieceType}
        boardPos={position} rowText={rowText} columnText={columnText} />;
      boardSquares[index] = square;

      if (j !== boardLen - 1) {
        isWhiteSquare = !isWhiteSquare;
      }
    }
  }
  
  if (playerColor === 'black') {
    // TODO: Find a more performance efficient way to reverse the board view
    boardSquares.reverse();
  }

  console.log(boardSquares);
  return (
    <div id='board'>
      {boardSquares.map((square) => (
        <div key={square.boardPos}>
          {square}
        </div>
      ))}
    </div>
  )
}

function Square({ is_white, pieceType, boardPos, rowText, columnText }) {
  if (is_white) {
    return <div className='board-square white'>
      <div className='piece-row-text'>{rowText}</div>
      <div className='piece-column-text'>{columnText}</div>
      <Piece pieceType={pieceType} />
    </div>;
  } else {
    return <div className='board-square black'>
      <div className='piece-row-text'>{rowText}</div>
      <div className='piece-column-text'>{columnText}</div>
      <Piece pieceType={pieceType} />
    </div>;
  }
}

function Piece({ pieceType }) {
  let pieceName;
  switch (Math.abs(pieceType)) {
    case 6:
      pieceName = 'king';
      break;
    case 5:
      pieceName = 'queen';
      break;
    case 4:
      pieceName = 'bishop';
      break;
    case 3:
      pieceName = 'knight';
      break;
    case 2:
      pieceName = 'rook';
      break;
    case 1:
      pieceName = 'pawn';
      break;
    default:
      pieceName = 'none';
      break;
  }
  let color;
  if (pieceType > 0) {
    color = 'white';
  } else {
    color = 'black';
  }

  const imgPath = `${window.location.origin}/pieces/${color}_${pieceName}.svg`;
  const altText = `${color} ${pieceName}`;

  if (pieceName !== 'none') {
    return (
      <div className='board-piece'>
        <img src={imgPath} alt={altText} />
      </div>
    );
  }
}