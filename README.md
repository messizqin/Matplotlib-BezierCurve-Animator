<h1>Matplotlib Bezier Curve Animator</h1>
<hr />
Python 3.7.3<br />
Matplotlib 3.2.1<br />
<br />
Data science application for free distribution<br />
<b>Illustrate motion of bezier curve based on given points</b>
<br /><br />
<h1>Output</h1>
<hr />
<h3><u>Bezier Curve Level 2</u></h3>

![l2](https://github.com/Weilory/Matplotlib-BezierCurve-Animator/blob/master/docs/gif/level2.gif)

<h3><u>Bezier Curve Level 3</u></h3>

![l3](https://github.com/Weilory/Matplotlib-BezierCurve-Animator/blob/master/docs/gif/level3.gif)

<h3><u>Bezier Curve Level 7</u></h3>

![l7](https://github.com/Weilory/Matplotlib-BezierCurve-Animator/blob/master/docs/gif/level7.gif)

<h3><u>Bezier Curve Level 12</u></h3>

![l12](https://github.com/Weilory/Matplotlib-BezierCurve-Animator/blob/master/docs/gif/level12.gif)

<br /><br />
<h1>Requirements</h1>
<hr />
<ol>
  <li>Lang: None</li>
  <li>Python 3 installed</li>
  <li>Matplotlib installed</li>
</ol>
<br /><br />
<h1>Usage</h1>
<hr />

<b>Illustrate all animation of a bezier curve</b>

```
from matplotlib import pyplot as plt
from bezier import illustrate

fig = plt.figure()

points = [[0, 0], [3, 3], [6, 0]]
b = illustrate(fig, points, interval=50, n=100)

plt.show()
```

<b>Sketch a bezier curve</b>

```
from matplotlib import pyplot as plt
from bezier import sketch

fig = plt.figure()
plt.xlim(-1, 11)
plt.ylim(-2, 8)
b = sketch(fig, [[0, 0], [5, 5], [10, 0]], color='b')
plt.show()
```

<b>Moving line, moving dot motion</b>

```
from matplotlib import pyplot as plt
from bezier import Bezier
import numpy as np

fig = plt.figure()
plt.xlim(0, 10)
plt.ylim(0, 10)
left_x = np.linspace(2, 8, 100)
left_y = [8 for x in range(100)]
right_x = np.linspace(2, 8, 100)
right_y = [2 for x in range(100)]
b = Bezier(fig)
a1 = b.vector_animate(left_x, left_y, right_x, right_y, color='k', no_line=True)
a2 = b.line_animate(left_x, left_y, right_x, right_y, color='b')
plt.show()
```

<br /><br />
<h1>Feature</h1>
<hr />
<ol>
  <li>Animate points transformation</li>
</ol>
<br /><br />
<h1>Limitations</h1>
<hr />
<ol>
  <li>Don't pass in too much points, a number between 2 to 10 will be fine, any larger number may cause your machine overstressed</li>
</ol>
<br /><br />
