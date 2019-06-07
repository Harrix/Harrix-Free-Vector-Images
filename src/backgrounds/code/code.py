from pathlib import Path

letter_height = 9
letter_width = 8
line_height = 9
margin = 10
width_fix = 512
height_fix = 512
is_fix = True
space_symbols = ' '

color_background = '#36434f'
color_code = '#999999'

file = Path("input.txt")
with open(file) as f:
    content = f.read().splitlines()

data = []

max_length = -1
for s in content:
    line = []
    if len(s) > max_length:
        max_length = len(s)
    for letter in s:
        if letter in space_symbols:
            line.append(0)
        else:
            line.append(1)
    data.append(line)

height = len(data) * letter_height + (len(data) - 1) * line_height + 2 * margin
width = max_length * letter_width + 2 * margin

if is_fix:
    height = height_fix
    width = width_fix

result = '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0" y="0" viewBox="0 0 {} {}" xml:space="preserve">\n'.format(
    width, height)

result += '<style type="text/css">.st0{{fill:{};}}</style>'.format(color_code)
result += '<path fill="{}" d="M0 0h{}v{}H0z"/>'.format(color_background, width, height)

list_rects = []

for i in range(len(data)):
    length_block = 0
    stop = False
    j_block = 0
    for j in range(len(data[i])):
        if data[i][j] == 1:
            length_block = length_block + 1
            if stop:
                j_block = j
            stop = False

        if j == len(data[i]) - 1:
            stop = True
        else:
            if data[i][j + 1] == 0:
                stop = True

        if stop and data[i][j] == 1:
            list_rects.append(
                '<rect x="{}" y="{}" class="st0" width="{}" height="{}"/>'.format(j_block * letter_width + margin, i * (
                        letter_height + line_height) + margin, letter_width * length_block, letter_height))
            length_block = 0

result += '\n<g>\n{}\n</g>\n'.format("\n".join(list_rects))

result += "</svg>"

with open('output.svg', 'w') as file:
    file.write(result)
