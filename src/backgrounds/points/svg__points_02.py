import random

result = '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0" y="0" viewBox="0 0 1920 1920" xml:space="preserve">\n'

width = 1920
height = 1920
n = 300
n_lines = 600
radius_max = 15
radius_min = 5
line_width = 1
color_background = '#445a76'
color_circles = '#989898'
color_lines = '#989898'

result += '<style type="text/css">.st0{{fill:none;stroke:{};stroke-width:{};}}.st1{{fill :{};}}</style>'.format(
    color_lines, line_width,
    color_circles)
result += '<path fill="{}" d="M0 0h1920v1920H0z"/>'.format(color_background)

points = [[random.randint(radius_max, width - radius_max), random.randint(radius_max, height - radius_max)] for i in
          range(n)]

set_lines = set()
for i in range(n_lines):
    begin = random.randint(0, n - 1)
    temp_points = points.copy()


    def my_fn(s):
        d = (points[begin][0] - s[0]) ** 2 + (points[begin][1] - s[1]) ** 2
        if d == 0:
            d = width ** 2
        return d


    temp_points = sorted(temp_points, key=my_fn)

    for j in range(random.randint(1, 4)):
        begin_point = points[begin]
        if j <= 2:
            end_point = temp_points[j]
        else:
            end_point = temp_points[j+30]
        if begin_point[0] < end_point[0]:
            begin_point, end_point = end_point, begin_point
        set_lines.add(
            '<line class="st0" x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(begin_point[0], begin_point[1], end_point[0],
                                                                         end_point[1]))
result += '\n<g>\n{}\n</g>\n'.format("\n".join(set_lines))

list_circles = []
for point in points:
    r = random.randint(radius_min, radius_max)
    list_circles.append('<circle class="st1" cx="{}" cy="{}" r="{}"/>'.format(point[0], point[1], r))
result += '\n<g>\n{}\n</g>\n'.format("\n".join(list_circles))

result += "</svg>"

with open('output.svg', 'w') as file:
    file.write(result)
