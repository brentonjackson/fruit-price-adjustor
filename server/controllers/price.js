import express from "express";
import fs from "fs";

const router = express.Router();

export const getPrice = async (req, res) => {
  try {
    // get price from file
    let filename = "currentFruitPrice.txt";
    let price = fs.readFileSync(process.cwd() + "/" + filename).toString();

    res.json({
      data: price,
    });
  } catch (error) {
    res.status(404).json({ message: error.message });
    console.log("tried to give you back file output");
  }
};

export default router;
