
---
---
# 0. First JavaScript
#### Put script into the `head` section, the javascript will run automatically

E.g., `1.hello.html`
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>first demo</title>
    <script>
        alert("Hello, world!");
    </script>
</head>
  <body>
    <h1>Hello!</h1>
  </body>
</html>
```

---
---
# 1. JavaScript [Events](https://www.w3schools.com/js/js_events.asp)
Add an attribute to the HTML element called `onclick`
E.g., `1.hello2.html`
```html
<button onclick="alert('Hello')">
      Click here!
</button>
```
Common HTML Events
- onchange:	An HTML element has been changed
- onclick:	The user clicks an HTML element
- onmouseover:	The user moves the mouse over an HTML element
- onmouseout:	The user moves the mouse away from an HTML element
- onkeydown:	The user pushes a keyboard key
- onload:	The browser has finished loading the page

---
---
# 3. JavaScript [Functions](https://www.w3schools.com/js/js_functions.asp)
A JavaScript function is a block of code designed to perform a particular task.

A JavaScript function is executed when "something" invokes it (calls it).

E.g., `1.hello3.html`
```html
<script>
    function hello() {
        alert("Hello, world!");
    }
</script>
<button onclick="hello()">
      Click here!
</button>
```

# 3. JavaScript [Variables](https://www.w3schools.com/js/js_variables.asp)
#### Variables are Containers for Storing Data
JavaScript Variables can be declared in 4 ways:

1. Automatically
```html
<p id="demo"></p>

<script>
x = 5;
y = 6;
z = x + y;
document.getElementById("demo").innerHTML =
"The value of z is: " + z;
</script>
```
>Note: It is considered good programming practice to always declare variables before use. So we do not use automatically often.

2. Using var
```html
<p id="demo"></p>

<script>
var x = 5;
var y = 6;
var z = x + y;
document.getElementById("demo").innerHTML =
"The value of z is: " + z;
</script>
```
> Note:
> The var keyword was used in all JavaScript code from 1995 to 2015.
> The let and const keywords were added to JavaScript in 2015.
> The var keyword should only be used in code written for older browsers.

3. Using let
```html
let x = 5;
let y = 6;
let z = x + y;
```

4. Using const
```html
const x = 5;
const y = 6;
const z = x + y;
```

## When to Use var, let, or const?
1. Always declare variables

2. Always use `const` if the value should not be changed

3. Always use `const` if the type should not be changed (Arrays and Objects)

4. Only use `let` if you can't use `const`

5. Only use `var` if you MUST support old browsers.

E.g., `2.counter.html`
- Create a variable `let counter=0` to track the number of times of click events
- Create a function `count()` that takes the click event
```html
<script>
    let counter = 0;

    function count() {
        counter += 1;
        // or counter++;
        // or counter = counter + 1;

        // display an alert with the value of counter
        alert(counter);
    }
</script>

<button onclick="count()">
    Count!
</button>
```

# 4. Manipulate the DOM document object model 

#### JavaScript Can Change HTML Content

E.g., `1.hello4.html`
```html
<script>
    function Goodbye() {
    document.querySelector("#hello").innerHTML = "Goodbye!";
    }
</script>
<h1 id="hello">Hello!</h1>

<button onclick="Goodbye()">
    Click here!
</button>
```

# 4.1 Use conditional expression
E.g., `1.hello5.html`
```html
<script>
    function GoodbyeHello() {
        if (document.querySelector("#firstH1").innerHTML === "Hello!") {
            document.querySelector("#firstH1").innerHTML = "Goodbye!";
        } else {
            document.querySelector("#firstH1").innerHTML = "Hello!";
        }
    }
</script>
<h1 id="firstH1">Hello!</h1>

<button onclick="GoodbyeHello()">
    Click here!
</button>
```

Improve the code with variables, see `3.submit.html`.
```html
<script>
    const heading = document.querySelector("#firstH1")
    function GoodbyeHello() {
        if (heading.innerHTML === "Hello!") {
            heading.innerHTML = "Goodbye!";
        } else {
            heading.innerHTML = "Hello!";
        }
    }
</script>
```
---
E.g., `2.counter2.html`
```html
<script>
    let counter = 0;

    function count() {
        counter += 1;
        document.querySelector("#myH1").innerHTML = counter;
    }
</script>

<body>
<h1 id="myH1">0</h1>

<button onclick="count()">
    Count!
</button>
</body>
```

Add a conditional expression
```html
<script>
    let counter = 0;

    function count() {
        counter += 1;
        document.querySelector("#myH1").innerHTML = counter;
        if (counter % 10 === 0) {
            alert(`Count is now ${counter}`);
        }
    }
</script>
```

# 4.2 Use Event Listeners
To improve the code, i.e., remove the `onclick="count()"` attribute, we could add `` in the script
```html
<script>
    let counter = 0;

    function count() {
        counter += 1;
        document.querySelector("#myH1").innerHTML = counter;
    }

    // function count() can be also sent to an element
    document.querySelector("button").onclick = count;

</script>

<body>
<h1 id="myH1">0</h1>

<button>
    Count!
</button>
</body>
```
However, this will not work as expected, because the page is not loaded.

There are several ways to solve this problem:
1. move the `document.querySelector("button").onclick = count;` to the end of the `<body>`
2. add event listeners
   E.g.,
```html
<script>
    let counter = 0;

    function count() {
        counter += 1;
        document.querySelector("#myH1").innerHTML = counter;
    }

    // the addEventListener has two arguments, one is the event, and the second is the function to be called
    document.addEventListener("DOMContentLoaded", function() {
        // function count() can be also sent to an element
        document.querySelector("button").onclick = count;
        // equivalent to
        // document.querySelector("button").addEventListener("click", count);
    });
</script>

<body>
<h1 id="myH1">0</h1>

<button>
    Count!
</button>
</body>
```

# 5. You can move the JavaScript to a independent file
E.g., `2.counter5.html`










