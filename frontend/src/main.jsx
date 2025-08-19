import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";



import {
  QueryClient,
  QueryClientProvider,
 
} from '@tanstack/react-query'
import HomeMain from './pages/HomeMain.jsx';
import Home from './pages/Home.jsx';
import LoginPage from './pages/LoginPage.jsx';
import Logout from './pages/Logout.jsx';
import RegisterPage from './pages/RegisterPage.jsx';
const queryClient = new QueryClient()
const router = createBrowserRouter([
  {
    path: "/",
    element: <HomeMain></HomeMain>,
    children:[
      {
        path:'/',
        element:<Home></Home>
      },
      {
        path:'/login',
        element:<LoginPage></LoginPage>
      },
      {
        path:'/logout',
        element:<Logout></Logout>
      },
      {
        path:'/register',
        element:<RegisterPage></RegisterPage>
      }
    ]
  },
]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
     <QueryClientProvider client={queryClient}>
  <RouterProvider router={router} />
  </QueryClientProvider>
  </StrictMode>,
)
