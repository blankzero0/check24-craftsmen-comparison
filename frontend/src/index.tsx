import React from 'react';
import ReactDOM from 'react-dom/client';
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.min.css';
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import Root from "./routes/root";
import Error from "./components/Error";
import Listing from "./routes/listing";
import './index.css'
import {OpenAPI} from "./api";
import Craftsman from './routes/change';
import GetCraftman from './components/GetCraftman';
import ChangeCraftman from './components/ChangeCraftman';
import SearchingCraftsman from './routes/searchingCraftsman';

if (process.env.REACT_APP_API_URL) {
  OpenAPI.BASE = process.env.REACT_APP_API_URL
}

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root/>,
    errorElement: <Error/>,
  },
  {
    path: '/listing',
    element: <Listing/>,
    errorElement: <Error/>,
  },
  {
    path: '/craftsman',
    element: <Craftsman/>,
    errorElement: <Error/>,
  },
  {
    path: '/searchingCraftsman',
    element: <SearchingCraftsman/>,
    errorElement: <Error/>,
  },
])

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
