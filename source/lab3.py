# Лабораторная работа № 3. Обработка изображений в цветовых каналах.
#
# 1. К тестовому изображению применить кривые различной формы для выделения объектов разной интенсивности.
#
# 2. Реализовать автоконтраст по всему изображению и по отдельным цветовым компонентам.
#
# 3. Создать произвольные кривые преобразования, применить их к изображению.
#
# 4. Провести интерпретацию полученного результата.
#
# 5. Осуществить перевод тестового изображения в цветовые пространства HSL, Lab, XYZ.
#
# 6. В пространстве HSL осуществить выделение красных объектов путем цветовой сегментации.
#
# 7. Написать краткий отчет по проделанной работе с использованием Jupiter notebook.

import cv2
import numpy as np


def draw_contours(img, deep_lvl):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, threshold = cv2.threshold(gray, deep_lvl, 255, 0)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 255), 2)
    cv2.imshow("Contoured", img)
    cv2.waitKey(0)


def contrast(img, value):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=value, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    cv2.imshow("Contrasted", final)
    cv2.waitKey(0)


def contrast_component(img):
    b0, g0, r = cv2.split(img)
    r1 = np.zeros(np.shape(img), np.uint8)
    r1[:, :, 2] = r
    lab = cv2.cvtColor(r1, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    b, g, r = cv2.split(final)
    img = cv2.merge((b0, g0, r))
    cv2.imshow("Contrasted RED channel", img)
    cv2.waitKey(0)


def transform(img):
    b, g, r = cv2.split(img)
    img = cv2.merge((b * 3, g * 2, r * 4))
    cv2.imshow("Transformed", img)
    cv2.waitKey(0)


def red_detect(img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    red_low = np.array([0, 100, 0])
    red_high = np.array([10, 255, 255])
    red_low2 = np.array([160, 40, 40])
    red_high2 = np.array([180, 255, 255])
    curr_mask = cv2.inRange(hsv_img, red_low, red_high)
    curr_mask2 = cv2.inRange(hsv_img, red_low2, red_high2)
    hsv_img[curr_mask > 0] = ([75, 255, 200])
    hsv_img[curr_mask2 > 0] = ([75, 255, 200])
    rgb = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    ret, threshold = cv2.threshold(gray, 200, 255, 0)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (255, 0, 0), 2)
    cv2.imshow("RED contoured", img)
    cv2.waitKey(0)


image = cv2.imread(".\\..\\assets\\caps.jpg")
image1 = cv2.imread(".\\..\\assets\\caps.jpg")
image2 = cv2.imread(".\\..\\assets\\taxi-1932107_640.jpg")
image3 = cv2.imread(".\\..\\assets\\taxi-1932107_640.jpg")
image4 = cv2.imread(".\\..\\assets\\taxi-1932107_640.jpg")
image5 = cv2.imread(".\\..\\assets\\taxi-1932107_640.jpg")
image6 = cv2.imread(".\\..\\assets\\red.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)
draw_contours(image1, 150)
contrast(image2, 3.0)
contrast_component(image3)
transform(image4)
cv2.imshow("HSV", cv2.cvtColor(image5, cv2.COLOR_BGR2HSV))
cv2.waitKey(0)
cv2.imshow("LAB", cv2.cvtColor(image5, cv2.COLOR_BGR2LAB))
cv2.waitKey(0)
cv2.imshow("XYZ", cv2.cvtColor(image5, cv2.COLOR_BGR2XYZ))
cv2.waitKey(0)
red_detect(image6)
