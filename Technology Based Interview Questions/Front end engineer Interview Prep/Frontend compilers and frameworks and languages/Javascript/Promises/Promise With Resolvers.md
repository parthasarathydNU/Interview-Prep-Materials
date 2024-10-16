This helps us resolve or reject a promise based on an external action..

Let's say we have 4 elements in the dom

```js
const btnReview = document.querySelector('#btnReview');
const btnApprove = document.querySelector('#btnApprove');
const btnReject = document.querySelector('#btnReject');
const dialog = document.querySelector('dialog');
```

One button to open the review dialog, and two other buttons to either resolve or reject the form.

```js
const { promise, resolve, reject } = Promise.withResolvers();
```

Here we create a promise with resolvers.

And we associate these resolvers to the event listeners of these buttons
```js
btnReview.addEventListener('click', () => dialog.show());

btnApprove.addEventListener('click', resolve);
btnReject.addEventListener('click', reject);
```

Since the resolve and reject function was created before, it is associated with the resolve and reject of that promise. 

So when we click on the respective buttons, these get triggered accordingly. 

```js
promise
  .then(() => (message.innerHTML = 'You approved it.'))
  .catch(() => (message.innerHTML = 'You rejected it.'))
  .finally(() => {
    message.hidden = false;
    dialog.close();
    btnReview.remove();
  });
```

So here rather than waiting for some api call, we wait for interaction on the dom.
