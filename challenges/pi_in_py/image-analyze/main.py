import imageio
import math # using pi for calculating percent error at the end

filename = 'Black_Circle.jpg'
circle_img = imageio.imread(filename)

def is_black(color):
    # rough estimate for whether a color is black-ish
    return sum(color) < 384

total_black = sum(sum(is_black(cell) for cell in row) for row in circle_img)
side_length = circle_img.shape[0] # should be square

pi_estimate = total_black / ((0.5 * side_length) ** 2) # see if you can find out why this works

print(f'Pi estimated at {pi_estimate} from {filename}.')
print(f'Percent error from true pi is {100 * abs((pi_estimate - math.pi) / math.pi)}%')
