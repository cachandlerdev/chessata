import { useState } from 'react';
import dashboard_logo from './assets/dashboard_logo.png';
import game_logo from './assets/game_logo.png';

import './Dashboard.css';
import './ChessGame.css';

export default function ChessGame({ isHost, username, setUsername, gameCode, setGameCode, client }) {
  const [userId, setUserId] = useState('');
  const [userRole, setUserRole] = useState('');
  const [color, setColor] = useState('');

  const [showMatch, setShowMatch] = useState(false);

  const [numOfPlayers, setNumOfPlayers] = useState(0);
  const [boardData, setBoardData] = useState([]);
  const [isYourTurn, setIsYourTurn] = useState(false);
  const [isOver, setIsOver] = useState(false);
  const [matchState, setMatchState] = useState('');
  const [moves, setMoves] = useState([]);
  const [chatMessages, setChatMessages] = useState([]);
  const [notifications, setNotifications] = useState([]);
  
  const [newMove, setNewMove] = useState();

  function setupSocket(client) {
    if (typeof client !== "undefined") {
      client.onopen = () => {
        console.log('Websocket connected.');
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
    } else {
      console.log('Error: Socket is undefined.');
    }
  }

  function processServerResponse(data) {
    console.log(data);
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
      case 'move':
        processMove(data);
        break;
      case 'chat':
        processChat(data);
        break;
      case 'close':
        processClose(data);
        break;
      default:
        console.log('Error: Unsupported server response type.');
        break;
    }
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
    let textRole;
    if (data['role'] === 'player') {
      textRole = 'Player';
    } else {
      textRole = 'Spectator';
    }
    let newNotificationMsg = `${textRole} '${data['username']}' has joined the match.`;
    const notifyData = { 'type': 'join', 'message': newNotificationMsg };
    setNotifications([notifyData, ...notifications]);

    setNumOfPlayers(data['num_of_players']);
    if (data['num_of_players'] < 2 && !isHost) {
      // Exit match.
      resetAllVars();
    } else if (data['num_of_players'] === 2) {
      setShowMatch(true);
    }
  }

  /**
   * Handles leave packets from the server.
   */
  function processLeave(data) {
    let textRole;
    if (data['role'] === 'player') {
      textRole = 'Player';
    } else {
      textRole = 'Spectator'
    }
    let newNotificationMsg = `${textRole} '${data['username']}' has left the match.`;
    const notifyData = { 'type': 'leave', 'message': newNotificationMsg };
    setNotifications([notifyData, ...notifications]);
  }

  /**
   * Handles start packets from the server.
   */
  function processStart(data) {
    setColor(data['color']);
    setShowMatch(true);
  }

  /**
   * Processes game state updates from the server.
   */
  function processGameState(data) {
    const state = data['state'];
    setIsYourTurn(state['your_turn']);
    setMatchState(state['match_state']);
    setBoardData(state['board']);
    
    if (state['match_state'] !== 'not over') {
      let newNotification = {'type': 'match_state'};
      switch (state['match_state']) {
        case 'white check':
          newNotification['message'] = 'The white king is in check!';
          break;
        case 'black check':
          newNotification['message'] = 'The black king is in check!';
          break;
        case 'stalemate':
          newNotification['message'] = 'The match ended in a stalemate.';
          break;
        case 'white win':
          newNotification['message'] = 'White won the game!';
          break;
        case 'black win':
          newNotification['message'] = 'Black won the game!';
          break;
        default:
          console.log('Error: Unsupported match state');
          break;
      }
      setNotifications([newNotification, ...notifications]);
    } else {
      const filtered = notifications.filter((notification) => {
        return notification['type'] !== 'match_state';
      })
      setNotifications(filtered);
    }

    setNewMove();
    
    const isGameOver = (state['match_state'] === 'white win' || state['match_state'] === 'black win' || state['match_state'] === 'stalemate' );
    
    if (isGameOver) {
      setIsOver(true);
    }
  }
  
  /**
   * Processes move packets from the server.
   */
  function processMove(data) {
    const serverMove = {
      "start": data['start'],
      "end": data['end'],
      "is_white": data['is_white']
    };
    setMoves([...moves, serverMove]);
  }

  /**
   * Processes chat packets from the server.
   */
  function processChat(data) {
    const chatMessage = { 'username': data['username'], 'message': data['message'] };
    setChatMessages([...chatMessages, chatMessage])
  }

  /**
   * Processes close packets from the server.
   */
  function processClose(data) {
    console.log('Close match');
    resetAllVars();
  }
  
  function resetAllVars() {
    setUserId('');
    setUserRole('');
    setColor('');

    setShowMatch(false);
    setUsername('');
    setGameCode('');

    setNumOfPlayers(0);
    setBoardData([]);
    setIsYourTurn(false);
    setIsOver(false);
    setMatchState('');
    setMoves([]);
    setChatMessages([]);
    setNotifications([]);
    client.close();
  }

  setupSocket(client);

  if (showMatch) {
    return (
      <>
        <div className='board-container'>
          <BoardPage color={color} boardData={boardData} client={client}
            moves={moves} messages={chatMessages} username={username}
            isYourTurn={isYourTurn} notifications={notifications}
            isGameOver={isOver} resetAllVars={resetAllVars} newMove={newMove}
            setNewMove={setNewMove} userRole={userRole} gameCode={gameCode} />
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
      <div className='bg'></div>
      <div className='center-children'>
        <div className='dashboard-banner center-children'>
          <img id='dashboard-logo' src={dashboard_logo} alt="Logo" />
          <div className='floating-box center-children'>
            <h1>Waiting...</h1>
            <hr />
            <p>Send a friend your join code!</p>
            <div className='blue-widget big-widget'>{gameCode}</div>
          </div>
          <div className='floating-box center-children'>
            <div className='tip-box'>
              The game will start when two players have joined and the board is loaded.
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

function BoardPage({ color, boardData, client, moves, messages, username,
  isYourTurn, isGameOver, notifications, resetAllVars, newMove, setNewMove,
  userRole, gameCode }) {

  const [newChatMessage, setNewChatMessage] = useState('');
  const updateNewChatMessage = (e) => setNewChatMessage(e.target.value);

  function sendMessage(e, message) {
    if (message.startsWith('/m')) {
      // Process it as a move instead
      
      if (!isGameOver) {
        const userInput = message.split(' ');
        if (userInput.length === 3 || userInput.length === 4) {
          const start = userInput[1];
          const end = userInput[2];        
          
          let promotion;
          if (userInput.length === 4) {
            promotion = userInput[3];
          } else {
            promotion = "queen";
          }
          
          client.send(
            JSON.stringify({
              type: "move",
              start: start,
              end: end,
              promotion: promotion,
            })
          );
          setNewChatMessage('');
          e.preventDefault();

          return;
        }
      }
    }

    // Otherwise treat it as a regular chat message.
    client.send(
      JSON.stringify({
        type: "chat",
        message: newChatMessage,
      })
    );
    setNewChatMessage('');
    e.preventDefault();
  }

  return (
    <div className='horizontal-window-box'>
      <div className='vertical-window-box'>
        <LogoWindow gameCode={gameCode} />
        <NotifyWindow isYourTurn={isYourTurn} notifications={notifications}
          isGameOver={isGameOver}/>
      </div>
      <div className='vertical-window-box center-children'>
        <Board playerColor={color} boardData={boardData} newMove={newMove}
          setNewMove={setNewMove} client={client} isGameOver={isGameOver}
          userRole={userRole} />  
        <button id='surrender-button' className='blue-button'
          onClick={resetAllVars}>Leave Match</button>
      </div>
      <div className='vertical-window-box'>
        <MovesWindow moves={ moves } />
        <ChatWindow messages={messages} sendMessage={sendMessage}
          newChatMessage={newChatMessage}
          updateNewChatMessage={updateNewChatMessage} />
      </div>
    </div>
  );
}

function Board({ playerColor, boardData, newMove, setNewMove, client,
  isGameOver, userRole }) {

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
        boardPos={position} rowText={rowText} columnText={columnText}
        newMove={newMove} setNewMove={setNewMove} client={client}
        isGameOver={isGameOver} userRole={userRole} />;
      boardSquares[index] = {"position": position, "square": square };

      if (j !== boardLen - 1) {
        isWhiteSquare = !isWhiteSquare;
      }
    }
  }
  
  if (playerColor === 'black') {
    // TODO: Find a more performance efficient way to reverse the board view
    boardSquares.reverse();
  }
  return (
    <div id='board'>
      {boardSquares.map((square_data) => (
        <div key={square_data['position']}>
          {square_data['square']}
        </div>
      ))}
    </div>
  )
}

function Square({ is_white, pieceType, boardPos, rowText, columnText, newMove,
  setNewMove, client, isGameOver, userRole }) {
  
  function sendMove(start, end) {
    // TODO: Support multiple promotion types.
    if (!isGameOver) {
      let promotion = 'queen';
      client.send(
        JSON.stringify({
          type: "move",
          start: start,
          end: end,
          promotion: promotion,
        })
      );
      setNewMove();
    }
  }

  function handleLeftClick() {
    if (typeof (newMove) === 'undefined') {
      if (pieceType !== 0) {
        setNewMove(boardPos);
      }
    } else {
      const start = newMove;
      sendMove(start, boardPos);
    }
  }

  function handleRightClick(e) {
    setNewMove();
    e.preventDefault();
  }
  
  const squareContents = (<>
    <div className='piece-row-text'>{rowText}</div>
    <div className='piece-column-text'>{columnText}</div>
    <Piece pieceType={pieceType} />
  </>);
  
  let color;
  if (is_white) {
    color = 'white';
  } else {
    color = 'black';
  }

  let selected = '';
  if (typeof (newMove) !== 'undefined') {
    if (newMove === boardPos && userRole === 'player') {
      selected = 'selected';
    }
  }
  
  let selectable = '';
  if (pieceType !== 0 && userRole === 'player') {
    selectable = 'selectable';
  }
  
  if (!isGameOver) {
    return <div className={`board-square ${color} ${selectable} ${selected}`}
      onClick={handleLeftClick} onContextMenu={handleRightClick}>
      {squareContents}
    </div>;
  } else {
    return <div className={`board-square ${color} ${selectable}`}>
      {squareContents}
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

function ChatWindow({messages, sendMessage, newChatMessage, updateNewChatMessage}) {

  return (
    <div id='chat' className='floating-box center-children'>
      <h1>Chat</h1>
      <hr />
      <div className='messages'>
        {messages.map((message, index) => (
          <div key={index}>
            <b>{message.username}: </b>{message.message}
          </div>
        ))}
      </div>
      <form noValidate onSubmit={(e) => sendMessage(e, newChatMessage)}>
        <div id='chat-input-box' className='horizontal-children small-gap'>
          <input type='text' placeholder='Type something...' value={newChatMessage}
            onChange={updateNewChatMessage} />
          <button type='submit'>{'>'}</button>
        </div>
      </form>
    </div>
  );
}

function MovesWindow({ moves }) {
  return (
    <div id='moves' className='floating-box center-children'>
      <h1>Moves</h1>
      <hr />
      <div className='moves'>
        <div className='moves-content'>
          {moves.map((move, index) => (
            <div key={index}>
              <MoveItem move={move} />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

function MoveItem({ move }) {
  if (move['is_white']) {
    return <div className='move move-white'>
      <b>White:</b> {move['start']} -{'>'} {move['end']}
    </div>
  } else {
    return <div className='move move-black'>
      <b>Black:</b> {move['start']} -{'>'} {move['end']}
    </div>    
  }
}

function NotifyWindow({ isYourTurn, notifications, isGameOver }) {
  let turnText;
  if (!isGameOver) {
    if (isYourTurn) {
      turnText = 'Your Turn!';
    } else {
      turnText = 'Waiting...';
    }
  } else {
    turnText = 'Match Finished!';
  }
  return (
    <div id='notify' className='floating-box center-children'>
      <h1>{ turnText }</h1>
      <hr></hr>
      <div className='notifications'>
        {notifications.map((notification, index) => (
          <div key={index} className='move move-black'>
            <b>Note: </b>{notification['message']}
          </div>
        ))}
      </div>
    </div>
  );
}

function LogoWindow({ gameCode }) {
  return (
    <div id='logo' className='floating-box center-children'>
      <img src={game_logo} alt='Logo'/>
      <div className='game-code'><b>Game code:</b> { gameCode }</div>
    </div>
  );
}
