Presentation delay is the time that starts from when the processing for a given event ends and till the time the visual change for that particular event is rendered on the UI.

This could be image loading on the screen, or when typing something in an input box or displaying a video or could be just rendering a page on the the screen on first load.

#### Minimize Dom Size

- Smaller doms mean lesser work during initial page load
- Smaller DOMs also mean lesser work while searching for the portion of the DOM to update whenever there is a change

#### Use `content-visibility` to lazily render off screen elements

