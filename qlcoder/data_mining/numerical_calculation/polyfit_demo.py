import numpy as np
import urllib2
from io import StringIO


def demo_polyfit0():
    x, y = np.loadtxt('stock.txt', unpack=True)
    print '-'.join(map(str, np.polyfit(x, y, 1)))


def demo_polyfit1():
    d = urllib2.urlopen("http://www.qlcoder.com/download/145622513871043.txt").read().decode("utf-8")
    print d
    arr = np.genfromtxt(StringIO(d), delimiter=" ")
    z1 = np.polyfit(arr[:, 0], arr[:, 1], 5)
    print z1


if __name__ == '__main__':
    demo_polyfit0()
    demo_polyfit1()
