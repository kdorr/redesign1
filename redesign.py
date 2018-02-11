import pandas
from math import pi
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Range1d, NumeralTickFormatter
from bokeh.layouts import gridplot

#Read data
df = pandas.read_csv("data.csv")

#Raw data
raw = df
raw = raw.sort_values('dollars', ascending=False)
raw_src = ColumnDataSource(raw)

raw_plot = figure(
    plot_width=600, plot_height=600,
    title="Tier One Organization Budget Breakdown (raw numbers)",
    x_axis_label="Funding (in dollars)", y_axis_label="Organization",
    x_range=Range1d(0, 170000), y_range=[row[0] for row in raw.values]
)
raw_plot.hbar(y='Organization', left=0, right='dollars',
              height=.5, color="#718dbf",
              source=raw_src)
raw_plot.xaxis[0].formatter = NumeralTickFormatter(format="$0,000")

#Percentages
sum = df['dollars'].sum()
perc = df
perc['dollars'] = df['dollars']/sum
perc['remainder'] = 1 - df['dollars']
perc = perc.sort_values('dollars', ascending=False)
src = ColumnDataSource(perc)

#Setup plot
perc_plot = figure(
    plot_width=600, plot_height=600,
    title="Percentage of Tier One Budget by Organization",
    x_axis_label="Percentage of Whole Tier One Budget", y_axis_label="Organization",
    x_range=Range1d(0,1), y_range=[row[0] for row in perc.values]
)

perc_plot.hbar_stack(['dollars', 'remainder'], y='Organization',
                     height=.5, color=["#718dbf","#c9d9d3"],
                     source=src)
perc_plot.xaxis[0].formatter = NumeralTickFormatter(format="0%")

grid = gridplot([[raw_plot], [perc_plot]])
show(grid)