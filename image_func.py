import numpy as np


# we need this function after every manipulation
def fix_image(img):
    # in manipulation we work with normalized images
    img *= 255
    # so pixel value can not be higher than 255 and lower than 0
    img[np.where(img > 255)] = 255
    img[np.where(img < 0)] = 0
    # also we fixing float data
    return np.array(img, dtype=np.uint8)


# linear transformation of an image
def linear_transform(img, a, b):
    result = a * img + b
    return fix_image(result)


# power transformation of an image
def power_transform(img, c, n):
    result = c * (img**n)
    return fix_image(result)


# next 16 functions are mixing 2 image by special rule
def additive_mix(img1, img2):
    result = img1 + img2
    return fix_image(result)


def subtractive_mix(img1, img2):
    result = img1 + img2 - 1
    return fix_image(result)


def difference_mix(img1, img2):
    result = np.abs(img1-img2)
    return fix_image(result)


def multiply_mix(img1, img2):
    result = img1 * img2
    return fix_image(result)


def screen_mix(img1, img2):
    result = np.ones_like(img1) - (np.ones_like(img1) - img1) * (np.ones_like(img2)-img2)
    return fix_image(result)


def negation_mix(img1, img2):
    result = np.ones_like(img1) - np.abs(np.ones_like(img1) - img1 - img2)
    return fix_image(result)


def darken_mix(img1, img2):
    result = np.zeros_like(img1)
    for color in range(3):
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                if img1[i, j, color] < img2[i, j, color]:
                    result[i, j, color] = img1[i, j, color]
                else:
                    result[i, j, color] = img2[i, j, color]

    return fix_image(result)


def lighter_mix(img1, img2):
    result = np.zeros_like(img1)
    for color in range(3):
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                if img1[i, j, color] > img2[i, j, color]:
                    result[i, j, color] = img1[i, j, color]
                else:
                    result[i, j, color] = img2[i, j, color]

    return fix_image(result)


def exclusion_mix(img1, img2):
    result = img1 + img2 - 2*img1*img2
    return fix_image(result)


def overlay_mix(img1, img2):
    result = np.zeros_like(img1)
    for color in range(3):
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                if img1[i, j, color] < 0.5:
                    result[i, j, color] = img1[i, j, color] * 2 * img2[i,j,color]
                else:
                    result[i, j, color] = 1 - 2 * (1 - img1[i,j,color]) * (1-img2[i,j,color])

    return fix_image(result)


def hard_light_mode(img1, img2):
    result = np.zeros_like(img1)
    for color in range(3):
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                if img2[i, j, color] < 0.5:
                    result[i, j, color] = img1[i, j, color] * 2 * img2[i,j,color]
                else:
                    result[i, j, color] =  1 - 2 * (1 - img1[i,j,color]) * (1-img2[i,j,color])

    return fix_image(result)


def soft_light_mode(img1,img2):
    result = np.zeros_like(img1)
    for color in range(3):
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                if img2[i, j, color] < 0.5:
                    result[i, j, color] = img1[i, j, color] * 2 * img2[i,j,color] + img1[i, j, color] **2 \
                                          * (1-2*img2[i, j, color])
                else:
                    result[i, j, color] = np.sqrt(img1[i, j, color]) * (2*img2[i, j, color])
                    + (2 * img1[i, j, color])*(1-img2[i, j, color])

    return fix_image(result)


def color_dodge_fix(img1,img2):
    result = np.zeros_like(img1)
    for color in range(3):
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                if img2[i, j, color] !=1:
                    result[i, j, color] = img1[i, j, color] /(1 - img2[i,j,color])

    return fix_image(result)


def color_burn_fix(img1,img2):
    result = np.zeros_like(img1)
    for color in range(3):
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                if img2[i, j, color] !=0:
                    result[i, j, color] = 1-(1-img1[i, j, color]) / (img2[i,j,color])

    return fix_image(result)


def reflect_fix(img1,img2):
    result = np.zeros_like(img1)
    for color in range(3):
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                if img2[i, j, color] != 1:
                    result[i, j, color] = img1[i, j, color]**2 / (1 - img2[i, j, color])

    return fix_image(result)


def opacity(img1, img2, alpha):
    result = (1-alpha)*img2 + alpha*img1
    return  fix_image(result)


