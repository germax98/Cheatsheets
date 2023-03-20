# Redux

## Description

Redux is a state management library for JavaScript applications. It provides a predictable and centralized way to manage the state of your application, making it easier to reason about and maintain as it grows in complexity.

## Terminology:
- Store: An object that holds the state of the application
- Action: A plain JavaScript object that describes a change in the state
- Reducer: A function that takes the current state and an action, and returns a new state
- Dispatch: A function that sends an action to the store, triggering a state change
- Subscriber: A function that listens for changes to the store and updates the UI

## Example (easy)

```
// Define the initial state of the counter
const initialState = { count: 0 };

// Define the reducer function
function counterReducer(state = initialState, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    default:
      return state;
  }
}

// Create the store
const store = Redux.createStore(counterReducer);

// Subscribe to changes in the store
store.subscribe(() => {
  console.log(store.getState());
});

// Dispatch an action to increment the counter
store.dispatch({ type: 'INCREMENT' });

// Dispatch an action to decrement the counter
store.dispatch({ type: 'DECREMENT' });

```

In this example, we define an initial state for the counter, and a reducer function that takes the current state and an action and returns a new state. We then create a store using the createStore method from the Redux library, and subscribe to changes in the store using the subscribe method. Finally, we dispatch two actions to the store using the dispatch method to increment and decrement the counter, respectively.


## Advancet 

- Selectors: Functions that retrieve data from the store and transform it into a specific shape for the UI to use.
- Actions: Functions that generate action objects to be dispatched to the store. They can also be asynchronous and dispatch multiple actions.
- Middleware: Functions that intercept actions before they reach the reducer, allowing you to add additional behavior to the dispatch process.
- Thunks: A type of middleware that allows you to write async actions using functions that return a function. These functions can dispatch multiple actions and have access to the store and other data.
- Immutability: Since the state in Redux should be treated as read-only, it's important to use immutable data structures to avoid accidentally modifying the state. Libraries like Immutable.js or Immer can help with this.

### Example Selectors

Let's say you have an array of todos in your Redux store, and you want to display only the completed todos in your UI. You can create a selector function that filters the todos based on their completed status:

```
// Define a selector function to get the completed todos
function getCompletedTodos(state) {
  return state.todos.filter(todo => todo.completed);
}
```

You can then use this selector function in your UI component to display only the completed todos:


```
import { useSelector } from 'react-redux';
import { getCompletedTodos } from './selectors';

function TodoList() {
  const completedTodos = useSelector(getCompletedTodos);

  return (
    <ul>
      {completedTodos.map(todo => (
        <li key={todo.id}>{todo.text}</li>
      ))}
    </ul>
  );
}
```

In this example, the useSelector hook is used to retrieve the completed todos from the Redux store by calling the getCompletedTodos selector function. The completedTodos variable is then used to render the list of completed todos in the UI.

This example demonstrates how selectors can be used to compute derived data from the Redux store and decouple the UI from the internal structure of the store. By defining selectors for specific pieces of data, you can easily reuse them across different components and avoid duplicating computation logic.


### Example Actions

Let's say you have a simple todo list application and you want to define actions for adding a todo and marking a todo as completed. You can create two action creators that return objects with a type property and any additional data that is needed:

```
export const addTodo = (text) => ({
  type: 'ADD_TODO',
  payload: {
    id: Date.now(),
    text,
    completed: false,
  },
});

// Define the COMPLETE_TODO action
export const completeTodo = (id) => ({
  type: 'COMPLETE_TODO',
  payload: {
    id,
  },
});
```
In this example, addTodo and completeTodo are action creator functions that take any necessary data as arguments and return an object with a type property and a payload property. The type property is a string that describes the type of action being performed, and the payload property contains any additional data needed to perform the action.

To dispatch these actions in your Redux application, you can import the action creators and call them inside your component or other parts of your code:

```
import { addTodo, completeTodo } from './actions';

// Dispatch an ADD_TODO action
store.dispatch(addTodo('Buy milk'));

// Dispatch a COMPLETE_TODO action
store.dispatch(completeTodo(1));
```
In this example, we import the addTodo and completeTodo action creators from a file called actions.js. We then use the store.dispatch method to dispatch the actions to the Redux store. The addTodo action includes the text of the todo that we want to add, and the completeTodo action includes the ID of the todo that we want to mark as completed.


### Example Middlewear

Let's say you want to log every action that is dispatched in your Redux application. You can create a middleware function that logs the action and passes it along to the next middleware or the reducer:

```
const loggerMiddleware = store => next => action => {
  console.log('Dispatching action:', action);
  const result = next(action);
  return result;
};
```
In this example, loggerMiddleware is a function that takes the store object as its argument and returns another function that takes the next middleware or reducer as its argument and returns yet another function that takes the action object as its argument. Inside the middleware function, we log the action and then pass it along to the next middleware or reducer by calling next(action). Finally, we return the result of calling next(action).

To use this middleware in your Redux application, you can pass it as an argument to the applyMiddleware function when creating your store:

```
import { createStore, applyMiddleware } from 'redux';
import rootReducer from './reducers';
import loggerMiddleware from './middleware/logger';

const store = createStore(rootReducer, applyMiddleware(loggerMiddleware));
```

In this example, we import the createStore and applyMiddleware functions from Redux, as well as our rootReducer and loggerMiddleware functions. We then create the Redux store by passing the rootReducer to createStore and passing loggerMiddleware to applyMiddleware.

Now, every time an action is dispatched in your application, the middleware function will log the action to the console before passing it along to the reducer. This can be useful for debugging and understanding the flow of actions in your application.


