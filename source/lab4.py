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


def sobel(img, level):
    lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    sobel_x = cv2.Sobel(l, cv2.CV_64F, 1, 0)
    sobel_y = cv2.Sobel(l, cv2.CV_64F, 0, 1)
    abs_sobel_x = np.absolute(sobel_x)
    abs_sobel_y = np.absolute(sobel_y)
    return np.uint8(cv2.threshold(abs_sobel_x + abs_sobel_y, level, 255, cv2.THRESH_BINARY)[1])


image = cv2.imread(".\\..\\assets\\caps.jpg")

show_img("Original", image)
show_img("Canny", canny(image, 100))
show_img("Sobel", sobel(image, 100))
