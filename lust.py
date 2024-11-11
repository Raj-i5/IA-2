import matplotlib.pyplot as plt
price=[2.50, 1.23, 4.02, 3.25, 5.00, 4.40]
sales=[34, 62, 49, 22, 13, 19]
plt.scatter (price, sales, c='RED', s=60, marker='D', alpha=1)
plt.title("Dataset")
plt.ylabel('price')
plt.xlabel('sales')
plt.show()