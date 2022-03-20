import React, { useState } from "react";
import {
  Container,
  Grow,
  Grid,
  AppBar,
  TextField,
  Button,
  Paper,
} from "@material-ui/core";
import Price from "../Price/Price";

const Home = () => {
  return (
    <Grow in>
      <Container maxWidth="xl">
        <Price />
      </Container>
    </Grow>
  );
};

export default Home;
