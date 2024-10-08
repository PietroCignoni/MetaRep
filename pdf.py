import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.interpolate import InterpolatedUnivariateSpline


class ProbabilityDensityDistribution(InterpolatedUnivariateSpline):

    def __init__(self, x, y):
        spline = InterpolatedUnivariateSpline(x, y)
        norm = spline.integral(x.min(), x.max())
        self._x = x
        self._y = y / norm
        super().__init__(self._x, self._y)

    def plot(self):
        plt.plot(self._x, self._y, 'o')
        x = np.linspace(self._x.min(), self._x.max(), 250)
        plt.plot(x, self(x))

    def normalization(self):
        return self.integral(self._x.min(), self._x.max())


def Lin(x, a):
    return a*x


if __name__ == '__main__':
    x = np.linspace(0., 1., 5)
    y = Lin(x)
    plt.plot(x, y)

    pdf = ProbabilityDensityDistribution(x, y)
    x0 = 0.5
    print(np.exp(x0), pdf(x0))
    print(pdf.normalization())
    pdf.plot()
    plt.show()
