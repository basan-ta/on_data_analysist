def calculate_pearson(x,y):
    return x,y

x = [1,3,5,7,9,11]
y = [2,4,6,8,10,12]

result = calculate_pearson(x, y)
print(f"X and y are :", result)

#Formula to calculate Pearson correlation coefficient:
#cov(x,y) / (std(x) * std(y))
#cov(x,y) = sun((x- x.mean) * (y - y.mean)) / n
#std(x) = ( sum((x-x.mean) **2) /n ) ** 0.5
#std(y) = (sum((y-y.mean) **2) / N )n ** 0.5

