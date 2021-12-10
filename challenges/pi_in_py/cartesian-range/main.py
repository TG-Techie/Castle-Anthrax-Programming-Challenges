import math

approx_pi = lambda res: 4 * sum ( # the dumb way
    math.sqrt(1-(2*x/res) ** 2)
    for x in range(-res//2, res//2)
)

pi_estimate = approx_pi(10_000)

print(f'Pi estimated at {pi_estimate} from {filename}.')
print(f'Percent error from true pi is {100 * abs((pi_estimate - math.pi) / math.pi)}%')
