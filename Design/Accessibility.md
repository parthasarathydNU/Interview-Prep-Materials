Accessibility markup is an integral part of creating documentation for design specs. 

Use standard platform controls and semantic HTML. Apps automatically control the markup and code needed to work well with a platform's assistive technology. 

#### Color contrast

Color contrast can help users see and interpret the app's content, interact with right elements and understand user actions. 

##### Contrast Ratios

Contrast ratios represent how different one color is from another, commonly written as 1:1 or 21:1. The greater the difference between the greater the difference in relative luminance between the colors. 

Recommended Contrast Ratios: 
- Last text and graphics: 3: 1 against the background
- Small text: 4.5 : 1 against the background

Disabled states do not need to meet contrast requirements.
### Hierarchy

To emphasize which information is important, multiple visual and textual cues like color, shape, text and motion add clarity.  

Visual feedback ( labels, colors and icons ) and touch feedback show users what's available in the UI. 

#### Visual Hierarchy

To enable the screen reader to read out content in the intended order, it's important for designers to collaborate with developers - both for writing out the HTML in the correct order and understanding how screen readers will interpret designs. 

While CSS determines the layout and appearance of the page, screen readers, rely on the top-down structure of HTML on any platform. This structure creates a map for the screen reader to follow when reading the content. 

#### Web Landmarks and Headings

There are eight landmark roles: navigation, search, main, banner, complementary, content info, region

#### Accessibility Labels: 

Clear and specific labels to any landmark roles that appear multiple times. This helps users differentiate information. Do not repeat the landmark role within a label. 

![Diagram labeling two regions with a navigation role with the labels primary and pagination.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fl6qwm47l-a11y-accessibility-labels.png?alt=media&token=d89d19c7-e1d3-4188-acbb-9822f95a5e35)

#### Define headings: 

Assistive technology users often navigate web pages with the help of headings. They create a clear hierarchy to help users navigate and take action. 

Don't skip headings levels. For example, don't directly go from H2 to H4. 

A single H1 for the page title is recommended.

### Target Sizes: 

Target guidelines can help users who aren't able to see the screen or who have difficulty with small touch targets to tap elements in your app. 

**Touch and Pointer Target sizes:** 

Touch targets are the parts of the screen that respond to user input, extending beyond the visual bounds of an element. For example, an icon may appear 24x24 dp , but the padding surrounding it comprises the full 48x48 dp touch target.![A row of four 24dp icons and one 40dp icon.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fl6qrcigc-touch-target-sizes.png?alt=media&token=0a243a43-cbf5-46da-92f0-4cafb28d799a)

For most platforms, consider making touch targets, 48x48 dp. A touch 