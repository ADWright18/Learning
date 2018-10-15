# Applied Accessibility
"Accessibility" generally means having web content and a user interface that can
be understood, navigated, and interacted with by a broad audience.

## Objectives
* Have well-organized code that uses appropriate markup
* Ensure text alternatives exist for non-text and visual content
* Create an easily-navigated page that's keyboard friendly

## Add a Text Alternative to Images for Visually Impaired Accessibility
* ```alt``` text describes the content of the image and provides a text-alternative
* This helps in case the image fails to load or can't be seen by a user.
* Good ```alt``` text is short but descriptive, and meant to briefly convey the
meaning of the message
* Example:

```html
<img src="doingKarateWow.jpeg" alt="Camper Cat Karate">
```

## Know When Alt Text Should be Left Blank
* Sometimes images are grouped with a caption already describing them, or are
used for decoration only. In these cases ```alt``` text may seem redundant or
unnecessary
* In situations when an image is already explained with text content, or does
not add meaning to a page, the ```img``` still needs an ```alt``` attribute, but
it can be set to an empty string
* Example:

```html
<img src="visualDecoration.jpeg" alt="">
```

## Use Headings to Show Hierarchical Relationships of Content
* Headings with equal (or higher) rank start new implied sections, headings with
lower rank start subsections of the previous one
* Example:

```html
<h1>How to Become a Ninja</h1>
<main>
  <h2>Learn the Art of Moving Stealthily</h2>
  <h3>How to Hide in Plain Sight</h3>
  <h3>How to Climb a Wall</h3>

  <h2>Learn the Art of Battle</h2>
  <h3>How to Strengthen your Body</h3>
  <h3>How to Fight like a Ninja</h3>

  <h2>Learn the Art of Living with Honor</h2>
  <h3>How to Breathe Properly</h3>
  <h3>How to Simplify your Life</h3>
</main>
```

## Jump Straight to the Content Using the main Element
* The ```main``` element is used to wrap the main content, and there should only
be one per page
* The ```main``` tag also has an embedded landmark feature that assistive
technology can use to quickly navigate to the main content.
* Example:

```html
<header>
  <h1>Weapons of the Ninja</h1>
</header>
<main>

</main>
<footer></footer>
```

## Wrap Content in the article Element
* ```article``` is another one of the new HTML5 elements that adds semantic meaning to your markup.
* ```article``` is a sectioning element, and is used to wrap independent, self-contained content.
* Reference:

```
<div> - groups content
<section> - groups related content
<article> - group independent, self-contained content
```

## Make Screen Reader Navigation Easier with the header Landmark
* The ```header``` tag is used to wrap introductory information or navigation links for its parent tag
* ```header``` shares the embedded landmark feature you saw with ```main```, allowing assistive technologies to quickly navigate to that content
* Note: ```header``` is meant for use in the ```body``` tag of your HTML document
* Example:

```html
<body>
  <header>
    <h1>Training with Camper Cat</h1>
  </header>
</body>
```

## Make Screen Reader Navigation Easier with the nav Landmark
* The ```nav``` element is meant to wrap around the main navigation links in your page