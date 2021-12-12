import json
import random as r
import matplotlib.pyplot as plt

path = r"path\Mandelbrot.json"
print("Loading...")

data = []
with open(path) as f:
	data = json.load(f)
data = list(data)

print(f"There are {len(data)} graphs.")
place = int(input("Which one do you want to show?\n")) - 1

x = data[place][0]
y = data[place][1]
plt.scatter(x, y, s=0.1)
plt.savefig(f'foo{r.randrange(100000)}.png', bbox_inches='tight')
plt.show()