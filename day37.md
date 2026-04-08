# Day 37: Flexbox Navbar

## What I Built Today
A navigation bar using `display: flex`. Logo on the left, links on the right.

## What I Learned
- `display: flex` turns a container into a flex container.
- `justify-content: space-between` pushes first child left, last child right.
- `align-items: center` vertically centers flex items.
- Flexbox controls **where** children are placed, not **what** they look like.
- Children of a flex container become flex items; grandchildren are not affected.

## My Code
```html
<!DOCTYPE html>
<html>
<head>
    <title>Day 37 - navbar</title>
    <style>
        * {
            margin: 0;
            padding:0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif; 
        }
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #333;
            padding: 15px 30px;
        }
        .logo a {
            color: white;
            text-decoration: none;
            font-size: 1.5rem;
            font-weight: bold;
        }
        .nav-links {
            list-style: none;
            display: flex;
            gap: 20px;
        }
        .nav-links li a:hover {
            background-color: #555;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <header class="navbar">
        <div class="logo">
            <a href="#">My site</a>
        </div>
        <nav>
            <ul class="nav-links">
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>
</body>
</html>
```
## Key Takeaway
Flexbox is a layout tool. I now understand how to align elements without floats or inline-block.
