# React Hooks

[useState](#useState)  
[useEffect](#useEffect)  
[useContext](#useContext)  
  

<a name="useState"/>

## UseState

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

<a name="useEffect"/>

## useEffect

### Description

The useEffect hook in JavaScript is used in React functional components to perform side effects, such as fetching data, updating the DOM, or subscribing to events. It runs after every render of the component, and it takes two arguments: a function that performs the side effect, and an optional array of dependencies that specify when the effect should run. The function can return a cleanup function that runs before the next effect, or when the component unmounts. The dependencies array can be used to control when the effect runs by including variables that the effect depends on. 

the cycle of use Effect is divided in three parts.

1. mounting- Gets called when the page is loaded

2. updating- Gets Called if a value Changes or new Data is beeing fetched

3. unmounting- Gets called if a Component gets unmounted of a page.

### Example 

- Import the Use Effect Hook:
```
import { useState, useEffect } from "react";
```

- Example of a useEffect hook only at mounting
```

function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    setTimeout(() => {
      setCount((count) => count + 1);
    }, 1000);
  }, []); // <- add empty brackets here

  return <h1>I've rendered {count} times!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Timer />);
```

- Example of a useEffect hook with updating

```

function Counter() {
  const [count, setCount] = useState(0);
  const [calculation, setCalculation] = useState(0);

  useEffect(() => {
    setCalculation(() => count * 2);
  }, [count]); // <- add the count variable here

  return (
    <>
      <p>Count: {count}</p>
      <button onClick={() => setCount((c) => c + 1)}>+</button>
      <p>Calculation: {calculation}</p>
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Counter />);
```

- Example of a useEffect hook with unmounting (cleanup)

```

function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    let timer = setTimeout(() => {
    setCount((count) => count + 1);
  }, 1000);

  return () => clearTimeout(timer)
  }, []);

  return <h1>I've rendered {count} times!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Timer />);
```


<a name="useContext"/>

## useContext

React Context is a way to manage state globally. It can be used together with the useState Hook to share state between deeply nested components more easily than with useState alone.

### Example useContext

1. Create Context and initalize it 

```
import { useState, createContext } from "react";
import ReactDOM from "react-dom/client";
const UserContext = createContext()
```

2. Create a Context Provider
Wrap child components in the Context Provider and supply the state value. This allows the access of the data between files with Context.

```
function Component1() {
  const [user, setUser] = useState("Jesse Hall");

  return (
    <UserContext.Provider value={user}>
      <h1>{`Hello ${user}!`}</h1>
      <Component2 user={user} />
    </UserContext.Provider>
  );
}
```

3. Use the useContext Hook
To use the data in another file. It is needed to import the useContext hook.

```
import { useState, createContext, useContext } from "react";
```

4. implement the data in the File. 

```
function Component5() {
  const user = useContext(UserContext);

  return (
    <>
      <h1>Component 5</h1>
      <h2>{`Hello ${user} again!`}</h2>
    </>
  );
}
```
