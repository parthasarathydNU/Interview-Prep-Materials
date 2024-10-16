```js
function download(url, callback) {
    setTimeout(() => {
        // script to download the picture here
        console.log(`Downloading ${url} ...`);
        
        // process the picture once it is completed
        callback(url);
    }, 1000);
}

function process(picture) {
    console.log(`Processing ${picture}`);
}

let url = 'https://wwww.javascripttutorial.net/pic.jpg';
download(url, process);
```

In the above example, we have two functions, download and process. 
We pass the `process` function as an argument when calling the `download` function.

Inside the `download` function, the `process` function is associated with the `callback` variable in the outer scope of the function inside `setTimeout`

And when the `anonymous function` fires from the event loop, it completes the download and calls the `process` function with the `url` parameter. 

### Handling errors

```js
function download(url, success, failure) {
  setTimeout(() => {
    console.log(`Downloading the picture from ${url} ...`);
    !url ? failure(url) : success(url);
  }, 1000);
}

download(
  '',
  (url) => console.log(`Processing the picture ${url}`),
  (url) => console.log(`The '${url}' is not valid`)
);

```

In real life, things are rarely straightforwards, the download might fail, the url might be invalid. 

So we pass in 2 callbacks, one to call in case of success, another in case of failure. 

How can we handle this when we want to download a 1000 pictures in sequence ? 

```js
function download(url, callback) {
  setTimeout(() => {
    console.log(`Downloading ${url} ...`);
    callback(url);
  }, 1000);
}

const url1 = 'https://www.javascripttutorial.net/pic1.jpg';
const url2 = 'https://www.javascripttutorial.net/pic2.jpg';
const url3 = 'https://www.javascripttutorial.net/pic3.jpg';

download(url1, function (url) {
  console.log(`Processing ${url}`);
  download(url2, function (url) {
    console.log(`Processing ${url}`);
    download(url3, function (url) {
      console.log(`Processing ${url}`);
    });
  });
});

```

Callback hell

```js
asyncFunction(function(){
    asyncFunction(function(){
        asyncFunction(function(){
            asyncFunction(function(){
                asyncFunction(function(){
                    ....
                });
            });
        });
    });
});
```

We use async await and promises here. 

