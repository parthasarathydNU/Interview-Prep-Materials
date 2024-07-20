Here we learn techniques that let our application step out of react and access external systems. Most of our rendering logic and data flow should not rely on these techniques.

### Refs:

> Regular variables like `let timeoutID` don’t “survive” between re-renders because every render runs your component (and initializes its variables) from scratch. Should you keep the timeout ID somewhere else?

When we want our component to remember some information but don't want that information to trigger re-renders, we can use `refs`

Like state, refs are retained by React between re-renders. However, setting state re-renders a component. Changing a ref does not! 

You can access the current value of that ref through the `ref.current` property.

`useRef` returns an object that looks like this: 
```
{  
	current: 0 // The value you passed to useRef  
}
```

Refs are like a secret pocket that holds some information, that is stored outside React's rendering logic.

![[Pasted image 20240709002600.png]]

### Using Refs to store references to Dom elements, outside react's rendering scope

Hooks must be called at the top level of your component: You can't call `useRef` inside a function.

By requiring hooks to be called at the top level of function components and custom hooks, React ensures a consistent and predictable order of hook calls. This consistency is crucial for maintaining correct state management and avoiding bugs that can arise from conditional or nested hook calls. Following these rules helps ensure that your components behave as expected and are easier to understand and debug.

### Using RefCall Backs

Sometimes when we need to access a node within a list that is mapped over in React, we will need to save the ref's of all these nodes in an array outside the rendering logic of the list. 

Examples:
```jsx

<ul>  
	{items.map((item) => {  
		// Doesn't work!  
		const ref = useRef(null);  
		return <li ref={ref} />;  
	})}  
</ul>
```

The above example does not work as the ref is defined inside the loop, also we cannot call hooks within a loop. it has to be called at the top level.

```jsx
  {catList.map((cat) => (
	<li
	  key={cat}
	  ref={(node) => {         // <-- Example of Ref Call Back
		const map = getMap();
		if (node) {
		  map.set(cat, node);
		} else {
		  map.delete(cat);
		}
	  }}
>
	  <img src={cat} />
	</li>
  ))}

```

In the above example, we notice that rather than creating a ref within the loop, we try to create and store these refs outside the render function of the component.

The `refCallback` here returns the reference to the current node in the `node` variable.

### Accessing another component's DOM nodes

If you try to put a ref on **your own** component, like `<MyInput />`, by default you will get `null`

`Warning: Function components cannot be given refs. Attempts to access this ref will fail. Did you mean to use React.forwardRef()?`

> This is intentional. Refs are an escape hatch that should be used sparingly. Manually manipulating* another component’s DOM nodes makes your code even more fragile.

**Components that  *want* to expose their DOM nodes, have to opt in to that behavior**

A component can specify that it "forwards" its ref to one of its children.

```jsx
const MyInput = forwardRef((props, ref) => {  
	return <input {...props} ref={ref} />;  
});
```

Here we see that the `MyInput` component takes in the provided ref as part of the props and uses it to provide reference to the `input` DOM element.

### Controlling what functionalities are exposed through the ref by the component: 

```jsx
const MyInput = forwardRef((props, ref) => {
  const realInputRef = useRef(null);
  useImperativeHandle(ref, () => ({ 
   
	  // <- This hook controls what functionality to expose for the given out through the ref
	  
     // Only expose focus and nothing else
    focus() {   
    
    // <-- Define a custom method to expose , this wraps around the exposed ref
    
      realInputRef.current.focus();
    },
  }));
  return <input {...props} ref={realInputRef} />;
});
```

Usage

```jsx
  ...
  const inputRef = useRef(null);

  function handleClick() {
    inputRef.current.focus();  // <-- No other functions exposed apart for focus
  }
  ...
  <MyInput ref={inputRef} />
  <button onClick={handleClick}>
	Focus the input
  </button>
```

> The current value of the ref is only set after the render. Refs are not to be accessed / modified during rendering. 

### Performing State Updates Synchronously

Since refs are only updated after the render cycle, sometimes in situation likes the ones mentioned here, the ref still contains reference to the previous state of the element in the DOM as it was before the state update. 

```jsx
  function handleAdd() {
    const newTodo = { id: nextId++, text: text };
    setText('');
    setTodos([ ...todos, newTodo]);    // Update task list
    listRef.current.lastChild.scrollIntoView({
      behavior: 'smooth',
      block: 'nearest'
    });
  }
```

In the above function, we have a todo list, and whenever a new todo task is added, the todos list is updated using the setTodos and since the `listRef` points to the DOM list, we expect it to scroll to the last newly added element. 

However since `setState` is an async operation, it only scrolls to the previous element that was considered the last. Here is the fix: 

```jsx
  import { flushSync } from 'react-dom';
  
  function handleAdd() {
    const newTodo = { id: nextId++, text: text };
    
	// Using flushSync from react-dom
	// This ensures the state update happens in sync
    flushSync(() => {
      setText('');
      setTodos([ ...todos, newTodo]);      
    });

	// Since state updated happened in sync, 
	// now the ref contains to the updated DOM state
    listRef.current.lastChild.scrollIntoView({
      behavior: 'smooth',
      block: 'nearest'
    });
  }
```

