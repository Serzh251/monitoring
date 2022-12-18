import React from 'react';
import { createRoot } from 'react-dom/client';
import './static/css/index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

// ReactDOM.render(<App />, document.getElementById('root'));
const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);
serviceWorker.unregister();

