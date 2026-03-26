# Day 33: HTML Tables

## What I Built Today
A leaderboard table showing top tutors with ranks, names, points, and ratings.

## What I Learned
- `<table>` creates the table.
- `<thead>` groups header rows; `<tbody>` groups data rows.
- `<tr>` is a table row.
- `<th>` is a header cell (bold and centered by default).
- `<td>` is a standard data cell.
- Tables are for **tabular data** – things that fit in rows and columns.
- What I struggled with today was getting the <thead> and <tbody> structure right. I originally closed </thead> before opening it.

## My Code
```html
<!DOCTYPE html>
<html>
<head>
    <title>Day 33 - tutor leaderboard</title>
</head>
<body>
    <h1>top tutors</h1>
    <table border="1">
    <thead>
        <tr>
            <th>rank</th>
            <th>name</th>
            <th>points</th>
            <th>rating</th>
            <th>reviews</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Yuchi Tongyou</td>
            <td>1500</td>
            <td>4.9</td>
            <td>100</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Jake</td>
            <td>1450</td>
            <td>4.5</td>
            <td>50</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Sam</td>
            <td>1400</td>
            <td>4.5</td>
            <td>20</td>
        </tr>    
         <tr>
            <td>4</td>
            <td>Tom Chan</td>
            <td>1300</td>
            <td>4</td>
            <td>10</td>
        </tr>
    </tbody>
    </table>
</body>
</html>
```

## Key Takeaway
Tables are the right tool for data like leaderboards. I typed every tag myself and now I understand how the structure works.
