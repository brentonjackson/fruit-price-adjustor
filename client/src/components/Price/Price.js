import React, { useState, useEffect } from "react";
import {
  Card,
  CardActions,
  CardContent,
  CardMedia,
  Button,
  Typography,
  ButtonBase,
  Grid,
  CircularProgress,
} from "@material-ui/core/";
import MoreHorizIcon from "@material-ui/icons/MoreHoriz";
import ThumbUpAltOutlined from "@material-ui/icons/ThumbUpAltOutlined";
import moment from "moment";
import { useHistory } from "react-router-dom";
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
      <ButtonBase component="span" name="test" className={classes.cardAction}>
        <CardContent>
          <Typography variant="body2" color="textSecondary" component="p">
            {price}
          </Typography>
        </CardContent>
      </ButtonBase>
    </Card>
  );
};

export default Price;
