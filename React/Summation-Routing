# ----------------React Routing---------

To use Routing in React the package routing is needed. There for enter the command:

yarn add react-router-dom@6

into the Terminal

## ----------------index.js---------

import the PAckage into the index.js file 

import {BrowserRouter} from 'react-router-dom';

Browserrouter acts like a React component. There fore wrap rhe code inside the return statement inside the component Browser Router like in the example.
This Code enables the Routing inside the React Application.


Example: 
```
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>  
  </React.StrictMode>
);
```

## ----------------routes ----------------

Add a new Folder named 'routes' where all Routing Components are added. 

Add the Components like the Example.

Example: 
```
import { Fragment } from 'react'
import { Outlet, Link } from "react-router-dom"
import{ ReactComponent as CrwnLogo} from '../../assets/crown.svg'
import './navigation.styles.scss'

const Navigation = ()=> {
    return (
      <Fragment>
        <div className='navigation'>
            <Link className='logo-container' to='/'>
                <CrwnLogo className='logo'/>
            </Link>
            
            <div className='nav-links-container'>
                <Link className='nav-link' to= '/shop'>
                    SHOP
                </Link>
            </div>
        </div>
        <Outlet />
      </Fragment>
    )
  }
  ```
  export default Navigation

### ----------------Fragment----------------

Fragment is a component in React that allows you to return multiple components or elements without adding an extra node to the DOM. It's often used when you want to return multiple elements but don't want to wrap them in an additional HTML element.


### ----------------Link----------------
Link is a component in the "react-router-dom" library that is used for navigation in React applications. It's similar to an HTML <a> tag, but it's specifically designed to work with React Router and provides a way to navigate to different routes in your application. with the attribute 'to' I am able to specifie where the path should lead.


### ----------------Outlet----------------
The Outlet component is part of the "react-router" library, which provides routing capabilities for React applications. It is used to specify where the components associated with the current route should be rendered (before or after).
