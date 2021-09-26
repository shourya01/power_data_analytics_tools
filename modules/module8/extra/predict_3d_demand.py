import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


county_name = "Alameda County"

df_population = pd.read_csv("population_all.csv")
df_population = df_population[["Year", county_name]]
X = df_population

df_demand = pd.read_csv("demand_all.csv")
y = df_demand[[county_name]]

linear_regression = LinearRegression()
linear_regression.fit(X, y)
y_pred = linear_regression.predict(X)


def get_slopes():
    slopes_list = linear_regression.coef_.tolist()

    slopes_str = []
    for element in slopes_list[0]:
        slopes_str.append(str(element))
    for element in slopes_str[0]:
        slopes_str.extend(element.split(','))

    return slopes_str


intercept = linear_regression.intercept_
slopes = get_slopes()

print("y = ", slopes[0], "x1 + ", slopes[1], "x2 + ", intercept[0])
slopes = linear_regression.coef_.tolist()
year_slope = slopes[0][0]
pop_slope = slopes[0][1]

xdata = X.iloc[:, 0].values
ydata = X.iloc[:, 1].values
zdata = y.values

zdata_pred = np.arange(30, dtype=float)
for i in range(0, 30):
    zdata_pred[i] = year_slope*xdata[i] + pop_slope*ydata[i] + intercept[0]

fig = plt.figure()
fig.suptitle(f"Multivariate Regression of Power Demand in {county_name}")
ax = plt.axes(projection='3d')

plt.xlabel("Year")
plt.ylabel("Population")
ax.set_zlabel("Power Demand (MW)")
ax.scatter3D(xdata, ydata, zdata, color="blue", label="Actual Demand")
ax.scatter3D(xdata, ydata, zdata_pred, color="black", label="Predicted Demand")


def plot_chart(feature_name, feature, target, target_pred, county):
    figure = plt.figure()
    figure.suptitle(f"Multivariate Regression of Power Demand in {county}")
    plt.scatter(x=feature, y=target, color="blue", label="Actual Demand")
    plt.scatter(x=feature, y=target_pred, color="black", label="Predicted Demand")
    plt.xlabel(feature_name)
    plt.ylabel("Power Demand (MW)")
    plt.legend(loc="upper left")


features_list = ["Year", "Population"]
for i in range(len(features_list)):
    plot_chart(features_list[i], X.iloc[:, i], y, y_pred, county_name)

plt.show()
