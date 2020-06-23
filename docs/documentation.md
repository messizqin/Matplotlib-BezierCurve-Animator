# main
<hr />
<h2>Brezier.illustrate(fig, points, n=100, interval=100, depth=None)</h2>
<li>
* fig: plt.figure() object
</li>
<li>
* points: list object, collection of points, for example, points = [[0, 0], [3, 3], [6, 0]]
</li>
<li>
* n: int object, how many points to sketch between each two points. Notice the larger n is, the more smooth the animation will be, the more stressed the machine will be. 
</li>
<li>
* interval: int object, time in milliseconds decides how fast the motion goes. 
</li>
<li>
* depth: not required. can trigger by int object, range from a minimum of 1 to the length of the points, the smaller depth, the simpler the graph will be.  
</li>
<br /><br />

# loop
<hr />
<h2>b = Brezier(fig, points, n, interval)</h2>
<h2>b.loop(depth)</h2>
<b>It cannot be written as `Brezier(fig, points, n, interval).loop()`, if you do this, the animation will not be recorded at global level. </b>
<li>
* depth: required, can trigger by int object, range from a minimum of 1 to the length of the points, the smaller depth, the simpler the graph will be.  
</li>
<br /><br />
<ul>
<li>
* loop function basically animate vectors [left_x, left_y, right_x, right_y] into moving dots and moving lines. It goes deeper and deeper until it reaches the bottom, which it starts from 0 to the length of the points by an increment of 1.
</li>
<li> 
* self.init(): the first animation is sketching fixed growing dot and growing lines, this is when the vector_animator and line_animator still works but with left_x equal to right_x and left_y equal to right_y.
</li>
<li>
* self.run(): enumerate existing [left_x, left_y, right_x, right_y] to one by one sketch dot and line. 
</li>
<li>
* self.recurse(): empty [left_x, left_y, right_x, right], decrement self.level by one to end the while loop.
</li>
<li>
* self.store(x_res, y_res): store generated path to self.reduced, which is a dict with keys of 'x' and 'y'.   
</li>
<li>
* self.dump(): refresh self.x_on_left... with a new set of x y values stored in self.reduced
</li>
<li>
* self.clear(): empty self.reduced
</li>
</ul>

# core
<h2>vector_animate(self, left_x, left_y, right_x, right_y, color)</h2>
<hr />
<u>left args indicate initial points, right args indicate final points, in iteration of self.n, work out instaneous position</u>
<ul>
<li>
* left_x: values of initial points x
</li>
<li>
* left_y: values of initial points y
</li>
<li>
* right_x: values of final points x
</li>
<li>
* right_y: values of final points y
</li>
<li>
* color: hexvalue
</li>
</ul>
<br /><br />
<h2>line_animate(self, x_left, y_left, x_right, y_right, color)</h2>
<hr />
<u>left args indicate initial points, right args indicate final points, without any iteration, using frames to change change plotting line value</u>
<ul>
<li>
* x_left: values of initial points x
</li>
<li>
* y_left: values of initial points y
</li>
<li>
* x_right: values of final points x
</li>
<li>
* y_right: values of final points y
</li>
<li>
* color: hexvalue
</li>
</ul>

# array
<h2>Bezier.condense(two, n)</h2>
<hr />
<u>dilute two values evenly</u>
<ul>
<li>
* two: list consists of of two value, initial one and final one
</li>
<li>
* n: int, segment, what's the length of returning list 
</li>
</ul>
<br /><br />
<h2>Bezier.forward(*points)</h2>
<hr />
<u>convert points to x y values</u>
<ul>
<li>
* points: list of single points
</li>
</ul>
<br /><br />
<h2>Bezier.backward(x_, y_)</h2>
<hr />
<u>combine x y values into points</u>
<ul>
<li>
* x_: list of x values
</li>
<li>
* y_: list of y values
</li>
</ul>
<br /><br />
  
# color
<h2>c = Color(max_intensity=50, gray=False)</h2>
<u>The class contains no repeating feature, the color that exist won't show up twice</u>
<hr />
<ul>
<li>
* max_intensity: int, between 0 to 100, with lower max_intensity, will return more clear colors. however slower calculations. default to 50. 
</li>
<li>
* gray: boolean, True #=> the class only return gray values. False #=> the class return colourful hexcodes.
</li>
</ul>  
<br /><br />
<h2>c.new</h2>
<hr />
<p>Returns a new instance of no repeating color. 
<br /><br />
<h2>c.last</h2>
<hr />
<p>Returns the last generated color. 
<br /><br />


