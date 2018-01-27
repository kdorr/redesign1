import pandas
from math import pi
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Range1d

#Read data
df = pandas.read_csv("data.csv")

#Percentages
sum = df['dollars'].sum()
perc = df
perc['dollars'] = df['dollars']/sum

#Format data
#src = ColumnDataSource(df)
perc = perc.sort_values('dollars', ascending=False)
src = ColumnDataSource(perc)
#Setup plot
plot = figure(
    plot_width=600, plot_height=600, x_axis_label="Organization", y_axis_label="percentage of funding", x_range=[row[0] for row in perc.values], y_range=Range1d(0,1)
)

plot.vbar(x='Organization', top='dollars', width=.5, source=src)
plot.yaxis.bounds=(0,1)
plot.xaxis.major_label_orientation = pi/2
show(plot)