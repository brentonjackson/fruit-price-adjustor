const express = require('express')
const app = express()
const cors = require('cors');
const port = 3000

app.use(cors());

app.get('/', (req, res) => {
  res.end('Hello World!');
});

app.get("/price", (req, res) => {
  var fs  = require("fs");
  var price = fs.readFileSync('./../currentFruitPrice.txt').toString();
  result = {
    price
  };
  res.send(result);
});

app.listen(port, () => {
    console.log(`app listening at http://localhost:${port}`)
  });