import cv2
import requests
import numpy as np
import os

def create_certificate(full_name, date, week):
    certificate_background = cv2.imread("with_texts_2.png")

    cv2.putText(
        certificate_background,
        full_name,
        (150, 402),  # Change these values to adjust the location
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,  # Change this value to adjust the font size
        (0, 0, 255),
        2,
    )

    cv2.putText(
        certificate_background,
        week,
        (145, 473),  # Change these values to adjust the location
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,  # Change this value to adjust the font size
        (10, 10, 10),
        2,
    )

    cv2.putText(
        certificate_background,
        date,
        (280 , 748),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 0),
        2,
    )

    filename = f"{full_name}_{date}_certificate.png"
    cv2.imwrite(filename, certificate_background)