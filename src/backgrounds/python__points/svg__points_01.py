import random

result = '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0" y="0" viewBox="0 0 1920 1920" xml:space="preserve">\n'

width = 1920
height = 1920
n = 100
n_lines = 200
radius_max = 10
radius_min = 5
line_width = 2
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
    end = 0
    set_lines.add(
        '<line class="st0" x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(points[begin][0], points[begin][1], points[end][0],
                                                                     points[end][1]))
result += '\n<g>\n{}\n</g>\n'.format("\n".join(set_lines))

list_circles = []
for point in points:
    r = random.randint(radius_min, radius_max)
    list_circles.append('<circle class="st1" cx="{}" cy="{}" r="{}"/>'.format(point[0], point[1], r))
result += '\n<g>\n{}\n</g>\n'.format("\n".join(list_circles))

result += "</svg>"

with open('output.svg', 'w') as file:
    file.write(result)
