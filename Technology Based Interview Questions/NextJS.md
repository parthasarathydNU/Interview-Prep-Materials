Questions:
- How does next js perform SEO optimization and performance tuning?
- What is vercel ? What are all it's capabilities ?
- Can we use `getServerSideProps` and `getStaticProps` together in one file ? What will be the behavior in that case ?
- How are assets optimized and cached in next js for content present in the public directory ?

https://www.coding-ninja.com/interview-questions/nextjs

#### **Why use NextJS over traditional React ?**

Enhances react by adding features like server-side rendering (SSR), static site generation (SSG) and routing. It simplifies complex tasks such as SEO optimization. Leads to faster load times, and improved developer experience

#### **Explain SSR and it's benefits** :

React components are rendered on the server side instead of the client. This results in fully formed HTML pages sent to the client enhancing page load times and SEO ?? how ?? 

*Quicker initial page loads and better performance for users with slower devices or network connections.* 

#### **What is client side rendering ?  And when to use it ?**

Web browser handles rendering by executing JS code after receiving HTML page. It is chosen for parts where real time data updates are crucial. Ideal for interactive elements like dashboards or chat applications where benefits of SSR or SSG might not be as prominent. 

#### Differentiate SSR and SSG in NextJS

Static site generation is for generating HTML pages during build time and serves them as static files. 

SSR conversely generates HTML dynamically with each request offering ability to provide dynamic content. SSG is chosen for content heavy pages with infrequent updates. 

SSR is suitable for pages with personalized content like user profiles and stuff like that.

#### Purpose of pages dir

Pages is where we define the routes and pages of the application. Each file inside pages represents a route. 
- `pages.index.js` corresponds to the root route ( '/' )
- `pages/about/index.js` or `pages/about.js` represents the route ( '/about' )

We can either use a directory and an index file or directly mention the file name for the route. 

```
- pages
  - index.js (Maps to '/')
  - about.js (Maps to '/about')
  - contact.js (Maps to '/contact')
```

#### How to create a custom 404 error page in Next.js ? 

We create  a file called `pages/404.js`. This is directly considered as the error page if the requested page is not found.

#### Difference between getServerSideProps and getStaticProps: 

`getServerSideProps`:
- This is used for server side rendering (SSR)
- Runs on every request to the page - data is fetched every time the page is rendered on the server for each request
- Suitable for pages where data cannot be determined at build time
- Slower than getStaticProps because it involves server-side rendering for each request which can impact performance
- User Specific pages, pages with real-time data ...

`getStaticProps`:
- Used for static site generation
- Runs on build time and fetches data to pre-render files as static html files
- Generated HTML can be cached and served from a CDN which makes the site faster and scalable. 

#### How to implement dynamic routing in next js ?

- We can use a slug which is basically `[unqueId]` a pair of square brackets to pass in an id or any unique identifier. 
- Within the component, we can use the useRouter from `next/router`. 
- And the uniqueId will be available as a key in the `router.query` parameter. We can access this in the top level within the component function.

#### What is the purpose of the public directory in Next.js ?

Location for static assets that you want to serve publicly such as images, fonts, or any other files that *don't need to go through the build process.* 

They can be referenced within the application using a special path `/`. Example if we have an image named `logo.png` in the public dir, we can use it in our components as follows: 

`<img src='/logo.png' alt='Logo' />`

These assets are optimized and cached by Next.js for improved performance.

#### Explain the concept of API routes in Next.js ?

Allow us to create serverless functions to handle API requests. These routes are defined int he pages/api directory and are automatically served as serverless functions when deployed. 

Example: we can create `pages/api/users.js` to handle user related API requests. 

API routes are useful for separating API logic from frontend code and can be used for tasks like fetching data from db, handling form submissions or serving JSON data to your application. 

https://rc.nextjs.org/docs/app/building-your-application/data-fetching/caching-and-revalidating#caching

##### Benefits of using API routes in Next.JS: 

- **Optimization**: Next.js optimizes and caches API routes for better performance.
- Separation of concerns 

#### What is the purpose of the `_app.js` file

The `_app.js` file in Next.js is a crucial component used to control the layout, styling and behavior shared across all pages of a Next.js application. 

It allows us to maintain consistency by defining global elements for the layout. 
Additionally we can perform 
- data fetching and 
- setting up of global context or 
- state management within this file

#### Compare `getServerSideProps`, `getStaticProps` and `getInitialProps` for data fetching

getServerSideProps : 
- runs on every render on the server side, where data is fetched dynamically and passed into the component as props

getStaticProps: 
- Runs at build time
- Used for fetching data that can be pre rendering and shared among multiple requests
- Returns data to the component as props


#### How can you implement client side routing in Next.js ?

Using `Link` component form the  `next/Link` library.

#### How to optimize Images in NextJS ?

Use the `Image` component from `next/Image`

#### What are dynamic imports in Next JS ?

Dynamic imports in Next.js allow you to load modules or components only when they are needed which can help reduce initial page load times. 

We should use Dynamic imports when we have components that are not necessary for the initial page load, but should be loaded lazily when a user interacts with a part of the page or route.

```
const DynamicComponent = dynamic(() => import('../components/DynamicComponent'));
```


#### Describe the purpose of getStaticPaths function in next.js

When working with dynamic routes , getStaticPaths can be used to specify the possible values for dynamic segments in the URL. 

It is often used with `getStaticProps` to generate static pages for each dynamic route.

```javascript
export async function getStaticPaths() {
  const paths = await fetchDynamicPaths(); // Fetch dynamic paths from your data source
  return {
    paths,
    fallback: false // or true for incremental static regeneration
  };
}

export async function getStaticProps({ params }) {
  const data = await fetchDataForParam(params.id);
  return {
    props: { data }
  };
}
```

In the above example, `getStaticPaths` generates a list of possible dynamic paths. An getStaticProps fetches data for each dynamic path. This allows nextJS to pre-render each pages for all possible dynamic paths. 

## PERFORMANCE OPTIMIZATON


#### What are some strategies to improve performance of a Next.js application

1. Server side rendering for critical content
2. Client side routing using the next/link component
3. Optimize images with the next/image component
4. Use lazy loading for components that are not immediately required
5. Implement caching for SSR data
6. Minimize and optimize JS and CSS bundles
7. Use the `getStaticProps` and `getServerSideProps` efficiently
8. Enable incremental static regeneration for dynamic content
9. Implement code splitting for optimized loading


