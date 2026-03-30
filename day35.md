# Day 35: Adding CSS

## What I Built Today
I styled my semantic blog page with CSS. I used element selectors to add colors, spacing, and layout.

## What I Learned
- CSS must go inside `<style>` tags in the `<head>`.
- `font-family`, `background-color`, `color`, `margin`, `padding`, `border`, `text-align`, `text-decoration`.
- How to target nested elements like `article header` and `article footer`.
- I made a typo `san-serif` which I fixed to `sans-serif`.

## My Code
```html
[Paste your final HTML+CSS code]<!DOCTYPE html>
<html>
<head>
    <title> day 35 </title>
    <style>
body {
    font-family: Arial, san-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}
header {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}
nav a {
    color: #fff;
    margin: 0 10px;
    text-decoration: none;
}
main {
    padding: 20px;
}
article {
    margin-bottom: 20px;
}
article header {
    border-bottom: 1px solid #ccc;
    margin-bottom: 10px;
}
article footer {    border-top: 1px solid #ccc;
    margin-top: 10px;    padding-top: 10px;
}
footer {    background-color: #333;
    color: #fff;    text-align: center;
    padding: 10px;
}
</style>
</head>
<body>
    <header>
        <h1> learning journal </h1>
        <nav>
            <a href="#"> home </a>
            <a href="#"> posts </a>
            <a href="#"> about </a>
        </nav>
    </header>
    <main>
        <article>
            <header>
                <h2> learning html reason </h2>
                <p>Posted on March 27th, 2026 by Helios</p>
            </header>
            <p> Today, I started learning HTML to build my own website. I want to create a personal blog where I can share my thoughts and experiences. Learning HTML will allow me to structure my content and make it visually appealing. I'm excited to see how my website will evolve as I learn more about web development! </p>
            <p>Today I learn tags</p>
            <footer>
                <p>Web development is fun!</p>
            </footer>
        </article>
    </main>
    <footer>
        <p>&copy; 2026 Helios. All rights reserved.</p>
    </footer>
</body>
</html>
```
## Key Takeaway
CSS brings HTML to life. I can now control colors, spacing, and fonts.

