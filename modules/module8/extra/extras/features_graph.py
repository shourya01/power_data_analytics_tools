import csv
import matplotlib.pyplot as plt
import numpy as np


def read_csv(filename):
    with open(filename) as csvfile: # same location as data3.csv
        datareader = csv.reader(csvfile, delimiter=',')
        years = []
        counties = []
        num_counties = len(next(datareader)) - 1 # calculate number of columns
        #csvfile.seek(0) # reset dataset after the next(...) function call

        for i in range(num_counties):
            counties.append([])
        for row in datareader:
            years.append(float(row[0]))
            for i in range(num_counties):
                counties[i].append(float(row[i+1]))

        returned_values = []
        returned_values.append(years)
        for i in range(num_counties):
            returned_values.append(counties[i])

    return returned_values


def create_regression(years, county):
    n = len(years)
    sum_x = 0
    sum_y = 0
    sum_xx = 0
    sum_xy = 0

    for i in range(n):
        x = years[i]
        y = county[i]
        sum_x += x
        sum_y += y
        xx = x * x
        sum_xx += xx
        xy = x * y
        sum_xy += xy

    result = []
    s_xy = (n * sum_xy) - (sum_x * sum_y)
    s_xx = (n * sum_xx) - (sum_x * sum_x)
    result.append(s_xy / s_xx) # slope

    x_avg = sum_x / n
    y_avg = sum_y / n
    result.append(y_avg - result[0] * x_avg) # y-intercept

    y1 = (result[0] * years[0]) + result[1]
    y2 = (result[0] * years[len(years) - 1]) + result[1]

    return y1, y2


def plot_points(county_name, pop, rev, dem):
    xpoints = np.array(years)
    pop_points = np.array(pop)
    rev_points = np.array(rev)
    dem_points = np.array(dem)

    figure = plt.figure()
    figure.suptitle(f"Features in {county_name}")

    ax = plt.subplot(3, 1, 1)
    ax.axes.get_xaxis().set_visible(False)
    plt.ylabel("Population (in millions)")
    plt.scatter(xpoints, pop_points)
    regression = create_regression(years, pop)
    plt.plot([years[0], years[len(years) - 1]], [regression[0], regression[1]])

    ax = plt.subplot(3, 1, 2)
    ax.axes.get_xaxis().set_visible(False)
    plt.ylabel("Revenue Per Capita ($)")
    plt.scatter(xpoints, rev_points)
    regression = create_regression(years, rev)
    plt.plot([years[0], years[len(years) - 1]], [regression[0], regression[1]])

    plt.subplot(3, 1, 3)
    plt.xlabel("Year (1990-2019)")
    plt.ylabel("Power Demand (MW)")
    plt.scatter(xpoints, dem_points)
    regression = create_regression(years, dem)
    plt.plot([years[0], years[len(years) - 1]], [regression[0], regression[1]])


values_pop = read_csv("population_all.csv")
values_rev = read_csv("revenue_all.csv")
values_dem = read_csv("demand_all.csv")

years = values_pop[0]
county_names = ["Alameda", "Los Angeles", "Merced", "Riverside", "San Diego", "San Mateo", "Santa Barbara", "Santa Clara", "Santa Cruz"]

for i in range(1, 9):
    plot_points(county_names[i-1], values_pop[i], values_rev[i], values_dem[i])

plt.show()
