
---
---
# 1. Make a to-do list application


```html
<script>
    document.addEventListener("DOMContentLoaded", function(){

    document.querySelector("form").onsubmit = function(){
        const task = document.querySelector("#task").value;

        const li = document.createElement("li");

        li.innerHTML = task;

        document.querySelector("#tasks").append(li);

        // Stop form from submitting
        return false;

    };

    });
</script>

<body>
    <h1>Tasks</h1>
    <ul id="tasks">
    </ul>
    <form action="">
      <input id="task" placeholder="New Task" type="text">

      <br>
      <input id="sumbit" type="submit" value="Submit the task">
    </form>
</body>
```


# 1.3 Clear the input values after submission
```javascript
document.addEventListener("DOMContentLoaded", function(){

    document.querySelector("form").onsubmit = function(){
        const task = document.querySelector("#task").value;

        const li = document.createElement("li");

        li.innerHTML = task;

        document.querySelector("#tasks").append(li);

        // clear the input values
        document.querySelector("#task").value = "";

        // Stop form from submitting
        return false;
    };

});
```
# 1.4 Disable the sumbit buttion
```javascript
document.addEventListener("DOMContentLoaded", function(){

    // By default, subit button is disabled
    document.querySelector("#submit").disabled = true;
    // enable submit button when type content
    document.querySelector("#task").onkeyup = () => {
        document.querySelector("#submit").disabled = false;
    };

    document.querySelector("form").onsubmit = function(){
        const task = document.querySelector("#task").value;

        const li = document.createElement("li");

        li.innerHTML = task;

        document.querySelector("#tasks").append(li);

        // clear the input values
        document.querySelector("#task").value = "";

        // disable the button after submission
        document.querySelector("#submit").disabled = true;

        // Stop form from submitting
        return false;
    };

});
```

### 1.4.1 Prevent submit empty input
```javascript
document.addEventListener("DOMContentLoaded", function(){

    // By default, subit button is disabled
    document.querySelector("#submit").disabled = true;
    // enable submit button when type content
    document.querySelector("#task").onkeyup = () => {
        if (document.querySelector("#task").value.length > 0) {
            document.querySelector("#submit").disabled = false;
        } else {
            document.querySelector("#submit").disabled = true;
        }
    };

    document.querySelector("form").onsubmit = function(){
        const task = document.querySelector("#task").value;

        const li = document.createElement("li");

        li.innerHTML = task;

        document.querySelector("#tasks").append(li);

        // clear the input values
        document.querySelector("#task").value = "";

        // disable the button after submission
        document.querySelector("#submit").disabled = true;

        // Stop form from submitting
        return false;
    };

});
```

---
---
# 2. Use interval

E.g., `2.counter6.html`;
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

        // run the count function every 1000 milliseconds
        setInterval(count, 1000);
    });
</script>
```


---
---
# 3. Local Storage
Use localStorage to store and retrieve information from the browser
- localStorage.getItem(key)
- localStorage.setItem(key, value)

E.g., `6.storage.html`;
```html
<script>
    // ! means this is not something  
    if (!localStorage.getItem("counter")) {
        localStorage.setItem("counter", 0);
    };

    function count() {

        let counter = Number(localStorage.getItem("counter"));

        counter += 1;
        document.querySelector("#myH1").innerHTML = counter;

        localStorage.setItem("counter", counter);


    }
    // the addEventListener has two arguments, one is the event, and the second is the function to be called
    document.addEventListener("DOMContentLoaded", function() {
        // function count() can be also sent to an element
        document.querySelector("button").onclick = count;
        // equivalent to
        // document.querySelector("button").addEventListener("click", count);
    });
</script>
```

## 3.1 make the H1 not show 0 after reloaded

E.g., `6.storage1.html`;
```html
<script>
    // ! means this is not something  
    if (!localStorage.getItem("counter")) {
        localStorage.setItem("counter", 0);
    };

    function count() {

        let counter = Number(localStorage.getItem("counter"));

        counter += 1;
        document.querySelector("#myH1").innerHTML = counter;

        localStorage.setItem("counter", counter);


    }
    // the addEventListener has two arguments, one is the event, and the second is the function to be called
    document.addEventListener("DOMContentLoaded", function() {

        // show the stored counter number
        document.querySelector("#myH1").innerHTML = localStorage.getItem("counter");

        // function count() can be also sent to an element
        document.querySelector("button").onclick = count;
        // equivalent to
        // document.querySelector("button").addEventListener("click", count);
    });
</script>
<body>
    <h1 id="myH1"></h1>

    <button>
        Count!
    </button>

</body>
```



