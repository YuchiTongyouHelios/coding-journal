# Day 36: Box Model & Inline‑Block Cards

## What I Built Today
Three cards placed side‑by‑side using `display: inline-block`. Each card has padding, border, margin, and a hover effect.

## What I Learned
- **Box model:** Every element is a box. Total width = content + left/right padding + left/right border + left/right margin.
- **`inline-block`** lets elements sit in a row while respecting width, padding, margin, and border (unlike `inline`).
- **Whitespace gap:** There is a small space between inline‑block elements because of line breaks in HTML. Centering the container with `text-align: center` works fine.
- **Hover effects** change styles when the mouse is over an element.

## My Code
```html
<!DOCTYPE html>
<html>
<head>
    <title>Day 36 project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 40px;
        }
        .card-container {
            text-align: center;
        }
        .card {
            display: inline-block;
            width: 200px;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            background-color: #f0f0f0;
            vertical-align: top;
        }
        .card:hover {
            background-color: #e0e0e0;
            border-color: black;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>
    <h1>three cards - day 36 project</h1>
    <div class="card-container">
        <div class="card">
            <h2>Card 1</h2>
            <p>this card has padding, border, and margin. hover over me!</p>
        </div>
        <div class="card">
            <h2>Card 2</h2>
            <p>inline-block puts card side by side.</p>
        </div>
        <div class="card">
            <h2>Card 3</h2>
            <p>the box model = content + padding + border + margin</p>
        </div>
    </div>
</body>
</html>
```
## Key Takeaway
The box model is the foundation of CSS layout. I now understand how padding, border, and margin affect an element's total size and spacing.

