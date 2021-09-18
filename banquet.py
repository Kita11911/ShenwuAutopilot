import cv2
import numpy as np

if __name__ == "__main__":
    test_img = cv2.imread('detection_test.png', cv2.IMREAD_UNCHANGED)
    served_table_img = cv2.imread('served_table.png', cv2.IMREAD_UNCHANGED)
    sample_button_img = cv2.imread('sample_button.png', cv2.IMREAD_UNCHANGED)

#TODO: the served_table image is contaminated by the cursor and needs an update

    # cv2.imshow('Served Table', served_table_img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    # cv2.imshow('button', sample_button_img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    match_result = cv2.matchTemplate(test_img, served_table_img, cv2.TM_CCOEFF_NORMED)

    # cv2.imshow("match res", match_result)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match_result)
    print(max_loc)
    print(min_loc)
    print(min_val)
    print(max_val)
    w, h = served_table_img.shape[1], served_table_img.shape[0]
    cv2.rectangle(test_img, max_loc, (max_loc[0]+w, max_loc[1]+h), (0,255,255), 2)
    
    cv2.imshow('test', test_img)
    cv2.waitKey()
    threshold = 0.85
    yloc, xloc = np.where(match_result > threshold)
    print(len(xloc))
    print(len(yloc))
    for(x, y) in zip(xloc, yloc):
        cv2.rectangle(test_img, (x,y), (x+w, y+h), (0,255,255),2)
    rectangles = []
    for(x, y) in zip(xloc, yloc):
        rectangles.append([int(x),int(y),int(w),int(h)])
        rectangles.append([int(x),int(y),int(w),int(h)])
    print(len(rectangles))
    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    print(len(rectangles))
    for(x, y, w, h) in rectangles:
        cv2.rectangle(test_img, (x,y), (x+w, y+h), (0,255,255),2)
    cv2.imshow('test', test_img)
    cv2.waitKey()