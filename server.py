# Program on server (macbook) to get video
# streams and display/process them

import cv2
import imagezmq

imageHub = imagezmq.ImageHub()
# initialize neural network stuff #

###################################

while True:
    # receive frame and acknowledge receipt
    rpiName, frame = imageHub.recv_image()
    imageHub.send_reply(b'OK')

    ########### PROCESS FRAME #######
    fruit_status = 1

    #################################

    ######## WEB APP PROCESSING #####

    price = fruit_price(fruit_status)

    # create server

    # helper functions

    def fruit_price(status):
        match status:
            case 1:
                return 1.50
            case 2:
                return 1.25
            case 3:
                return 1.00
            case 4:
                return 0.75
            case _:
                return "Something's wrong with the internet"
    ##################################

    cv2.imshow(rpiName, frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

# cleanup
cv2.destroyAllWindows()
