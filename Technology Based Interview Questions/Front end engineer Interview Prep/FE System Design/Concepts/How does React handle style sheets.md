### Stylesheets and component lifecycle

When using CSS modules or scoped CSS in React components, the stylesheets are not typically downloaded and discarded as the components mount and unmount: 
- Stylesheets are bundled with the javascript during the build process
- When the bundle is loaded, all CSS is typically loaded at once, regardless of which components are initially rendered
- CSS remains in the DOM even if the components are unmounted

However if we are using CSS-in-JS solutions like styled-components, the styles are indeed added and removed from the DOM as components mount and unmount.

### Multiple Stylesheets with Same ClassNames: 

This depends on how we are managing CSS: 

a. Global CSS: 

- If multiple stylesheets define the same class name, the last loaded stylesheet's definition will take precedence as per CSS cascade

b. CSS Modules: 
- CSS Modules solve this problem by automatically generating unique class names
- Even if we use same class name in multiple components, the build process will generate unique names avoiding conflicts

c. CSS-in-JS like styled-components: 
- These solutions scope styles to components, avoiding global namespace conflicts

d. Block Element Modifiers: 
- Block Element Modifier is a naming convention for CSS that can improve the maintainability of large-scale applications. 

Here for every class name we follow a structure and hierarchy: 

- Block: `.block`
- Element: `.block__element`
- Modifier: `.block--modifier` or `.block__element--modifier`

Example: 
```css
.card {}
.card__title {}
.card__image {}
.card--featured {}
.card__title--large {}
```

So here instead of just saying `title` we are very specific in mentioning that it is a title within the card component. 

This falls in line with React's compoonent composition strategy, and we can manage classes better by prefixing the with the component name, so we avoid conflict in classes across components. 

However while this can be effective, this needs team buy-on and consistent usage. Developers must ensure that they use these very specific class names within their components, if not this only becomes another unused CSS class. 

### CSS Modules

CSS Modules are CSS Files in which all class names and animation names are scoped locally by default. 

They provide a way to use CSS with a scope limited to a single component, avoiding namespace collisions and making styles more maintainable. 

#### Key Features: 
1. Local Scoping: Class names are made unique automatically; so they don't conflict with other styles
2. Explicit Dependencies: We import styles directly into JS modules
3. No more global scope: Styles are by default local, reducing global style conflicts
4. Reusability: We can compose styles and create new class names by creating existing ones. 

This is a good system: 

Naming Convention: `Component.module.css`.

```css
// Button.module.css
.button {
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
}

.buttonLarge {
  font-size: 18px;
  padding: 15px 25px;
}
```

Here in the react component, we can provide various variants of the button based on the size prop.

```jsx
import React from 'react';
import styles from './Button.module.css';

function Button({ children, size }) {
  return (
    <button 
      className={
      `${styles.button} ${size === 'large' ? styles.buttonLarge : ''}`
      }
    >
      {children}
    </button>
  );
}

export default Button;
```

- When we import `styles` as an object from the css file
- Class names are accessed as properties of this object `styles.button`
- The actual class names in the DOM will be unique, preventing conflicts
- We can compose and customize classes during run time using template literaly or classnames libraries for conditional classes

### Why the module keyword ?

- Regular CSS files have global scope, while modules are locally scoped
- Regular CSS files add styles to the global scope
- With regular css files, we can use the class names directly, with CSS Modules, we access class names as properties of the imported styles object

Build Process: 
- The build process treats `.module.css` files differently from regular `.css` files. 
- For `.module.css` files, it generates unique class names and provides them as an object when imported
- Regular `.css` files are bundled and injected into the DOM as is.