import pandas
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

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
    x_axis_label="Organization", y_axis_label="dollars", x_range=[row[0] for row in perc.values]
)

plot.vbar(x='Organization', top='dollars', width=.5, source=src)
plot.y_range.start=0
show(plot)