import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

iris.head()
species_list = iris["species"].drop_duplicates().to_list()
species_color = dict(zip(species_list, ["red", "blue", "green"]))

fig_hist = plt.figure(figsize=(8.0, 6.0))
fig_hist.subplots_adjust(hspace=0.4, right=0.8)
axes_hist = fig_hist.subplots(2, 2)

for i, axes_rows in enumerate(axes_hist):
    for j, axis in enumerate(axes_rows):
        for species, color in species_color.items():
            axis_index = i * len(axes_hist) + j
            column = iris[iris["species"] == species].iloc[:, axis_index]
            axis.hist(column, bins=20, range=(iris.iloc[:, axis_index].min(), iris.iloc[:, axis_index].max()), color=color, alpha=0.75)
        axis.set_title(column.name)

fig_hist.legend(species_list, loc="right")

fig_hist.show()

fig_scat = plt.figure(figsize=(10.0, 4.0))
fig_scat.subplots_adjust(right=0.8)
axes_scat = fig_scat.subplots(1, 2)

for j, (axis, iris_type) in enumerate(zip(axes_scat, ["sepal", "petal"])):
    for species, color in species_color.items():
        axis_index = i * len(axes_scat) + j
        df = iris[iris["species"] == species].filter(like=iris_type, axis=1)
        axis.scatter(df.iloc[:, 0], df.iloc[:, 1], color=color)
        axis.set_xlabel(df.iloc[:, 0].name)
        axis.set_ylabel(df.iloc[:, 1].name)
    # axis.set_title(column.name)

df = iris[iris["species"] == "setosa"].filter(like="sepal", axis=1)
df.iloc[:, 0]


fig_scat.legend(species_list, loc="right")
fig_scat.show()