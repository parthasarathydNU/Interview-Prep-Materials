https://additionalsheet.com/interview-questions/tailwind-css-interview-questions

### What is Tailwind CSS ?
- Utility first CSS framework that provides low level utility classes to build designs directly in your markup
- Offers small, single purpose utility classes that can be combined to create complex designs

### How to include Tailwind CSS in a project ? 
- Install tailwind through npm or yarn
- Create a `tailwind.config.js` file and include generate CSS file in your HTML or use it with a build tool

### What is the purpose of `@apply` directive in TCSS ?
- The `@apply` directive is used in custom styles to apply utility classes defined in the Tailwind framework within a css file... we can think of that as a spread operator in js where we bring in syles from a different class  / variable and apply them into this class
- This can be translated to `@extend` in `sass`


### Utility first and component first CSS approach
- Utility first approach, focuses on creating fine grained classes for individual styles, while component based approach starts with individual UI components and defines classes for each

### Customize default configuration in tailwind
- We can modify the `tailwind.congif.js` file to add, remove, customize colors, spacing, fonts, themes and other styles


### Setting up tailwind with PurgeCSS and PostCSS
- Use tailwind init to create the tailwind configuration file `tailwind.config.js`.
- Tailwind needs PostCSS - this is a tool that uses JS based plugins to automate routine CSS operations
- Tailwind also uses `Autoprefixer` - this is a plugin that uses data based on current browser popularity and support to apply prefixes for our css style declarations

So we create a `postcss.config.js` file : 

```json
// postcss.config.json
module.exports = {
  plugins: [
   tailwindcss: {}, 
   autoprefixer: {},
  ]
}
```

Add paths to all of our template files in `tailwind.config.js` file: 
```js
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Along with tailwind, we install postcss and also autoprefixer for tailwind to work.

This is the base tailwind style sheet

```css
<!--- main.css ---->
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```json
"scripts": {
  "build:css": "postcss src/main.css -o static/dist/tailwind.css"
}
```

### Trimming file sizes: 

Now since we are going to be writing all classes within the template files, our css files become very small. So to further reduce css file size, we install cssnano and purgecss to minify the files: 
```
npm install cssnano
npm install @fullhuman/postcss-purgecss
```

PurgeCSS is a tool that is used for removing unused CSS in a project. It removes unused styles and optimizes CSS bundle sizes. 

This is how we can update `postcss.config.js` to include purgecss and cssnano

```js
const purgecss = require('@fullhuman/postcss-purgecss')
const cssnano = require('cssnano')
module.exports = {
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    cssnano({
      preset: 'default'
    }),
    purgecss({
      content: ['./layouts/**/*.html', './src/**/*.vue', './src/**/*.jsx'],
      defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || []
    })
  ]
}
```

### Variants in tailwind css
- The `variants` section of `tailwind.config.js` file is where we control which core utility plugins should have `responsive variants` and `pseudo class variants` generated.

```js
// tailwind.config.js 
module.exports = { 
	variants: { 
		appearance: ['responsive'], 
		// ... 
		borderColor: ['responsive', 'hover', 'focus'], 
		// ... 
		outline: ['responsive', 'focus'], 
		// ... 
		zIndex: ['responsive'], 
	}, 
}
```


Each property is a core plugin name pointing to an array of variants (there are a list of variants that are supported out of the box) to generate for the plugin

Example, for border color, we can have `responsive, hover, focus` , etc..

*Any variants that we specify will override the default variants for that plugin*. Therefore when overriding the default variants, make sure you always specify `all` the variants tat you'd like to enable, and not just the new ones you like to add.

Apart from manually specifying variants, we can append, insert and filter out variants from the default list of variants. 

`before`, `after` and `without` can mostly help us perform all the tasks that we need.

**Order of the variants is important**

Variants reference: https://v1.tailwindcss.com/docs/configuring-variants


### Responsive UI - Breakpoints in Tailwind

We can define the project's breakpoints in the `theme.screens` section of the `tailwind.config.js` file. By default the values are where the breakpoint should start. 

```js
// tailwind.config.js 
module.exports = { 
	theme: { 
		screens: { 
			'sm': '640px', 
			// => @media (min-width: 640px) { ... } 
			'md': '768px', 
			// => @media (min-width: 768px) { ... } 
			'lg': '1024px', // => @media (min-width: 1024px) { ... } 
			'xl': '1280px', // => @media (min-width: 1280px) { ... } 
		} 
	} 
}
```

We can also use device names instead of sizes: 
![[Screenshot 2024-07-09 at 7.07.22 PM.png]]

Tailwind is mobile first by default, so any style applied with `laptop:` will be enabled after the 1024px width mark.

#### However if we want to work with max width breakpoints, instead of min width, we can specify that under the themes key of tailwind config

![[Screenshot 2024-07-09 at 7.11.55 PM.png]]