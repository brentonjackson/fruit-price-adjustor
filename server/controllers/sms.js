import express from "express";
import fs from "fs";
import twilio from "twilio";
import dotenv from "dotenv";

const MessagingResponse = twilio.twiml.MessagingResponse;
if (process.env.NODE_ENV !== "production") {
  dotenv.config();
}

const router = express.Router();

export const postSms = async (req, res) => {
  try {
    const twiml = new MessagingResponse();
    let message = req.body.Body;
    let filename = "currentFruitPrice.txt";
    let price = fs.readFileSync(process.cwd() + "/" + filename).toString();

    if (message == undefined || message == "") {
      twiml.message(
        "Hi 😃! Thanks for using the demo version of FruitPriceAdjustor! Contact Brenton or Reazul to learn more about our full version!"
      );
    } else {
      twiml.message(`Current Banana Price:  $${price}.00`);
    }

    // if (req.body.Body === "🍌") {
    //   twiml.message("Price: ");
    // }

    res.writeHead(200, { "Content-Type": "text/xml" });
    res.end(twiml.toString());
  } catch (error) {
    res.status(404).json({ message: error.message });
  }
};

export default router;
