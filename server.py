# Program on server (macbook) to get video
# streams and display/process them

import cv2
import imagezmq
import random
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

imageHub = imagezmq.ImageHub()
# initialize neural network stuff #
def predict_stage(image_data,model):
    size = (224, 224)
    image = ImageOps.fit(image_data,size, Image.ANTIALIAS)
    image_array = np.array(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    preds = ""
    prediction = model.predict(data)
    return prediction

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

    image = Image.fromarray(frame)
    #st.image(image, use_column_width=True)
    model = tf.keras.models.load_model('ripeness.h5')
    prediction = predict_stage(image, model)
    prob = prediction[0][1]
    print('THE PREDICTION IS ' + str(prob))

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
