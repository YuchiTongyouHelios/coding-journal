**# Day 38: Flexbox Card Grid

## What I Built Today
A responsive card grid using `flex-wrap: wrap` and the `flex` shorthand.

## What I Learned
- `flex-wrap: wrap` allows cards to move to the next row when space runs out.
- `flex: 1 1 250px` means: grow to fill space, shrink if needed, start at 250px wide.
- `gap` adds spacing between rows and columns.
- Flexbox grids are responsive without media queries.

## My Code
```html
<!DOCTYPE html>
<html>
<head>
    <title>Day 38 project</title>
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
        .card-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
        }
        .card {
            flex-grow: 1;
            flex-shrink: 1;
            flex-basis: 250px;
            flex: 1 1 250px;
            background: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            transition: 0.2s;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <h1>Flexbox Card Grid</h1>
    <div class="card-container">
        <div class="card">
            <h2>Card 1</h2>
            <p>Hi I'm Card 1!.</p>
        </div>
        <div class="card">
            <h2>Card 2</h2>
            <p>Hi I'm Card 2!.</p>
        </div>
        <div class="card">
            <h2>Card 3</h2>
            <p>Hi I'm Card 3!.</p>
        </div>
        <div class="card">
            <h2>Card 4</h2>
            <p>Hi I'm Card 4!.</p>
        </div>
    </div>
</body>
</html>
```
## Key Takeaway
Flexbox with wrapping is a simple way to build responsive grids. I don't need media queries for basic card layouts.
