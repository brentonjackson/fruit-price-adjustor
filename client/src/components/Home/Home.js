import React from "react";
import { Container, Grow } from "@material-ui/core";
import Price from "../Price/Price";

const Home = () => {
  return (
    <div className="home-div">
      <img
        src="/images/banana-clip-art.png"
        alt="image"
        className="banana-image"
      />
      <Price />
    </div>
  );
};

export default Home;
