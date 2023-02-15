# React Context

React Context is a way to share the user Data between multible Pages in React. To fullfill this task a new Hook is needed. This hook is named createContext.

This Hook is combined with the useStateHook. 
import { createContext, useState } from "react";

1. Define a default State for the crecreateContext Hook
```
export const UserContext = createContext({
    currentUser: null,
    setCurrentUser: ()=>null,
})
```

2.
Setup the useState Hook which is overwriting the default state of the Context hook.

```
export const UserProvider = ({children}) =>{
    const [currentUser, setCurrentUser]=useState(null)
    const value = {currentUser, setCurrentUser}//gives Access to user information inside index.js 

    return <UserContext.Provider value={value}>{children}</UserContext.Provider>
}
```

3. 
by wrapping the entire app in index.js inside the effect hook, it is possible to get the user information between diffrent Pages.

```
<UserProvider>
    <app/>
</UserProvider>
```

4.
To make the user information between components accesable you need to first import the Hook. 

```
import { Fragment,useContext } from 'react'
```

after that you can call the Hook by:
```
const {currentUser} = useContext(UserContext)
```

it returns the Current User Data
