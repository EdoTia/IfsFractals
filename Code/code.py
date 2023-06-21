import numpy as np
from PIL import Image
import random
import queue
from Christmas_tree import *

x_im = 540
y_im = 540


def minmax():
    z = [0, 0]
    xa, xb, ya, yb = 0, 0, 0, 0
    for k in range(0, x_im * y_im):
        i = 0
        p = random.random()
        psum = 0.0
        while i < NumS - 1:
            psum = psum + pr[i]
            if p <= psum:
                break
            i = i + 1
        v = [a[i] * z[0] + b[i] * z[1] + e[i], c[i] * z[0] + d[i] * z[1] + f[i]]
        if v[0] < xa:
            xa = v[0]
        if v[1] < ya:
            ya = v[1]
        if v[0] > xb:
            xb = v[0]
        if v[1] > yb:
            yb = v[1]
        z = v
    return xa, ya, xb, yb


def rescaling(xa, xb, ya, yb):
    if abs(xb - xa) < 1:
        rx = 1
    else:
        rx = xb - xa
    if abs(yb - ya) < 1:
        ry = 1
    else:
        ry = yb - ya
    return rx, ry


def attractor(iteration):
    matrix = np.zeros((x_im, y_im, 3), dtype="uint8")
    xa, ya, xb, yb = minmax()
    rx, ry = rescaling(xa, xb, ya, yb)
    z = [0, 0]
    p = [int(z[0] - xa * x_im / rx), int(z[1] - ya * y_im / ry)]
    matrix[p[0], p[1]] = (255, 255, 255)
    q = queue.Queue()
    q.put(z)
    it = 0
    while q.empty() is False and it < iteration:
        y = q.get()
        for i in range(0, NumS):
            y1 = [a[i] * y[0] + b[i] * y[1] + e[i], c[i] * y[0] + d[i] * y[1] + f[i]]
            p1 = [int(y1[0] * x_im / rx - xa * x_im / rx),
                  int(y1[1] * y_im / ry - ya * y_im / ry)]
            try:
                matrix[p1[0], p1[1]]
            except IndexError:
                if y1[0] < xa:
                    xa = y1[0]
                if y1[0] > xb:
                    xb = y1[0]
                if y1[1] < ya:
                    ya = y1[1]
                if y1[1] > yb:
                    yb = y1[1]
                rx = xb - xa
                ry = yb - ya
                p1 = [int(y1[0] * (x_im - 1) / rx - xa * (x_im - 1) / rx),
                      int(y1[1] * (y_im - 1) / ry - ya * (y_im - 1) / ry)]
            finally:
                if matrix[p1[0], p1[1], 0] != 255:
                    q.put(y1)
                    matrix[p1[0], p1[1]] = (255, 255, 255)
        it = it + 1
    q.queue.clear()
    return matrix


if __name__ == "__main__":
    im = Image.fromarray(attractor(100000))
    im = im.rotate(90)
    im.save("Christmas_tree.jpg")
