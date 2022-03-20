# Fruit-Price-Adjustor

## Steps to run the code locally

1. Start client from server folder: python client.py -s [ip_address_of_server]
2. Install all npm packages (in both client and server folders, npm install)
3. cd server && npm run dev

### (optional)

4. To setup Twilio messaging, creat a number on Twilio then tunnel tunnel your localhost port 5000 as a webhook
   To do this, install ngrok.
   Then run the command "ngrok http 5000" in the server folder. Take that http forwarding address and add it to your twilio handler.
