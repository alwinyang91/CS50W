function hello() {
    alert("Hello, world!");
  };

  let counter = 0;
  let counter2 = 0;
  let counter3 = 0;
  let counter4 = 0;

  function count() {
      counter += 1;
      // or counter++;
      alert(counter);
  }

  function sayGoodbye() {
      // look though the html page, and extract the element "h1" in the page 
      // then change the element content to "Goodbye" 
      document.querySelector("h1").innerHTML = "Goodbye!";
  }

  function sayGoodbye2() {
      if (document.querySelector("h1").innerHTML === "Hello!") {
          document.querySelector("h1").innerHTML = "Goodbye!";
      } else {
          document.querySelector("h1").innerHTML = "Hello!";
      }
  }
  // improve the code 
  function sayGoodbye3() {
      const heading = document.querySelector("h1");  // const mean the variable will never be changed
      if (heading.innerHTML === "Hello!") {
          heading.innerHTML = "Goodbye!";
      } else {
          heading.innerHTML = "Hello!";
      }
  }

  function count2() {
      counter2 += 1;
      document.querySelector("h2").innerHTML = counter2;
  }

  function count3() {
      counter3 += 1;
      document.querySelector("#count3").innerHTML = counter3;
      if (counter3 % 10 === 0) {
          alert(`Count is now ${counter3}`)
      }
  }

  // This does not work, because the page is not loaded 
  function count4_bad() {
      counter4 += 1;
      document.querySelector("#count4").innerHTML = counter4;
      if (counter4 % 10 === 0) {
          alert(`Count is now ${counter4}`)
      }
      // you can send onlick to be the fucntion count4 
      document.querySelector("#count4").onclick = count4_bad;
  }

  function count4() {
      counter4 += 1;
      document.querySelector("#count4").innerHTML = counter4;
      if (counter4 % 10 === 0) {
          alert(`Count is now ${counter4}`)
      }
  }
  // you can send onlick to be the fucntion count4 
  document.addEventListener('DOMContentLoaded', function() {
      // document.querySelector("#count4").onclick = count4;
      document.querySelector("#count4butten").addEventListener('click', count4);
  });