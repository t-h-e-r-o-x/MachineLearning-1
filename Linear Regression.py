x = [1,2,3,4]
y = [1,2,3,4]


x_test = [5,6]
y_test = [5, 6]

import numpy as np
x = np.array(x)
y = np.array(y)

m = ((np.mean(x*y) - (np.mean(x)*np.mean(y))))/(np.mean(x*x) - (np.mean(x)*np.mean(x)))
c = np.mean(y) - m*np.mean(x)

correct, total = 0, 0
for i in range(0,len(x_test)):
    y_pred = m * x_test[i] + c
    if(y_pred == y_test[i]):
        correct += 1
    total += 1
print(correct/total*100)

