# Day 41: CSS Transitions & Hover Effects

## What I Built Today
A card grid with smooth hover effects: cards lift slightly and show a shadow.

## What I Learned
- `transition: all 0.3s ease` makes property changes animate smoothly.
- `transform: translateY(-5px)` moves the card up on hover.
- `box-shadow` adds depth on hover.
- Cleaned up extra CSS properties and fixed typos (`sans-serif`, `text-align: center`).

## My Code
```html
<!DOCTYPE html>
<html>
    <head>
        <title> day 41</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: Arial, sans-serif;
                padding: 20px;
                text-align: center;   
            }
            .card-container {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                justify-content: center;
            }
            .card {
                flex: 1 1 250px;
                background: #f9f9f9;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 20px;
                transition: all 0.3s ease;
            }
            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
        </style>
    </head>
    <body>
        <h1> day 41 hover effects </h1>
        <div class="card-container">
            <div class="card">
                <h2> card 1 </h2>
                <p> hello </p>
            </div>
            <div class="card">
                <h2> card 2 </h2>
                <p> hello </p>
            </div>
            <div class="card">
                <h2> card 3 </h2>
                <p> hello </p>
            </div>
        </div>
    </body>
</html>
```
## Key Takeaway
Small hover effects make a page feel interactive. Transitions make changes smooth instead of abrupt.
