
---
---
# 1. Javascript with form
querySelector:
- document.querySelector("tag")
- document.querySelector("#id")
- document.querySelector(".class")

E.g., `3.submit.html`
```html
<script>
    function GoodbyeHello() {
            if (heading.innerHTML === "Hello!") {
                heading.innerHTML = "Goodbye!";
            } else {
                heading.innerHTML = "Hello!";
            }
        }

    document.addEventListener("DOMContentLoaded", function() {
        document.querySelector("form").onsubmit = function() {
            const name = document.querySelector("#name").value;
            alert(`Hello, ${name}!`);
        }
    });
</script>

<body>
    <h1 id="firstH1">Hello!</h1>
    <form action="">
        <input autofocus id="name" placeholder="Name" type="text">
        <input type="submit" value="Submita">
    </form>
</body>
```

## 2.2 Replace the H1 content
E.g., `3.submit2.html`
```html
<script>
    document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#boot").onsubmit = function(event) {
        event.preventDefault(); // Prevent form submission
        const name = document.querySelector('#name').value;
        const heading = document.querySelector('#baat');
        heading.innerHTML = `Hello, ${name}!`;
    };
    });
</script>
```
If `event.preventDefault();` were omitted:

- The form would be submitted to the server as soon as the submit button is clicked.
- The page would reload, and the browser would navigate to the URL specified in the form's action attribute (or reload the current page if action is not set).
- The JavaScript code that updates the `<h1>` element would not execute, as the page reload interrupts the script.

By including `event.preventDefault();`, you ensure that the form's submission is handled entirely by your custom JavaScript code, providing a seamless and interactive user experience.



---
---
# 2. Change the CSS style property
E.g., `4.colors.html`
```html
<script>
    document.addEventListener("DOMContentLoaded", function(){
    // Change font color to red
    document.querySelector("#red").onclick = function(){
        document.querySelector("#hello").style.color = "red";
    };
    // Change font color to blue
    document.querySelector("#blue").onclick = function(){
        document.querySelector("#hello").style.color = "blue";
    };
    // Change font color to red
    document.querySelector("#green").onclick = function(){
        document.querySelector("#hello").style.color = "green";
    };

    });
</script>
<body>
    <h1 id="hello">Hello!</h1>
    <button id="red">Red</button>
    <button id="blue">Blue</button>
    <button id="green">Green</button>
</body>
```

## 2.1 Optimize the code with `data attributes` and `querySelectorAll` function

E.g., `4.colors2.html`
```html
<script>
    document.addEventListener("DOMContentLoaded", function(){
    
        document.querySelectorAll("button").forEach(function(button) {

            button.onclick = function() {
                document.querySelector("#hello").style.color = button.dataset.color;
            };
        });

    });
</script>
<body>
    <h1 id="hello">Hello!</h1>
    <!-- data attributes: data-attribute, here is data-color  -->
    <button data-color="red">Red</button>
    <button data-color="blue">Blue</button>
    <button data-color="green">Green</button>
</body>
```

#### shorthand for functions:
```html
<script>
    document.addEventListener("DOMContentLoaded", () => {
    
        document.querySelectorAll("button").forEach(button => {

            button.onclick = () => {
                document.querySelector("#hello").style.color = button.dataset.color;
            };
        });

    });
</script>
<body>
    <h1 id="hello">Hello!</h1>
    <!-- data attributes: data-attribute, here is data-color  -->
    <button data-color="red">Red</button>
    <button data-color="blue">Blue</button>
    <button data-color="green">Green</button>
</body>
```

## 2.2 Use dropdown menu
E.g., `4.colors3.html`;
```html
<script>
    document.addEventListener("DOMContentLoaded", function(){

        document.querySelector("select").onchange = function(){
        // this here is the dropdown menu 
        document.querySelector("#hello").style.color = this.value;
        };
    });
</script>
<body>
    <h1 id="hello">Hello!</h1>

    <select name="color" id="">
        <option value="black">Black</option>
        <option value="red">Red</option>
        <option value="blue">Blue</option>
        <option value="green">Green</option>
    </select>
</body>
```
