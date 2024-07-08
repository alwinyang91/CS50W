
---
---
# 1. React: A Declarative Programming Framework
e.g., `react.html`

---
# 1.2 Reuse the component of react functions
e/g/, `hello.html`.

---
# 1.3 Create the counter application with react
e.g., `counter.html`.

---
---
# 2. Build a React based application
```html
<script type="text/babel">

    function App() {

        return (
            <div>
                <div>1+2</div>
                <input />
            </div>
        )
    }

    ReactDOM.render(<App />, document.querySelector("#app"));
</script>
```

Instead, I want these 1 and 2 to be based on some underlying state inside of my application.
The application is going to maintain state about what two numbers to add together, 
and then it's going to display a user interface based on that state.
```html
<script type="text/babel">

    function App() {
        // // This is not convenient 
        // const [num1, setNum1] = React.useState(1);
        // const [num2, setNum2] = React.useState(2);

        const [state, setState] = React.useState({
                    num1: 1,
                    num2: 1,
                });

        return (
            <div>
                <div>{state.num1} + {state.num2}</div>
                <input />
            </div>
        )
    }

    ReactDOM.render(<App />, document.querySelector("#app"));
</script>
```

# 2.1 Keep track of the inputfield
e.g., `addition2.html`
```html
<script type="text/babel">

    function App() {
        // // This is not convenient 
        // const [num1, setNum1] = React.useState(1);
        // const [num2, setNum2] = React.useState(2);

        const [state, setState] = React.useState({
                    num1: 1,
                    num2: 1,
                    response: "",
                });

        function updateResponse(event) {
                    setState({
                        ...state,
                        response: event.target.value
                    });
                }

        return (
            <div>
                <div>{state.num1} + {state.num2}</div>
                <input onChange={updateResponse} value={state.response} />
            </div>
        )
    }

    ReactDOM.render(<App />, document.querySelector("#app"));
</script>
```

# 2.2 Check the answer is right or wrong
e.g., `addition3.html`.
```html
<script type="text/babel">

    function App() {

        const [state, setState] = React.useState({
                    num1: 1,
                    num2: 1,
                    response: "",
                    score: 0,
                });

        function updateResponse(event) {
                    setState({
                        ...state,
                        response: event.target.value
                    });
                }

        function inputKeyPress(event) {
            if (event.key === "Enter") {
                // to convert the inputfield to integer 
                const answer = parseInt(state.response);
                if (answer === state.num1 + state.num2) {
                    // User got question right
                    setState({
                        ...state,
                        score: state.score + 1,
                        response: "",
                        num1: Math.ceil(Math.random() * 10),
                        num2: Math.ceil(Math.random() * 10),
                    });
                } else {
                    // User got question wrong
                    setState({
                        ...state,
                        score: state.score - 1,
                        response: "",
                    })
                }
            }
        }

        return (
            <div>
                <div>{state.num1} + {state.num2}</div>
                <input onKeyPress={inputKeyPress} onChange={updateResponse} value={state.response} />
                <div>Score: {state.score}</div>
            </div>
        )
    }

    ReactDOM.render(<App />, document.querySelector("#app"));
</script>
```

# 2.3 Make the userinterface nicer
e.g., `addition4.html`.
```html
<script type="text/babel">

    function App() {

        const [state, setState] = React.useState({
            num1: 1,
            num2: 1,
            response: "",
            score: 0,
            incorrect: false
        });

        function renderWinScreen() {
            return (
                <div id="winner">You won!</div>
            );
        }

        function inputKeyPress(event) {
            if (event.key === "Enter") {
                const answer = parseInt(state.response);
                if (answer === state.num1 + state.num2) {
                    // User got question right
                    setState({
                        ...state,
                        score: state.score + 1,
                        response: "",
                        num1: Math.ceil(Math.random() * 10),
                        num2: Math.ceil(Math.random() * 10),
                        incorrect: false
                    });
                } else {
                    // User got question wrong
                    setState({
                        ...state,
                        score: state.score - 1,
                        response: "",
                        incorrect: true
                    })
                }
            }
        }

        function updateResponse(event) {
            setState({
                ...state,
                response: event.target.value
            });
        }

        function renderProblem() {
            return (
                <div>
                    <div className={state.incorrect ? "incorrect" : ""} id="problem">
                        {state.num1} + {state.num2}
                    </div>
                    <input onKeyPress={inputKeyPress} onChange={updateResponse} autoFocus={true} value={state.response} />
                    <div>Score: {state.score}</div>
                </div>
            )
        }

        if (state.score === 10) {
            return renderWinScreen();
        } else {
            return renderProblem();
        }
    }

    ReactDOM.render(<App />, document.querySelector("#app"));
</script>
```