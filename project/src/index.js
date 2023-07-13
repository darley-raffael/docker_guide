import express from "express";
const app = express();
const port = 3333;

app.get("/", (req, res) => {
  res.send("Iniciando o servidor");
});

app.listen(port, () => {
  console.log(`Server app listening on port: http://localhost:${port} 🚀`);
});
