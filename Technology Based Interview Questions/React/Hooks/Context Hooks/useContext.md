Lets you read and subscribe to `context` from your component.

```jsx
const value = useContext(SomeContext)
```

Call `useContext` at the top level of your component to read and subscribe to `context`.

`useContexxt` returns the context value for the calling component. It is determined as the `value` passed to the closest `Context.Provider` above the calling component in the tree.

The returned value is always up-to-date. React automatically re-renders components that read some context if it changes!!!

This is a great segway to use the Context API in conjunction with the useReducer hook to lift state up the component hierarchy.

### Ways to use context

Context is only always accessible to components that are in the sub tree under the current component where the context.provider is called.

Example: 

```jsx
function MyPage() {  

const [theme, setTheme] = useState('dark');  
	return (  
		<ThemeContext.Provider value={theme}>  
			<Form />  
			<Button onClick={() => {  
				setTheme('light');  
			}}>  
			Switch to light theme  
			</Button>  
		</ThemeContext.Provider>  
	);  
}
```

In the above example, the theme value can only be read inside the `Button` and the `Form` Components.

The button can read this value like shown here

```jsx
function Button({ children }) {
  const theme = useContext(ThemeContext);
  const className = 'button-' + theme;
  return (
    <button className={className}>
      {children}
    </button>
  );
}
```

And since we also have an onClick listener on the`Button`, this updates the value passed through the context and triggers a re render in the Button.

