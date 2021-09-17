import cv2
import numpy as np




if __name__ == "__main__":
    served_table_img = cv2.imread('served_table.png', cv2.IMREAD_UNCHANGED)
    sample_button_img = cv2.imread('sample_button.png', cv2.IMREAD_UNCHANGED)

    cv2.imshow('Served Table', served_table_img)

    # cv2.imshow('button', sample_button_img)