import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as spi
import math

# 显示中文和负数
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("微分方程")
        self.setGeometry(200, 200, 640, 400)

        m = Interpolation(self, width=5, height=4)  # 实例化一个画布对象
        m.move(0, 0)

        # 设置原始图像按钮
        button = QPushButton('原始图像', self)
        button.move(520, 20)
        button.resize(100, 75)
        button.clicked.connect(m.main)

        # 设置直接欧拉法按钮
        button = QPushButton('直接欧拉法', self)
        button.move(520, 115)
        button.resize(100, 75)
        button.clicked.connect(m.euler)

        # 设置改进欧拉法按钮
        button = QPushButton('改进欧拉法', self)
        button.move(520, 210)
        button.resize(100, 75)
        button.clicked.connect(m.mproveeuler)

        # 设置四阶龙格库塔按钮
        button = QPushButton('四阶龙格库塔', self)
        button.move(520, 305)
        button.resize(100, 75)
        button.clicked.connect(m.rungeKutta)
        self.show()


# 插值方法类
class Interpolation(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.x0 = 0
        self.h = 0.1
        self.x = np.linspace(0, 2)
        self.y = [self.func(i) for i in self.x]
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        # 初始图像
        # self.main()

    # 初始函数
    def func(self, x):
        y = 1 / (2 * math.e ** x - x - 1)
        return y

    # 微分方程
    def f(self, x, y):
        return (-y - x * y * y)

    # 直接欧拉法，初值，步长 两个参数
    def euler(self):
        y = []
        y.append(self.func(self.x0))
        x = [self.x0]
        n = 2 / self.h
        for i in range(int(n)):
            x.append(x[-1] + self.h)
            y.append(y[-1] + self.h * self.f(x[i], y[i]))
        # return (x,y)
        # x,y=self.euler()
        self.axes.plot(x, y, ':', label='直接欧拉法')
        self.axes.legend()  # 默认右上角
        self.draw()

    # 改进欧拉法 初值，步长 两个参数
    def mproveeuler(self):
        yp = []
        yc = []
        y = []
        y.append(self.func(self.x0))
        x = [self.x0]
        n = 2 / self.h
        for i in range(int(n)):
            x.append(x[-1] + self.h)
            yp.append(y[-1] + self.h * self.f(x[i], y[i]))
            yc.append(y[-1] + self.h * self.f(x[i + 1], yp[-1]))
            y.append((yp[-1] + yc[-1]) / 2)
        # return (x,y)
        # x,y=self.euler()
        self.axes.plot(x, y, ':', label='改进欧拉法')
        self.axes.legend()  # 默认右上角
        self.draw()

    # 经典四阶龙格库塔法 初值，步长 两个参数
    def rungeKutta(self):
        k1 = []
        k2 = []
        k3 = []
        k4 = []
        y = []
        y.append(self.func(self.x0))
        x = [self.x0]
        n = 2 / self.h
        for i in range(int(n)):
            x.append(x[-1] + self.h)
            k1.append(self.f(x[i], y[i]))
            k2.append(self.f(x[i] + self.h / 2, y[i] + self.h / 2 * k1[-1]))
            k3.append(self.f(x[i] + self.h / 2, y[i] + self.h / 2 * k2[-1]))
            k4.append(self.f(x[i + 1], y[i] + self.h * k3[-1]))
            y.append(y[-1] + self.h / 6 * (k1[-1] + 2 * k2[-1] + 2 * k3[-1] + k4[-1]))
        # return (x,y)
        # x,y=self.rungeKutta()
        self.axes.plot(x, y, ':', label='四阶龙格库塔')
        self.axes.legend()  # 默认右上角
        self.draw()

    # 绘制原始图像
    def main(self):

        # 绘图
        self.axes.plot(self.x, self.y, 'purple', label="原始图像")
        self.axes.legend()  # 默认右上角
        self.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
