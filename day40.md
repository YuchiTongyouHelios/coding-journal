# Day 40: Media Queries – Responsive Grid

## What I Built Today
I made my CSS Grid layout responsive. On screens smaller than 768px, the layout stacks into a single column with header, main, sidebar, footer in that order.

## What I Learned
- `@media (max-width: 768px)` targets devices with screen width up to 768px.
- Inside the media query, I override `grid-template-areas` and `grid-template-columns` to 1fr.
- This makes the page readable on mobile without horizontal scrolling.

## My Code
```html
<!DOCTYPE html>
<html>
<head>
    <title>day 40 project</title>
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
        @media (max-width: 768px) {
            .grid-container {
                grid-template-areas:
                    "header"
                    "main"
                    "sidebar"
                    "footer";
                grid-template-columns: 1fr;
            }
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
Media queries are essential for responsive design. One layout for desktop, another for mobile – all with minimal code.
