from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import choice, randint


class Color:
    refer = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
             10: "A",  11: "B",  12: "C",  13: "D",  14: "E",  15: "F",  16: "G"}

    def __init__(self, max_intensity=50, gray=False):
        if max_intensity < 20:
            self.const = 20
        else:
            self.const = (max_intensity / 100.0) * 6 * 16
        self.exist = []
        self.gray = gray
        self.ind = 14

    @staticmethod
    def generate():
        sa = 0
        arr = []
        for i in range(6):
            ind = choice([x for x in range(16)])
            arr.append(Color.refer[ind])
            sa += ind
        return sa, arr

    def gray_new(self):
        if self.ind < 0:
            self.ind = 14
        self.ind -= 1
        res = f"#{''.join([Color.refer[self.ind] for i in range(6)])}"
        self.exist.append(res)
        return res

    @property
    def new(self):
        if self.gray is True:
            return self.gray_new()
        sa, arr = Color.generate()
        while sa >= self.const or arr in self.exist:
            sa, arr = Color.generate()
        res = f'#{"".join(arr)}'
        self.exist.append(res)
        return res

    @property
    def last(self):
        return self.exist[-1]


class Bezier:
    @staticmethod
    def condense(two, n):
        fir = two[0]
        sec = two[1]
        par = float((sec - fir) / (n - 1))
        sta = 0
        arr = []
        for i in range(n):
            arr.append(fir + sta)
            sta += par
        return arr

    @staticmethod
    def forward(*points):
        x_ = []
        y_ = []
        for i in points:
            x_.append(i[0])
            y_.append(i[1])
        return x_, y_

    @staticmethod
    def backward(x_, y_):
        points = []
        for i, d in enumerate(x_):
            points.append([d, y_[i]])
        return points

    def __init__(self, fig, points, n, interval):
        self.fig = fig
        self.points = points
        self.n = n
        self.level = len(points)
        self.animate = {}
        self.interval = interval
        self.fr = [i for i in range(n)]
        self.x_on_left = []
        self.x_on_right = []
        self.y_on_left = []
        self.y_on_right = []
        self.inited = False
        self.reduced = {"x": [], "y": []}
        self.color = Color(max_intensity=50)
        self.gray = Color(gray=True)

    def store(self, x_res, y_res):
        self.reduced['x'].append(x_res)
        self.reduced['y'].append(y_res)

    def dump(self):
        for i, l_x in enumerate(self.reduced['x']):
            if i != len(self.reduced['x']) - 1:
                self.x_on_left.append(l_x)
                self.y_on_left.append(self.reduced['y'][i])
                self.x_on_right.append(self.reduced['x'][i + 1])
                self.y_on_right.append(self.reduced['y'][i + 1])

    def clear(self):
        self.reduced = {"x": [], "y": []}

    def recurse(self):
        self.level -= 1
        self.x_on_left = []
        self.x_on_right = []
        self.y_on_left = []
        self.y_on_right = []

    def add_animate(self, level, animation):
        try:
            self.animate[level].append(animation)
        except KeyError:
            self.animate[level] = [animation]

    def vector_animate(self, left_x, left_y, right_x, right_y, color):
        def update(frame):
            if frame != 0:
                plt.plot([x_res[frame - 1], x_res[frame]], [y_res[frame - 1], y_res[frame]], color=color)
            p.set_data(x_res[frame], y_res[frame])
            return p,

        def init():
            p.set_data(x_res[0], y_res[0])
            return p,

        x_res = []
        y_res = []
        for i in range(self.n):
            x_res.append(left_x[i] + ((right_x[i] - left_x[i]) * float(i / (self.n - 1))))
            y_res.append(left_y[i] + ((right_y[i] - left_y[i]) * float(i / (self.n - 1))))

        self.store(x_res, y_res)
        p, = plt.plot(x_res[0], y_res[0], "o", color=color)

        return FuncAnimation(fig=self.fig, func=update, init_func=init, frames=self.fr,
                             interval=self.interval, repeat=False)

    def line_animate(self, x_left, y_left, x_right, y_right, color):
        p, = plt.plot([x_left[0], x_right[0]], [y_left[0], y_right[0]], color=color)

        def update(frame):
            p.set_data([x_left[frame], x_right[frame]], [y_left[frame], y_right[frame]])
            return p,

        def init():
            p.set_data([x_left[0], x_right[0]], [y_left[0], y_right[0]])
            return p,

        return FuncAnimation(fig=self.fig, func=update, init_func=init, frames=self.fr,
                             interval=self.interval, repeat=False)

    def init(self):
        self.inited = True
        for i, d in enumerate(self.points):
            if i != self.level - 1:
                xys_ = Bezier.forward(d, self.points[i + 1])
                x_ = Bezier.condense(xys_[0], self.n)
                y_ = Bezier.condense(xys_[1], self.n)
                self.x_on_left.append(x_)
                self.x_on_right.append(x_)
                self.y_on_left.append(y_)
                self.y_on_right.append(y_)

    def run(self):
        for i, l_x in enumerate(self.x_on_left):
            x_l = self.x_on_right[i]
            l_y = self.y_on_left[i]
            y_l = self.y_on_right[i]
            if isinstance(self.color, Color):
                self.add_animate(self.level, self.vector_animate(l_x, l_y, x_l, y_l, self.color.new))
                self.add_animate(self.level, self.line_animate(l_x, l_y, x_l, y_l, self.color.last))
            else:
                self.add_animate(self.level, self.vector_animate(l_x, l_y, x_l, y_l, self.color))
                self.add_animate(self.level, self.line_animate(l_x, l_y, x_l, y_l, self.color))

    def loop(self, depth):
        lk = 0
        if not self.inited:
            self.init()
        while self.level != 0:
            self.run()
            self.recurse()
            self.dump()
            self.clear()
            lk += 1
            if lk == depth:
                return


def illustrate(fig, points, n=100, interval=100, depth=None, color=None):
    be = Bezier(fig, points, n, interval)
    if color is not None:
        be.color = color
    be.loop(depth)
    return be


if __name__ == '__main__':
    def example(lim_x, lim_y, n):
        dx = float((lim_x[1] - lim_x[0]) / n)
        x_arr = []
        y_arr = []
        for i in range(n + 1):
            x_arr.append(lim_x[0] + dx * i)
            y_arr.append(randint(int(lim_y[0]), int(lim_y[1])))
        return x_arr, y_arr

    fig = plt.figure()
    x_lim = (-20, 20)
    y_lim = (-20, 20)
    plt.xlim(*x_lim)
    plt.ylim(*y_lim)
    points = Bezier.backward(*example(x_lim, y_lim, 3))
    b = illustrate(fig, points, interval=50, n=100, depth=4)
    plt.show()


