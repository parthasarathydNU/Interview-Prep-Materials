https://react.dev/reference/react/hooks

Hooks let us use different React features from our components. We can either use built-in hooks or combine them to build our own. 

### State Hooks: 

Example: a form component can use state to store input values in various fields.

Image gallery component can use state to store the selected image index. 

There are two state gooks that can be used: 
- `useState` a state variable that can be updated directly
- `useReducer` a state variable that has the update logic inside a `reducer function`

### Context Hooks

Lets a component ***receive information from distant parents without passing it as props.*** 

Example. the app's top level component can pass the current UI theme to all components below, no matter how deep. 

`useContext` reads and subscribes to a context. 

```jsx
function Button() {  
const theme = useContext(ThemeContext);  
// ...
```

### Ref Hooks

Hold information that isn's used for rendering like a DOM node or a timeout ID. Updating a ref does not re-render your component. 

Refs are an `escape hatch` from the React Paradigm, and are used when we want to work with `non-React` systems such as built-in browser APIs.

```jsx
function Form() {  
	const inputRef = useRef(null);
	// ....
```

### Effect Hooks

Lets a component `connect to and synchronize with external systems`. Includes, dealing with network, browser DOM, animation, widgets written using a different UI library and other non React code. 

Effects are also an `escape hatch` from React's paradigm. If we are not interacting with an external system, we might not need an effect. 

```jsx
function ChatRoom({ roomId }) {  
	useEffect(() => {  
		const connection = createConnection(roomId);  
		connection.connect();  
		return () => connection.disconnect();  
	}, [roomId]); 
	// ...
```

### Performance Hooks

A common way to optimize re-rendering performance is to skip unnecessary work. 

Here are two hooks you can use to optimize react's performance: 

- `useMemo` lets you cache the result of an expensive calculation
- `useCallback` lets you cache a function definition before passing it down to an optimized component 

### Defining your own hooks