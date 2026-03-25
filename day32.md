# Day 32: HTML Forms

## What I Built Today
A simple contact form with name and email fields – pure HTML, no CSS yet.

## What I Learned
- `<form>` wraps input fields; `action` and `method` control where data goes.
- `<label>` with `for` connects to an input's `id`.
- `<input type="text">` for text, `type="email"` for email (browser validates).
- `<input type="submit">` creates a submit button.
- I used VS Code's Emmet shortcuts (tab completion) – it's still me typing, just faster.

## My Code
```html
<!DOCTYPE html>
<html>
<head>
    <title>Day 32 Form</title>
</head>
<body>
    <h1>Day 32 Form</h1>
    <form action="/submit" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
