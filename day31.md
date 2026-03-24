# Day 31: Contact Form + Bio Page

## What I Built Today
A personal profile page with a contact form (name, email, message) and a short bio.

## What I Learned
- How to connect `<label>` with `<input>` using `for` and `id`.
- Different input types: text, email.
- `<textarea>` for multi-line messages.
- A submit button that tries to send the form data.

## My Code
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
        <p>In my free time, I like to explore new technologies, contribute to open source projects, and connect with other developers in the community. I believe in the power of collaboration and continuous learning to drive progress in the tech industry.</p>
        <p>If you want to connect or learn more about my work, feel free to reach out!</p>
        <p>My Email is abc@gmail.com</p>
    </body>
</html>
```
## Key Takeaway
I can now build a contact form from scratch. This is the same structure used in login and signup pages.

## What's Next
Tomorrow: HTML tables and nested lists.
