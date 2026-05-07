# Day 39: CSS Grid Layout

## What I Built Today
A two‑column blog layout using CSS Grid: header, sidebar, main content, footer.

## What I Learned
- `display: grid` creates a grid container.
- `grid-template-areas` defines the layout with named regions.
- `grid-template-columns` sets column widths using `fr` (fraction) units.
- Grid is better than flexbox for full‑page layouts because it controls rows and columns at the same time.
- I fixed syntax errors: misplaced braces and orphaned CSS rules.

## My Code
```html
<!DOCTYPE html>
<html>
<head>
    <title> day 39 project</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        .grid-container {
            display: grid;
            grid-template-areas:
                "header header header"
                "sidebar main main"
                "footer footer footer";
            gap: 20px;
            grid-template-columns: 1fr 2fr 1fr;
        }
        header {
            grid-area: header;
            background: #333;
            color: white;
            padding: 20px;
            text-align: center;
        }
        aside {
            grid-area: sidebar;
            background: #f4f4f4;
            padding: 15px;
        }
        main {
            grid-area: main;
            background: #fff;
            padding: 15px;
            border: 1px solid #ddd;
        }
        footer {
            grid-area: footer;
            background: #333;
            color: white;
            text-align: center;
            padding: 10px;
        }
    </style>
</head>
<body>
    <div class="grid-container">
        <header>
            <h1>My Blog</h1>
        </header>
        <aside>
            <h2>About Me</h2>
            <p>This is the sidebar.</p>
        </aside>
        <main>
            <h2>Main Content</h2>
            <p>This is where the blog posts go.</p>
        </main>
        <footer>
            <p>&copy; 2026 Helios</p>
        </footer>
    </div>
</body>
</html>
```
## Key Takeaway
Grid gives me precise control over both rows and columns. I can now build magazine‑style layouts.

