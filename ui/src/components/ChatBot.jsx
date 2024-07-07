import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './ChatBot.css';

const ChatBot = () => {
  const [messages, setMessages] = useState([
    {
      message: "Hello, I'm ChatGPT! Ask me anything!",
      sentTime: "just now",
      sender: "ChatGPT"
    }
  ]);
  const [inputMessage, setInputMessage] = useState('');
  const messageListRef = useRef();

  useEffect(() => {
    // Scroll to the bottom smoothly whenever messages change
    if (messageListRef.current) {
      messageListRef.current.scrollTop = messageListRef.current.scrollHeight;
    }
  }, [messages]);

  const handleSend = async () => {
    if (inputMessage.trim() === '') return;

    const newMessage = {
      message: inputMessage,
      sentTime: "just now",
      sender: "user"
    };
    setMessages([...messages, newMessage]);
    setInputMessage('');

    try {
      const response = await axios.post('http://localhost:5001/api/chat-completion', {
        model: "mistralai/Mistral-7B-Instruct-v0.1",
        messages: [
          { role: "system", content: "You are a helpful assistant." },
          { role: "user", content: newMessage.message }
        ]
      });

      const data = response.data;
      setMessages([...messages, newMessage, {
        message: data.choices[0]?.message?.content,
        sender: "ChatGPT"
      }]);
    } catch (error) {
      console.error('Error generating chat completion:', error);
      setMessages([...messages, newMessage, {
        message: 'An error occurred while generating the chat completion.',
        sender: "ChatGPT"
      }]);
    }
  };

  return (
    <div className='chatbot-container'>
      <div className='chatbot-messages' ref={messageListRef}>
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.sender === 'ChatGPT' ? 'ai-message' : 'user-message'}`}>
            {message.message}
          </div>
        ))}
      </div>
      <div className='chatbot-input-form'>
        <input
          type="text"
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' ? handleSend() : null}
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};

export default ChatBot;
