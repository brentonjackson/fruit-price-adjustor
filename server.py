# Program on server (macbook) to get video
# streams and display/process them

import cv2
import imagezmq
import random

imageHub = imagezmq.ImageHub()
# initialize neural network stuff #

###################################


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


count = 0
while True:
    # receive frame and acknowledge receipt
    rpiName, frame = imageHub.recv_image()
    imageHub.send_reply(b'OK')

    ########### PROCESS FRAME #######
    fruit_status = 1

    #################################

    ######## WEB APP PROCESSING #####

    # write price to file currentFruitPrice.txt
    f = open('currentFruitPrice.txt', 'w')
    # price = fruit_price(fruit_status)
    price = random.choice([0.75, 1.00, 1.25, 2.00, 3.00])
    print('random price: ', price)
    f.write(str(price))
    f.close()

    # save image to file
    cv2.imwrite("currentFrame.jpg", frame)

    cv2.imshow(rpiName, frame)

    ##################################

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# cleanup
cv2.destroyAllWindows()
