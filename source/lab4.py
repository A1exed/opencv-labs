# Лабораторная работа № 4. Контурный анализ.
#
# 1. Реализовать методы Канни, Собеля. Применить их к тестовому изображению.
#
# 2. Сравнить результаты.
#
# 3. Реализовать морфологические операции с использованием библиотеки OpenCV.
#
# 4. Осуществить устранение шумовых точек.
#
# 5. Провести замыкание контура на изображении.
#
# 6. Залить, получившийся контур.
#
# 7. Результрующую маску применить к исходному изображению и извлечь объект из исходного изображения.
#
# 8. Написать краткий отчет по проделанной работе с использованием Jupiter notebook.

import cv2
import numpy as np


def show_img(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)


def canny(img, level):
    return cv2.Canny(img, level, 255)


def make_thresh(img):
    for i in range(20000):
        x = np.random.randint(0, img.shape[0])
        y = np.random.randint(0, img.shape[1])
        img[x][y] = 255
    return img


def sobel(img, level):
    lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    sobel_x = cv2.Sobel(l, cv2.CV_64F, 1, 0)
    sobel_y = cv2.Sobel(l, cv2.CV_64F, 0, 1)
    abs_sobel_x = np.absolute(sobel_x)
    abs_sobel_y = np.absolute(sobel_y)
    return np.uint8(cv2.threshold(abs_sobel_x + abs_sobel_y, level, 255, cv2.THRESH_BINARY)[1])


# Коррозия
def erode_morph(img, level):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (level, level))
    return cv2.erode(img, kernel)


# Открытая операция
def open_morph(img, level):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (level, level))
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


# Закрытая операция
def close_morph(img, level):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (level, level))
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


# Градиент
def grad_morph(img, level):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (level, level))
    return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


# Черная шляпа
def blackhat_morph(img, level):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (level, level))
    return cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


def connect_contour(img, level):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (level, level))
    dilated = cv2.dilate(img, kernel)
    _, cnts, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, [cnts[0]], -1, (0, 255, 0), 2)
    return img


image = cv2.imread(".\\..\\assets\\caps.jpg")

show_img("Original", image)
# show_img("Canny", canny(image, 100))
# show_img("Sobel", sobel(image, 100))
# show_img("Eroded morph", erode_morph(image, 10))
# show_img("Open morph", open_morph(image, 10))
# show_img("Close morph", close_morph(image, 10))
# show_img("Gradient morph", grad_morph(image, 10))
# show_img("Blackhat morph", blackhat_morph(image, 10))
# show_img("Thresh image", make_thresh(image))
# show_img("No thrash image", open_morph(image, 5))
show_img("Connect contour", canny(open_morph(image, 20), 200))

