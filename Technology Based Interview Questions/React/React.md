### Features of react
- Extensions for complete application architecture support
- JSX used to describe what UI should look like
- Component is a function that returns HTML
- Speedy performance - Only the changed components are updated
- One way data binding keeps everything modular 
- Virtual DOM - a light weight representation of Real DOM

JSX - extension used for react - extension to JS programming language

Enables use to write HTML code within the same file where we write Java Script code- this let's us bring UI code closer to where we write business logic - makes code modular 

#### Can JSX be directly read by the web browser ?

Browsers are only built to read regular JS objects. React uses Babel internally to convert JSX code to JavaScript code so that it can run on the browser.

### What is the Virtual DOM ?

- React maintains a light weight in-memory representation of the structure of the page ( Inverted tree structure ) - this and the actual DOM are kept in Sync with each other
- Changes to state or props of a component lead to creation of a new virtual DOM tree, which is compared to the previous one
- The diffs are computed and only the necessary changes are batched and applied to the actual DOM
- Reconciliation process - ensures only parts of the DOM that need updates are changed - minimizes performance impact of updates
- Updates are batched and applied in one go , thia

### What are synthetic events in React ?
- A synthetic event is an object which acts as a cross-browser wrapper around the browser's native event
- It combines the behavior of different browser's native event into one API and this makes sure that the events are consistent across different browsers

### What are forms in react ?
- Users can interact with application and enter information when needed

### How does server side rendering work in react ?

1. Initial Render on Server - React renders the components to a string HTML on the server
2. Sends the fully rendered HTML to the client along with the JS bundle to run the react app <-- Is this sent for every Server Side Rendered component ?
3. Browsers receives and displays the HTML immediately providing a fully rendered page that users can see and good for SEO
4. **Hydration** : Browser downloads and executes the React JS bundle that contains client-side code for the react app ( business logic ): During hydration, react attaches event listeners to the HTML markup and prepares components for interactivity. 
5. Virtual DOM is also created in this process which will then serve as baseline for subsequent renders

Hydration binds the event listeners and other objects to the server side rendered component after the HTML is displayed so that the component is now ready for user interactivity

### React component lifecycle

[![React Lifecycle Methods](https://dotnettrickscloud.blob.core.windows.net/article/react/3720230920232432.webp)

### Redux 
- Open source Javascript library used to manage application state
- Store: Holds state of the application
- Actions are sent to the store
- Reducer is the function that reacts to the action and updates the Store which then triggers update to the state of the various components that are subscribed to the store

### React Router
- Package used to implement routing in a react application
- Used to develop single page web applications by allowing multiple views in a single app by defining multiple routes in the React app

How React Routing Differs from Conventional Routing: 
- Single HTML Page
- Navigates multiple views in the same file
- Page does not refresh since it is a single file
- Improved performance

### Pure components in React: 

#### Side Effects: (Un) intended consequences

React's rendering process must always be pure: Components should only return their JSX and not change an objects or variables that existed before rendering - that makes them impure.

React offers a "Strict Mode" in which it calls each component's function twice during development. This way it helps find components that break these rules. StrictMode has no effect in production, it won't slow down the app for users.


### Side Effects In React:

Features like updating the screen, api calls, changing animation, changing data are all called side effects - as these don't happen during rendering. 

Event handlers don't need to be pure: Side effects usually belong inside event handlers - functions that react runs when we perform some action. Even though they are defined within the component, they don't run during the rendering process. 

When we have exhausted all options and can't find the right event handler for the side effect, we can still attach it to the returned JSX with a `useEFfect` call in our component. This tells React to execute it later, after rendering, when side effects are allowed. However this approach should be our last resort. 

As much as possible try to express component logic with rendering alone.

### Controlled an Uncontrolled Components: 

A component is said to be "controlled" when important information in it is driven by props rather than it's own local state. This let's the parent component fully specify it's behavior. 

"Uncontrolled" components are easier to use within their parents because they require less configuration. But they are less flexible when we have to co-ordinate them together. "Controlled" components are fully flexible but require the parent component to fully configure them with props. 

In practice it is up to the developer to decide which information should be controlled via props and which should be controlled via the state.

### Preserving and Resetting State

#### Same component at the same position preserves state

```jsx
	  <div id="uniqueDiv" >
      {isFancy ? (
        <Counter isFancy={true} /> 
      ) : (
        <Counter isFancy={false} /> 
      )}
      </div>
```

Here we notice that we have two instances of the Counter Component that replace one another based on the `isFancy` label. 

According to React, since the component is the same `Counter` and it is rendered in the same position in the DOM tree `#uniqueDiv`  these components will share the same state. So when we flip the isFancy flag to true and false, it will be equivalent to the below snippet: 

The internal state stays the same 

```js
	  <div id="uniqueDiv" >
	      <Counter isFancy={isFancy} />
      </div>
```


![[Screenshot 2024-07-08 at 4.05.25 PM.png]]

> Remember that **it’s the position in the UI tree—not in the JSX markup—that matters to React**

React doesn’t know where you place the conditions in your function. All it “sees” is the tree you return.

> As a rule of thumb, **if you want to preserve the state between re-renders, the structure of your tree needs to “match up”** from one render to another. If the structure is different, the state gets destroyed because React destroys state when it removes a component from the tree.


However, adding a key to the component, causes it to act as completely new components in the same position, so that state does not get shared 

```
{isPlayerA ? (  

<Counter key="Taylor" person="Taylor" />  

) : (  

<Counter key="Sarah" person="Sarah" />  

)}
```

### This is a really interesting example that demonstrates a very nuanced use of the key attribute in react: 

https://react.dev/learn/preserving-and-resetting-state#challenges


### Reducer in react

Managing state with reducers is slightly different from directly setting state. Instead of telling React "what to do" by setting state, we specify "what the user just did" by dispatching "actions" from event handlers. 

The action that is dispatched can be of any type, usually it has information that describes "what_happened" and other information to help update the state based on the action triggered by the user. 

The reducer file can work independently of the initial state, it is a pure function that does not know the state. 

We can draw similarities between the useState and the useReducer hook

const [variableName, setVariableName] = useState(initialState)

const [variableName, dispatch]                = useReducer(reducer, initialState);

Reducer takes in the current state, and returns and immutable version of the next state to the `variableName` that can be used within the component.

### Hooks:

Your function is considered a custom Hook if its name starts with `use`. This lets you use other Hooks, like `useContext`, inside it.