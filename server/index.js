import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
import priceRoutes from "./routes/price.js";
import smsRoutes from "./routes/sms.js";

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json({ limit: "30mb", extended: true }));
app.use(express.urlencoded({ limit: "30mb", extended: true }));
app.use(cors());

app.use("/price", priceRoutes);
app.use("/sms", smsRoutes);
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
