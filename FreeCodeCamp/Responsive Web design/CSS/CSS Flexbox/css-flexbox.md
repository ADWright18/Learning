# CSS Flexbox
* CSS3 introduced Flexible Boxes, or flexbox, to create page layouts for a
dynamic UI. It is a layout mode that arranges elements in a predictable way for
different screen sizes and browsers

## Use display: flex to Position Two Boxes
* Placing the CSS property ```display: flex;``` on an element allows you to use
other properties to build a responsive page.
* Example:

```css
#box-container {
  height: 500px;
  display: flex;
}
```

## Use the flex-direction Property to Make a Row
* Adding ```display: flex``` to an element turns it into a flex container. This
makes it possible to align any children of that element into rows or columns.
* Other options for ```flex-direction``` are row-reversed and colun-reverse.
* Example:

```css
#box-container {
  display: flex;
  height: 500px;
  flex-direction: row;
}
```

## Use the flex-direction Property to Make a Column
* You can also create columns using ```flex-direction: columns```
* Example:

```css
#box-container {
  display: flex;
  height: 500px;
  flex-direction: column;
}
```
