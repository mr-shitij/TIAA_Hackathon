const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// GET endpoint to send a welcome message
app.get('/', (req, res) => {
  res.send('Welcome to the Express API!');
});

app.get('/get_user/:id', (req, resp) => {
  const id = req.params.id;
  console.log("User request id: ", id);
  resp.json({name: "Shitij", age: 20, portfolio: "Investment in tech compaines", companies: {"TATA": ["2022-04-01", 10000], "GOOGLE": ["2022-04-05", 32321]}});
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

