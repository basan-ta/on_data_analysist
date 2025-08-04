def pearson_cor(x,y):
    n = len(x)
    
    #calculate mean
    mean_x = sum(x)/n 
    mean_y = sum(y)/n
    #calculate std
    std_x = (sum((i-mean_x) ** 2 for i in x) / n ) ** 0.5
    std_y = (sum((i-mean_y) ** 2 for i in y) / n ) ** 0.5
    #calculate covariance 
    cov = sum((i - mean_x) * (j - mean_y) for i, j in zip(x,y)) / n
    
    # calculate Pearson correlation coefficient
    cor = cov / (std_x * std_y)
    return  cor

x = [1,3,5,7,9,11]
y = [2,4,6,8,10,15]

result = pearson_cor(x, y)
print(f"Pearson correlation is ", result)

