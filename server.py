# Program on server (macbook) to get video
# streams and display/process them

import cv2
import imagezmq
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
    '''
    if np.argmax(prediction)==0:
        st.write(f"Unripe😑")
    elif np.argmax(prediction)==1:
        st.write(f"Overripe😫")
    else :
        st.write(f"ripe😄")
    '''
    return prediction
###################################

while True:
    # receive frame and acknowledge receipt
    rpiName, frame = imageHub.recv_image()
    imageHub.send_reply(b'OK')

    ########### PROCESS FRAME #######
    fruit_status = 1

    image = frame
    #st.image(image, use_column_width=True)
    model = tf.keras.models.load_model('ripeness.h5')
    prediction = predict_stage(image, model)
    print('THE PREDICTION IS ' + prediction[0][1])
    #################################

    ######## WEB APP PROCESSING #####
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
    price = fruit_price(fruit_status)

    # create server

    ##################################

    cv2.imshow(rpiName, frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# cleanup
cv2.destroyAllWindows()
