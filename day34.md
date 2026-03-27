# Day 34: Semantic HTML

## What I Built Today
A simple blog page layout using semantic HTML tags like `<header>`, `<nav>`, `<main>`, `<article>`, and `<footer>`.

## What I Learned
- **Semantic tags** describe the content they hold.
- They improve accessibility and SEO.
- I used `<header>` twice: one for the page header, one inside the article.
- `<nav>` holds navigation links.
- `<footer>` is for copyright/contact info.

## My Code
```html
<!DOCTYPE html>
<html>
<head>
    <title> day 34 </title>
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
Using meaningful tags makes my HTML structure clear and accessible.

