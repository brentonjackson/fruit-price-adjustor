# Fruit-Price-Adjustor

[![pic](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/challenge_photos/001/837/695/datas/full_width.png)](https://hackgsu-2022.devpost.com/)
![pic](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/877/026/datas/original.PNG)
⭐️ Winner of Best Hardware Hack, [HackGSU 2022](https://devpost.com/software/fruit-price-adjustor) ⭐️

Fruit-Price-Adjustor is an IOT app that monitors fruit in stores and adjusts the price of the fruit real-time based on its ripeness. This is an effort to reduce the amount of food waste as well as maximize profits. It is implemented with a camera and machine learning, paired with a full-stack web app and sms messaging.


## Table Of Contents

- [Fruit-Price-Adjustor](#fruit-price-adjustor)
  - [Table Of Contents](#table-of-contents)
  - [Technology Used](#technology-used)
  - [Installation](#installation)
      - [Pre-work](#pre-work)
      - [Setup and Running App](#setup-and-running-app)
    - [sms service (optional)](#sms-service-optional)
  - [Credits](#credits)


## Technology Used

- Camera Input: **Webcam** (I used a Raspberry Pi but you can also use your standard laptop webcam)
- Messaging software: **ImageZMQ (Python)**
- Machine Learning Framework: **TensorFlow (Python)**
- Web App: **MERN Stack**
- SMS Messaging: **Twilio**


## Installation

#### Pre-work

The main functionality is all in **Python**. The web app portion is in **Node**. So you need both **pip** and **npm**.

- After forking this repo, first get all the python files up and running. If you are using two different computers, you'll want to have the repo on both machines. Keep in mind that the server uses TensorFlow. So you'll probably want a Windows machine for that, if possible. This caused me more headache than necessary trying to get it up and running with the M1 chip.
- On your server machine (the machine without the camera feed), **grab your ip address**. You'll need it because that's how the client will send the image feed.

#### Setup and Running App

1. On client machine, start client from the **/server** folder: `python client.py -s [ip_address_of_server]`
   - I suggest either looking at the code to determine what pip packages you're missing, or looking at the error feedback and installing the packages then, if they aren't already installed.
2. Install all npm packages on both computers (in both client and server folders, `npm install`)
3. `cd server && npm run dev`. This script will run the python server and webserver concurrently and launch the web app. You can view the front end on http://localhost:3000/ by default. Note that nothing will really happen until the client is running as well.
   - Again, there will likely be Python packages you don't have that are needed, so the errors may come from that. Install all the needed packages for the server using pip.

### sms service (optional)

4. To setup Twilio messaging, create a number on Twilio then tunnel tunnel your localhost port 5000 (the web server) as a webhook.
   1. To do this, install ngrok.
   2. Then run the command `ngrok http 5000` in the **/server** folder. Take that http forwarding address and add it to your twilio handler.


## Credits

Fruit-Price-Adjustor was written by Brenton Jackson and Md Reazul Islam.
Thanks to the HackGSU organizors, mentors, and sponsors!

\*If there is anything unclear or could be better worded, we welcome all forms of feedback
