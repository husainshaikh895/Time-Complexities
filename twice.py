import matplotlib.pyplot as plt

twice_value =[]
nums = []

for i in range(100):
	twice_value.append(2*i)
	nums.append(i)

plt.bar(range(len(twice_value)), list(twice_value), align='center', color='b')
plt.xticks(range(len(nums)), list(nums))
plt.xlabel("Twice_Value")
plt.ylabel("Numbers")
plt.title("Twice value Graph Visualisation")
plt.show()