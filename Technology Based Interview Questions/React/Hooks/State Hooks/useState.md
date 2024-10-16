Call at top level to declare a state variable.

Convention to name state variables:
- `[someting, setSomething] = useState(initialValueOfSomething)`

#### Caveat - Passing in functions as initializers to state

If we pass in a function as the initial state, React saves the output of the function call once and uses it on every re-render. 

Case 1: 
- `const [todos, setTodos] = useState(createInitialTodos());`

	In this case, `createInitialTodos` is called on every re-render. This is wasteful computation and a performance hit in case this is an expensive operation.

Case2: 
- `const [todos, setTodos] = useState(createInitialTodos);`
  
	Here the function is called once the first time and the initial value is returned on every other render
	
	It is important to keep it a pure function
	
	React calls it twice during development to ensure that there are no side effects for us to check if it is pure


Doesn't seem to satisfy the case, sandbox tests: 
- https://codesandbox.io/p/sandbox/pwmvjn
- https://codesandbox.io/p/sandbox/xdd656
- https://codesandbox.io/p/sandbox/8vvdmz

Here in the above tests, the component has to render a list of 50000 elements, and it is passed in as a initializer function to the useState hook. 

Irrespective of what method I use be it calling the function or just passing in the reference, it is slow to re render. But the behavior seems to be consistent with what is mentioned in the documentation.

In the below fork: https://codesandbox.io/p/sandbox/react-dev-forked-399dkd

We see that even though we have memoized the list rendering and also not calling the initializer function every time, the updates on the input field are executed slower than we would like for it to be. 

### Resetting state with a key

we encounter the key attribute while rendering items on a list. Key also serves another purpose. 

We can `reset a component's state by passing in a different key` !!

Example, suppose we have a form where users are typing in information.... and we need to include a feature to `reset` the form. We can just do this by attaching a `key` attribute to the `Form` component. And when we `update the key` attribute, the state of the Form get's reset.

```jsx
import { useState } from 'react';

export default function App() {
  const [version, setVersion] = useState(0);

  function handleReset() {
    setVersion(version + 1);
  }

  return (
    <>
      <button onClick={handleReset}>Reset</button>
      <Form key={version} />
    </>
  );
}
```

This has to do with how react uses the Virtual DOM to update the Original DOM.

When react recomputes the DOM, here we have provided a new Key for an element which now takes place of the old element. So since there is this difference, React Removes the old Form componenet from the DOM and Injects a new instance of the From Component, hence the state is reset.

If we add a console log in the `useEffect` we can capture this behavior.