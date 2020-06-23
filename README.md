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

![image](https://github.com/Weilory/matplotlib-bezier-curve-animator/blob/master/docs/gif/level2.gif)

<h3><u>Bezier Curve Level 3</u></h3>

![image](https://github.com/Weilory/matplotlib-bezier-curve-animator/blob/master/docs/gif/level3.gif)

<h3><u>Bezier Curve Level 7</u></h3>

![image](https://github.com/Weilory/matplotlib-bezier-curve-animator/blob/master/docs/gif/level7.gif)

<h3><u>Bezier Curve Level 12</u></h3>

![image](https://github.com/Weilory/matplotlib-bezier-curve-animator/blob/master/docs/gif/level12.gif)

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

```
from matplotlib import pyplot as plt
from bezier import illustrate

fig = plt.figure()

points = [[0, 0], [3, 3], [6, 0]]
b = illustrate(fig, points, interval=50, n=100)

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
