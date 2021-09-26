import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


counties_drop_list = ["Year", "Los Angeles County", "Merced County", "Riverside County", "San Diego County", "San Mateo County", "Santa Barbara County", "Santa Clara County", "Santa Cruz County"]

df = pd.read_csv("population_all.csv")
df = pd.concat([pd.Series(1, index=df.index, name="00"), df], axis=1)
X_global = df.drop(columns=counties_drop_list[1:])

df_demand = pd.read_csv("demand_all.csv")
y_global = df_demand.drop(columns=counties_drop_list)

#for i in range(1, len(X.columns)):
#    X[i-1] = X[i-1]/np.max(X[i-1])
#print(X.head())

theta_global = np.array([0]*len(X_global.columns))
m_global = len(X_global)


def hypothesis(theta, X):
    return theta*X


def computeCost(X, y, theta, m):
    y1 = hypothesis(theta, X)
    y1 = np.sum(y1, axis=1)
    return (sum((y1.sub(y.squeeze()))**2))/(2*m)


def gradientDescent(X, y, theta, m, alpha, i):
    J = []  #cost function in each iterations
    k = 0
    while k < i:
        y1 = hypothesis(theta, X)
        y1 = np.sum(y1, axis=1)
        for c in range(0, len(X.columns)):
            theta[c] = theta[c] - alpha*(sum((y1.sub(y.squeeze()))*X.iloc[:,c]))/m
            print(theta[c])
        j = computeCost(X, y, theta, m)
        J.append(j)
        k += 1
        print(J, j, theta)
    return J, j, theta


J, j, theta_global = gradientDescent(X_global, y_global, theta_global, m_global, 0.05, 10000)

y_hat = hypothesis(theta_global, X_global)
y_hat = np.sum(y_hat, axis=1)

plt.figure()
plt.scatter(x=list(range(0, m_global)), y=y_global, color='blue')
plt.figure()
plt.scatter(x=list(range(0, m_global)), y=y_hat, color='black')
plt.show()
