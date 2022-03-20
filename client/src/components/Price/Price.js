import React, { useState, useEffect } from "react";
import {
  Card,
  CardContent,
  Typography,
  CircularProgress,
} from "@material-ui/core/";

import * as api from "../../api";

import useStyles from "./styles";

const Price = () => {
  const [price, setPrice] = useState("0");
  const classes = useStyles();
  useEffect(() => {
    const intervalId = setInterval(() => {
      //assign interval to a variaable to clear it
      api
        .fetchPrice()
        .then((obj) => {
          let newData = obj.data.data;
          return newData;
        })
        .then((newData) => {
          setPrice((prevState) => newData);
        })
        .catch((err) => {
          console.log(err);
          setPrice((prevState) => prevState);
        });
    }, 5000);

    return () => {
      clearInterval(intervalId); //This is important
    };
  }, [useState]);

  return !price ? (
    <CircularProgress />
  ) : (
    <Card className={classes.card} raised elevation={6}>
      <CardContent>
        <p className="price-header">Price</p>
        <Typography
          variant="body2"
          color="textSecondary"
          component="p"
          style={{ fontSize: "40px" }}
        >
          ${price}.00
        </Typography>
      </CardContent>
    </Card>
  );
};

export default Price;
