import React from 'react';
import ReactDOM from 'react-dom/client';
import { NextUIProvider } from '@nextui-org/react';
import { AppContextProvider } from './AppContext';
import App from './App.jsx';
import './index.css';


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <NextUIProvider>
      <AppContextProvider>
        <App />
      </AppContextProvider>
    </NextUIProvider>
  </React.StrictMode>,
);
