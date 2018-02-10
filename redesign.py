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
    plot_width=600, plot_height=600,
    x_axis_label="Percentage of Funding", y_axis_label="Organization",
    x_range=Range1d(0,1), y_range=[row[0] for row in perc.values]
)

plot.hbar(y='Organization', height=.5, right='dollars', left=0, source=src)
show(plot)