Is a React Hook that let's you add a reducer to your component. We call this at the top level of the component to manage it's state.

Reducers are pure functions that specifies how the state get's updated. It must be pure, should take in current state and should return the next state.

Reducers by themselves are best at managing the state of a single component and it's children but not for using at a global state across many sibling components. React's context API is required for this use case.

#### Dispatch function

The `dispatch` function returned by the `useReducer` helps you update the state to a different value and trigger a re-render. We pass in the `action` as the only argument to the `dispatch` function. 

```jsx
const [state, dispatch] = useReducer(reducer, { age: 42 });  

function handleClick() {  
	dispatch({ type: 'incremented_age' });  
	// ...
```

##### Caveats

The `dispatch` function only updates the state variable for the next render. If you read the state after calling the `dispatch` function, you will still get the old value that was on screen before the call

If the new value is identical to the current `state` as determined by an `Object.is` comparison, React will `skip re rendering the component and its children`.

React `batches state updates`. This updates the screen after all the event handlers have run and have called their `set` function. In the rare case that we need to force React to update the screen earlier, we can use `flushSync`.

#### flushSync

Flush sync is a way to ensure that by the time the next line of code runs, React has already updated the DOM.

Follow https://react.dev/reference/react-dom/flushSync for further reading

#### Back to `useReducer`

This is very similar to `useState` , but it lets you move the state update logic from event handlers to a `single function outside of your component.`

This is a pure function which `takes in the current state and returns the next state.`

The State that is passed inside the reducer is a `Read Only` state.

When we write reducer code, `useReducer` does not re render the DOM if the same state object is returned from the reducer function. Always consider the input state to the DOM to be immutable and return a new state object with updated values from the reducer. Only then `useReducer` will trigger a Re render of the DOM.



