# React Hooks

## Use State

### Description

The state hook in React is a way to add stateful behavior to functional components. It allows to declare a piece of state and then update it when necessary.
The function returns an array with two values: the current state value and a function to update the state. Those values are used to render your component based on the current state and update the state when necessary.

### Example useState

1. Import the hook from react. 

```
import { useState } from "react";
import ReactDOM from "react-dom/client";
```

2. Initalize the Hook

```
function FavoriteColor() {
    const [color, setColor] = useState("red");
}
```

3. implement the return 

```
import { useState } from "react";
import ReactDOM from "react-dom/client";

function FavoriteColor() {
  const [color, setColor] = useState("red");

  return (
    <>
      <h1>My favorite color is {color}!</h1>
      <button
        type="button"
        onClick={() => setColor("blue")}
      >Blue</button>
    </>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<FavoriteColor />);
```

By pressing the Button the ChangeState 'setColor' gets Changed there for the Component get's rerendert.
the current state of 'color' gets changed to blue. 


## useEffect

### Description
