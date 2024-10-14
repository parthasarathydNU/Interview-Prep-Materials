https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

This term has widened to include injection of basically any content. XSS Attacks are serious and can lead to account impersonation, observing user behavior, loading external content , stealing sensitive data and more. 

### Framework Security

Modern web frameworks have a fewer XSS bugs, and help mitigate XSS by using templating and auto escaping. However improper use of frameworks can lead to security issues. 

#### InnerHTML

The innerHTML gets or sets the HTML or XML markup contained within the element. 

More precisely the `innerHTML` gets a serialization of the nested child DOM elements within the element or sets HTML or XML that should be parsed to replace the DOM tree within the element.

`dangerouslySetInnerHTML` is React's replacement for using `innerHTML` in the browser DOM. 

So the way to do it in React is by explicitly creating an object with an `__html` key.

```jsx
function createMarkup() {
  return {__html: 'First &middot; Second'};
}

function MyComponent() {
  return <div dangerouslySetInnerHTML={createMarkup()} />;
}
```

There will be times where you need to do something outside the protection provided by the framework which means that output encoding and HTML Sanitization can be crucial.

### XSS Defense Philosophy

In order for an XSS to be successful, an attacker must be able to insert and execute malicious content in a webpage. 

Thus all variables need to be protected and go through a validation and then sanitized before being rendered on the DOM.

### Output Encoding

When we need to safely display data exactly as a user types it in, output encoding is recommended. Variables should be interpreted as text instead of code.

```
<div> <script>alert`1`</script> </div> // Example Attack
```

If we are using JavaScript for writing to HTML, look at the `.textContent` attribute. This is a `Safe Sink` and will automatically HTML Entity Encode.

```js
a.innerText = "<script>alert`1`</script> "

Output: 
'\x3Cscript>alert`1`\x3C/script> '
```

Here we see that the brackets are escaped / output encoded. But on the UI we see the content printed in the proper way.

![[Screenshot 2024-10-13 at 8.43.00 PM.png]]

However the below one injects a dom element with the onClick event handler. 

```js
a.innerHTML = "<div onclick=alert(1) >Hello</div>"
```


Read More .... 

https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html


