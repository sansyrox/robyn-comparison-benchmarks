const express = require("express"); // Acquire the express package and assign it to a variable called "express"
const app = express(); // Calls the method "express()" and assigns it's output to "app". "express()" will create an express app for you.

app.get("/", (req, res) => {
  // Creates sort of a listener for when there are "GET" requests to the "/" (root) path. Takes in req (request) and res (response)
  res.send("Hello world!"); // For the response, send a string "Hello World!"
});

app.listen(3000, () => {
  // Tells the app to start on port 3000. This function below is run when
  console.log("Server listening on port 3000!"); // Say in the console "Server listening on port 3000!"
});
