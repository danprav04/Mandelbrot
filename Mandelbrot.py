import matplotlib.pyplot as plt
import random as r
import json

path = r"path\Mandelbrot.json"
print("Loading...")
data = []
with open(path) as f:
	data = json.load(f)
data = list(data)

x = []
y = []

imag = 1.2
while imag > -1.2:
	real = -1.5
	while real < 1.2:
		i = 0
		rt = real
		it = imag
		z = (real * real) + (imag * imag)
		while z < 4 and i < 500:
			rt2 = (rt * rt) - (it * it) + real
			it = (2 * rt * it) + imag
			rt = rt2
			z = (rt * rt) + (it * it)
			i += 1

		if i > 100:
			x.append(real)
			y.append(imag)

		real += 0.000035

	print(imag)
	imag -= 0.0006

print("Saving...")
data.append((x, y))
with open(path, 'w') as json_file:
	json.dump(data, json_file)

print("Showing...")
plt.scatter(x, y, s=0.05)
plt.savefig(f'foo{r.randrange(100000)}.png', bbox_inches='tight')
plt.show()