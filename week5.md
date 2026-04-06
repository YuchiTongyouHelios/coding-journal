## Week 1 of Month 2: HTML & CSS Foundations  
*March 19 – March 25, 2026*

### What I Built This Week  
After a month of Python, I started learning HTML and CSS. I built a personal page, a form, a leaderboard table, a semantic blog layout, and finally styled everything with CSS.

| Day | Project / Focus | Key Concepts |
|-----|----------------|---------------|
| 29 | First HTML Page | Tags, headings, lists, paragraphs, inline CSS (`<style>`) |
| 30 | Links & Images | `<a>` href, `<img>` src, alt text, link targets, debugging broken images |
| 31 | Contact Form + Bio Page | `<form>`, `<input>`, `<textarea>`, `<label>`, submit button, connecting `for` and `id` |
| 32 | HTML Form (simple) | `type="text"`, `type="email"`, `required` attribute |
| 33 | HTML Table | `<td>`, `<th>`, `<td>`, `<thead>`, `<tbody>`, logical data ordering |
| 34 | Semantic HTML | `<header>`, `<nav>`, `<main>`, `<article>`, `<footer>` – meaning over appearance |
| 35 | CSS Basics | Selectors, colors, fonts, box model (margin/padding), hover effects, `<style>` placement |

### What I Learned

#### 🧱 HTML Structure (Days 29–30)
- HTML is the **noun** – it holds content in labelled boxes.
- Tags come in pairs: `<h1>content</h1>`.
- Live Server in VS Code shows changes instantly – better than double‑clicking files.
- **Broken images taught me** that some URLs block hotlinking (403 errors). I switched to placekitten.com.

#### 📝 Forms (Days 31–32)
- `<form>` wraps everything. `action` and `method` control where data goes (we'll use later).
- `<label>` with `for` connects to an input's `id` – makes form accessible and lets you click the label to focus the field.
- Different input types: `text`, `email`, `submit`. The browser validates email format.
- `<textarea>` for multi‑line messages.
- I typed the whole form manually – no copy‑paste.

#### 📊 Tables (Day 33)
- `<table>` for table, `<tr>` for rows, `<th>` for headers, `<td>` for data cells.
- `<thead>` and `<tbody>` group header and body rows – helps with styling later.
- **Struggled with ordering** – my points were random at first. Had to fix so rank 1 had highest points. Learned that data must be logical, not just any numbers.

#### 🧩 Semantic HTML (Day 34)
- `<header>`, `<nav>`, `<main>`, `<article>`, `<footer>` describe what the content *is*, not just how it looks.
- Improves accessibility (screen readers) and SEO.
- I used `<header>` twice: one for page header, one inside the article for post metadata.

#### 🎨 CSS Basics (Day 35)
- CSS goes inside `<style>` in the `<head>` – not in a `<css>` tag (that was a bug I fixed).
- Element selectors: `body`, `h1`, `nav a` (nested selector).
- Properties: `background-color`, `color`, `font-family`, `margin`, `padding`, `border`, `text-align`.
- `:hover` pseudo‑class changes style when mouse over.
- **Typo alert:** `san-serif` doesn't work; it's `sans-serif`.

### Code Snippets

#### Day 31 – Contact Form + Bio Page

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hi, I am Helios Yuchi</title>
</head>
<body>
    <h1>Contact me</h1>
    <form>
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message"></textarea><br>
        <input type="submit" value="Submit">
    </form>
    <p>I am studying in Grade 8.</p>
    <p>In my free time, I like to explore new technologies...</p>
    <p>If you want to connect or learn more about my work, feel free to reach out!</p>
    <p>My Email is abc@gmail.com</p>
</body>
</html>

### Code Snippet – Final Styled Blog (Day 35)

```html
<!DOCTYPE html>
<html>
<head>
    <title>day 35</title>
    <style>
        body {
            font-family: Arial, sans-serif;
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
        nav a:hover {
            text-decoration: underline;
        }
        main {
            padding: 20px;
        }
        article {
            background: white;
            margin-bottom: 20px;
            padding: 15px;
            border-radius: 8px;
        }
        article header {
            border-bottom: 1px solid #ccc;
            margin-bottom: 10px;
            background: none;
            padding: 0;
        }
        footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>learning journal</h1>
        <nav>
            <a href="#">home</a>
            <a href="#">posts</a>
            <a href="#">about</a>
        </nav>
    </header>
    <main>
        <article>
            <header>
                <h2>learning html reason</h2>
                <p>Posted on March 27th, 2026 by Helios</p>
            </header>
            <p>Today, I started learning HTML to build my own website...</p>
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
## The Hard Truth This Week
I tried to rush – I wanted to skip to CSS on Day 32, but my HTML wasn't solid. Had to go back and really understand tables and forms.

File extension hell – saved as .txt by accident, got a white page with "hello world". Now I always check the file name in VS Code.

Placed <style> after </html> – browser still rendered it, but it's wrong. Style must be in <head>.

My blog posts were shallow at first – just copied my bullet points. I rewrote them to include what I actually struggled with (e.g., closing </thead> before opening it).

## Goals for Next Week (Days 36–42)
CSS Layout: Flexbox, Grid, media queries.

Responsive design: Make everything work on mobile.

Transitions & hover effects: Add polish.

Mini portfolio project: Combine everything.

## Advice to My Future Self
"HTML is just boxes. CSS is just rules. When stuck, use browser DevTools (right‑click → Inspect) to see what's actually happening. And always, always put <style> in the <head>."
