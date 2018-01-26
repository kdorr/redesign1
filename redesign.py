import pandas
from bokeh.plotting import figure, show
from bokeh.models import FactorRange
from bokeh.models import ColumnDataSource
import csv

df = pandas.read_csv("data.csv")
#print(df["dollars"])



data = []
with open("data.csv", "r") as csvfile:
    for line in csvfile:
        data.append(line.strip().split(','))
    csvfile.close()

#xdata = [row[0] for row in data]
#ydata = [row[1] for row in data]

src = ColumnDataSource(df)
plot = figure(
    x_axis_label="Organization", y_axis_label="dollars", x_range=[row[0] for row in df.values]
)

plot.vbar(x='Organization', top='dollars', width=.5, source=src)
plot.y_range.start=0

#
#csv
#
#plot = figure(
#    x_axis_label="Organization", y_axis_label="dollars", x_range=xdata
#)

#plot.vbar(x=xdata, width=.5, top=ydata)

#plot.y_range.start = 0

show(plot)