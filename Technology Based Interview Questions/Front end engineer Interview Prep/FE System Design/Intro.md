https://www.greatfrontend.com/system-design/types-of-questions?utm_source=frontendinterviewhandbook&utm_medium=referral&gnrs=frontendinterviewhandbook

### Types of Front End System Design Questions

### Applications

Designing applications for frontend system design interviews will feel similar to general Software Engg. Sys design interviews. However, instead of talking about distributed systems, you should focus on the client side of things and `talk about app architecture and client side implementation details. 

`Firstly, design the high-level architecture`, identify the components in the system, `and the API between the components`. Then dive into a few areas that are interesting to the problem and `how to implement or optimize them`. 

- High level architecture
- Identify components in the system
- API between the components
- Optimization considerations

> High level architecture --> API --> Optimize
> 
> *Looks a lot like distributed system design innit ?* 

###  UI Components

First start by determining the sub components of the component (e.g. for an image carousel, we have the image, the pagination buttons, thumbnails), define the external facing API of the component ( what options / props the component should accept ), describe the internal component state, API between the sub components ( if relevant ) , then dive into optimizations and considerations for performance, accessibility, user experience, security etc.. where relevant. 

- List sub components
- define the external facing API of the component
- Define internal component state
- API between sub components 
- List down considerations
	- performance
	- accessibility
	- user experience
	- security
	- etc..

### Customizing Theming

You will most certainly be expected to design a way for users of the component to customize the component appearance. 

#### Class Injection

This is something that shadcn-ui uses. Components accepts a prop / option to allow the developer to provide their own classes and these classes are added to the DOM elements. 

This approach is not very robust because if the component also adds its own styling via classes, there could be conflicting properties within the component's classes and developer provided classes. 

```jsx
import clsx from 'clsx';

function Slider({ className, value }) {
  return (
    <div className={clsx('gfe-slider', className)}>
      <input type="range" value={value} />
    </div>
  );
}

<Slider className="my-custom-slider" value={50} />;
```

#### Non-deterministic styling

Class injection has an unobvious downside. The final visual result is non-deterministic and may be not what is expected. In the above provided example, if the `gfe-slider` class already had a color attribute and the developer passes a class that has a color attribute, the winning style is the class that appears later on the HTML page. If the loading order of the stylesheet is not guaranteed ( if stylesheets are lazily loaded) the visual ressult will not be deterministic. Here is where developers needs to add `!important` to their styles to override this ambiguity.
### jQuery

In jQuery, classes can be passed as field on the options. 

```js
$('#gfe-slider').slider({
  classes: {
    'ui-slider': 'highlight',
    'ui-slider-handle': 'ui-corner-all',
    'ui-slider-range': 'ui-corner-all ui-widget-header',
  },
});
```

All of jQuery's UI component initializers take in the `classes` field to allow adding additional classes to individual elements. 

### CSS Selector Hooks

If we read the source code of the component and define the custom styles using the same classes, we can achieve complete customization, but this is dangerous as relying on a component's internals and there's no guarantee that the class names won't change in future. 

If a UI library author can make these classes/attributes part of their API, which comes with the guarantees: 
1. The list of selectors is published for external reference
2. Published selector's won't change without a breaking change and version bump

Then it is acceptable practice and developers can "hook" into them by using these selectors in their style sheets. 

Material UI used to have this approach where they would list out the class names to use to style various components. I found that a bit cumbersome to maintain.

Pros: This approach saves developers the hassle of passing in classes into the component, as they only have to write css to customize the styling. 

### Theme Object

Instead of taking in classes, the component takes an object of key/values for styling. This is useful if there is only a strict subset of properties to customize