JSX Stands for JavaScript XML. Which is a syntactic extension for Javascript that let's you use HTML tags inside the JS file. So using this, instead of creating, configuring and appending HTML tags through JS Objects, we can create elements using XML like syntax that will generate DOM elements for us behind the scenes.

### Expressions can be evaluated in JSX.

`const expression = <code>{a} + {b} = {a + b}</code>`

Functions can be called inside `{}` which can return HTML like elements that can be rendered. 

```js
const menu = <ul>
    {menu.map(item => {
        return <li>
            <a href={item.link}>{item.name}</a>
        </li>
    })}
</ul>;
```

Ternary operators and boolean logic can be evaluated inside JSX expressions. 

### Attributes in JSX

We can use HTML attributes in JSX elements, we can also use expressions to pass in variables for these attributes. 

`<a href={item.link} target="_blank">{item.name}</a>`

Camel case is used to denote attributes that are hyphenated. 

```js
{/* Invalid */}
<div aria-label="Label"></div>
<div aria-checked="true"></div>
<div tab-index="0"></div>

{/* Valid */}
<div ariaLabel="Label"></div>
<div ariaChecked="true"></div>
<div tabIndex="0"></div>
```

### Functions and Props

JSX elements can be stored in variables and can be passed around to be used in other JSX elements. 

In React, a major pattern is grouping JSX elements together as functions. Capitalize the function name else it will be treated as a HTML element. 

Like we have 'attributes' for HTML elements, we have '`props`' for JSX functions  or components as we call in react. 

```jsx
const Slider = ({ size }) => (
    <div className={size}>The HTML layout for the slider</div>
);

<Slider size="large" />
<Slider size="medium" />
<Slider size="small" />
```
### What JSX is Generated into ? 

React needs to compile it down to JS function calls that the browser can understand. These function calls witll create and update the necessary HTML elements at the end. 

```jsx
const jsx = <div>Welcome to React</div>;

{/* This will be generated into: */}
React.createElement('div', null, 'Welcome to React');

{/* Using attributes: */}
const jsx = <div className="carousel" />;

React.createElement('div', {className: 'carousel'});
```

If a JSX element has children elements, those will also be compiled down to `React.createElement` calls, therefore in the final JS bundle, we will always see the following blueprint. 

`React.createElement(component, props, ...children);`

### JSX Prevents Injection Attacks

It is safe to embed used input in JSX: 

```jsx
const title = response.potentiallyMaliciousInput;
// This is safe:
const element = <h1>{title}</h1>;
```

By default, React DOM `escapes` any values embedded in JSX before rendering them.

Thus it ensures that you can neve inject anything that is not explicitly written in your application. Everything is converted to a string before being rendered. This helps prevent XSS attacks. 