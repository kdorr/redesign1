import pandas
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

#Read data
df = pandas.read_csv("data.csv")

#Format data
src = ColumnDataSource(df)

#Setup plot
plot = figure(
    x_axis_label="Organization", y_axis_label="dollars", x_range=[row[0] for row in df.values]
)

plot.vbar(x='Organization', top='dollars', width=.5, source=src)
plot.y_range.start=0
show(plot)