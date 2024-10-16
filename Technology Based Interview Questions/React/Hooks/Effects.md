Suppose we want to establish a connection to a char room server. This is not a pure calculation, it is a side effect, so it can't happen during Rendering. However there is no particular event like "click" that causes the connection to be established. It has to be established by default when the chat component loads.

> Effects let you specify side effects that are caused by rendering itself rather than by a particular event. *Effects run at the end of a commit after the screen updates.* This is a good time to synchronize the React components with some external system.

**Do not rush and stat using effects**: 
If your code only adjusts some state based on another state, you might not need an effect. 

Example use case: 

```jsx
function VideoPlayer({ src, isPlaying }) {
  const ref = useRef(null);

  if (isPlaying) {
    ref.current.play();  // Calling these while rendering isn't allowed.
  } else {
    ref.current.pause(); // Also, this crashes.
  }

  return <video ref={ref} src={src} loop playsInline />;
}
```
In this above component, we get the following error: 
` null is not an object (evaluating 'ref.current.pause') `

This is because we are trying to access the ref object during the rendering process. 

But since ref is only set after the commit, it will not work. 

Hence we need to move this into an effect that runs after rendering.
```jsx
function VideoPlayer({ src, isPlaying }) {  

	const ref = useRef(null);  
	
	// Moving actions on ref into an effect
	useEffect(() => {  
		if (isPlaying) {  
			ref.current.play();  
		} else {  
			ref.current.pause();  
		}  
	});  
	  
	return <video ref={ref} src={src} loop playsInline />;  
}
```

> In this example, the “external system” you synchronized to React state was the browser media API. You can use a similar approach to wrap legacy non-React code (like jQuery plugins) into declarative React components.

WARNING:

Effects run after every render, so setting state inside a useEffect hook call will lead to an infinite loop and a stack overflow error.

Effects should usually synchronize your components with an _external_ system. If there’s no external system and you only want to adjust some state based on other state, [you might not need an Effect.](https://react.dev/learn/you-might-not-need-an-effect)

### Adding dependencies to an effect

This Effect uses _both_ `ref` and `isPlaying`, but only `isPlaying` is declared as a dependency:

```jsx
function VideoPlayer({ src, isPlaying }){  
	const ref = useRef(null);  
	useEffect(() => {    
		if (isPlaying) {      
			ref.current.play();    
		} 
		else {      
			ref.current.pause();   
			}  
	}, [isPlaying]);
	...
```

This is because the `ref` object has a _stable identity:_ React guarantees [you’ll always get the same object](https://react.dev/reference/react/useRef#returns) from the same `useRef` call on every render. It never changes, so it will never by itself cause the Effect to re-run. Therefore, it does not matter whether you include it or not. Including it is fine too:

```jsx
function VideoPlayer({ src, isPlaying }) {  
	const ref = useRef(null);  
	useEffect(() => {    
		if (isPlaying) {      
			ref.current.play();    
		} else {      
			ref.current.pause();    
		}  
	}, [isPlaying, ref]);
	...
```

The [`set` functions](https://react.dev/reference/react/useState#setstate) returned by `useState` also have stable identity, so you will often see them omitted from the dependencies too. If the linter lets you omit a dependency without errors, it is safe to do.

Omitting always-stable dependencies only works when the linter can “see” that the object is stable. *For example, if `ref` was passed from a parent component, you would have to specify it in the dependency array.* 

However, this is good because you can’t know whether the parent component always passes the same ref, or passes one of several refs conditionally. So your Effect _would_ depend on which ref is passed.

### Effects run twice in Deployment

In Development Mode, react runs the code within the useEffect block twice. This is to highlight any bugs / issues that are present in the current code base. We must ensure to destroy any connections and perform cleanup actions for the component in the `Cleanup` part of an Effect.

```jsx
useEffect(() => {  
	const connection = createConnection();  
	connection.connect();  
	return () => {  
		connection.disconnect();  
	};  
}, []);
```

This way in Development mode, we can check if the expected behavior is displayed.

> The idea here is not to avoid this behavior but to correct our code to ensure that this behavior is present and we fix any issues that show up.

## Sometimes you don't need an effect

#### Updating state based on props and state

```jsx

const [firstName, setFirstName] = useState('Taylor');  
const [lastName, setLastName] = useState('Swift');

// 🔴 Avoid: redundant state and unnecessary Effect  
const [fullName, setFullName] = useState('');  

useEffect(() => {  
	setFullName(firstName + ' ' + lastName);  
}, [firstName, lastName]);
```

First this is not necessary, second this causes an infinite loop. Replace this with:

```jsx
const [firstName, setFirstName] = useState('Taylor');  
const [lastName, setLastName] = useState('Swift');  

// ✅ Good: calculated during rendering  
const fullName = firstName + ' ' + lastName;  
// ...
```

#### Caching expensive calculations - `useMemo`

```jsx
const [newTodo, setNewTodo] = useState('');  

// 🔴 Avoid: redundant state and unnecessary Effect  
const [visibleTodos, setVisibleTodos] = useState([]);  

useEffect(() => {  
	setVisibleTodos(getFilteredTodos(todos, filter));  
}, [todos, filter]);
```

Better approach: 
```jsx
const [newTodo, setNewTodo] = useState('');  

// ✅ This is fine if getFilteredTodos() is not slow.  
const visibleTodos = getFilteredTodos(todos, filter);  
// ...

```

Much Better - if  `getFilteredTodos` is a slow op:
```jsx
import {useMemo} from 'react';

const [newTodo, setNewTodo] = useState('');  

const visibleTodos = useMemo(() => {  
// ✅ Does not re-run unless todos or filter change  
return getFilteredTodos(todos, filter);  
}, [todos, filter]);

```

NOTE: `useMemo` only works for pure calculations.

\
