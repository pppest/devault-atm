# this code is mostly a mixup based on code found in the links below
# zbar: https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-
#   scanner-with-zbar/
# video: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/
#   py_gui/py_video_display/py_video_display.html

from pyzbar import pyzbar
import cv2
import time


def read_qr_code():
    barcode_data = ""
    print("Scan wallet QR code")
    cap = cv2.VideoCapture(0)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret is True:
            # check for qrcode and write if found and exit
            barcodes = pyzbar.decode(frame)
            # loop over the detected barcodes
            for barcode in barcodes:
                # extract the bounding box location of the barcode and draw the
                # bounding box surrounding the barcode on the image
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # the barcode data is a bytes object so if we want to draw
                # it on
                # our output image we need to convert it to a string first
                barcode_data = barcode.data.decode("utf-8")
                barcode_type = barcode.type

                # draw the barcode data and barcode type on the image
                # text = "{} ({})".format(barcode_data, barcode_type)
                # cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                #             0.5, (0, 0, 255), 2)

                # print the barcode type and data to the terminal
                # print("Found {} barcode: {}".format(barcode_type,
                # barcode_data))
                # make sure its a devault wallet
                if "devault:" not in barcode_data:
                    not_dvt = "NOT a DeVault wallet!!!"
                    cv2.putText(frame, not_dvt, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 0, 255), 2)
                    barcodes = []

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or barcodes != []:
                break
        else:
            break

    #print("close video stream")

    cap.release()
    cv2.destroyAllWindows()

    return barcode_data
