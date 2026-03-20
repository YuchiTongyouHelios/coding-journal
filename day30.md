# Day 30: Links, Images & Debugging

## What I Built Today
A webpage with a link to my GitHub and an image. I also learned to fix file extension issues when my page showed "hello world" instead of my HTML.

## What I Learned
- **File extensions matter** – a `.txt` file won't render as HTML; it must be `.html`.
- **The `<a>` tag** creates links; `href` is the destination; `target="_blank"` opens in a new tab.
- **The `<img>` tag** shows images; `src` is the URL; `alt` is text if the image fails.
- **Not all image URLs work** – some sites block hotlinking (403 error). I switched to a working placeholder.
- **Live Server** shows my changes instantly, but I need to open the correct `.html` file.

## My Code
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Helios - Day 30</title>
        <style>
            body { background-color: lightblue; }
            h1 { color: navy; }
            a { color: darkred; text-decoration: none; }
            a:hover { text-decoration: underline; }
            img { border-radius: 10px; width: 300px; }
        </style>
    </head>
    <body>
        <h1>Hello, I'm Helios – this is day 30 website</h1>
        <p>Check out my GitHub posts:</p>
        <a href="https://github.com/YuchiTongyouHelios/coding-journal" target="_blank">Coding Journal</a>
        <p>Posting every day</p>
        <img src="https://placekitten.com/400/300" alt="Cute kitten placeholder">
    </body>
</html>
```
## Key Takeaways
I had a problem of not being able to open it in a live server but after checking the HTML and it's name and it's file, I was able to open it at last.
