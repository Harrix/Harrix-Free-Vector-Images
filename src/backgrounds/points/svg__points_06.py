import random

result = '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0" y="0" viewBox="0 0 1920 1920" xml:space="preserve">\n'

width = 1920
height = 1920
d = 20
radius = 3
color_background = '#f8f8f8'
color_circles = '#dddddd'

n = int(width / d - 1)

result += '<style type="text/css">.st0{{fill :{};}}</style>'.format(color_circles)
result += '<path fill="{}" d="M0 0h1920v1920H0z"/>'.format(color_background)

list_circles = []
for i in range(n):
    for j in range(n):
        x = (width / (n + 1)) * (i + 1)
        y = (height / (n + 1)) * (j + 1)
        list_circles.append('<circle class="st0" cx="{}" cy="{}" r="{}"/>'.format(x, y, radius))
result += '\n<g>\n{}\n</g>\n'.format("\n".join(list_circles))

result += "</svg>"

with open('output.svg', 'w') as file:
    file.write(result)
