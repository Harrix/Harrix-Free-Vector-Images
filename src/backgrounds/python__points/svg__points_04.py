import random

result = '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0" y="0" viewBox="0 0 1920 1920" xml:space="preserve">\n'

width = 1920
height = 1920
n = 30
radius_max = 20
color_background = '#445a76'
color_circles = '#989898'

result += '<style type="text/css">.st0{{fill :{};}}</style>'.format( color_circles)
result += '<path fill="{}" d="M0 0h1920v1920H0z"/>'.format(color_background)

list_circles =[]
for i in range(n-2):
    for j in range(n-2):
        percent = random.randint(30, 100)/100.
        opacity = percent
        r = percent * radius_max
        x = (width/(n-1))*(i+1)
        y = (height/(n-1))*(j+1)
        list_circles.append('<circle class="st0" cx="{}" cy="{}" r="{}" opacity="{}"/>'.format(x, y, r, opacity))
result += '\n<g>\n{}\n</g>\n'.format("\n".join(list_circles))

result += "</svg>"

with open('output.svg', 'w') as file:
    file.write(result)
