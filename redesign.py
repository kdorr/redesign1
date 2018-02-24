import pandas
import numpy as np
from math import pi
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Range1d, NumeralTickFormatter, SingleIntervalTicker
from bokeh.layouts import gridplot

#Read data
df = pandas.read_csv("data.csv")

# ---------------
#  Raw data plot
# ---------------
raw = df
raw = raw.sort_values('dollars', ascending=False)
raw_src = ColumnDataSource(raw)

raw_plot = figure(
    plot_width=600, plot_height=600,
    title="Tier One Organization Budget Breakdown (raw numbers)",
    title_location="above",
    x_axis_label="Funding (in dollars)", y_axis_label="Organization",
    #x_range=Range1d(0, 190000), y_range=[row[0] for row in raw.values]
    x_range=Range1d(0, 170000), y_range=[row[0] for row in raw.values]
)

#mean and max lines
y=np.linspace(0, 30, 30)
raw_plot.line(x=24736, y=y, line_color="#8c8c8c") #line_color="", line_width=#, line_alpha=#
raw_plot.line(x=160047, y=y, line_color="#8c8c8c")

#plot data
raw_plot.hbar(y='Organization', left=0, right='dollars',
              height=.75, color="#718dbf",
              source=raw_src)

#Data labels
raw_plot.text([row[1] for row in raw.values], [row[0] for row in raw.values],
              text=["${:,.0f}".format(round(row[1])) for row in raw.values],
              text_font_size="8pt",
              text_baseline="middle", x_offset=5)

#format axes
raw_plot.xaxis[0].formatter = NumeralTickFormatter(format="$0,000")
raw_plot.xaxis.ticker = SingleIntervalTicker(interval=50000)

#format grid
raw_plot.xgrid.ticker = SingleIntervalTicker(interval=20000)
raw_plot.ygrid.grid_line_color = None

# ------------------
#  Percentage Plot
# ------------------
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
    x_axis_label="Percentage of Whole Tier One Budget", #y_axis_label="Organization",
    x_range=Range1d(0,1), y_range=[row[0] for row in perc.values]
)

perc_plot.hbar_stack(['dollars', 'remainder'], y='Organization',
                     height=.75, color=["#718dbf","#c9d9d3"],
                     source=src)

perc_plot.xaxis[0].formatter = NumeralTickFormatter(format="0%")

vals=[]
for row in perc.values:
    vals.append("{:.2%}".format(row[1]))
print(vals)
perc_plot.text([row[1] for row in perc.values], [row[0] for row in perc.values],
              text=["{:.2%}".format(row[1]) for row in perc.values],
              text_font_size="10pt",
              text_baseline="middle", x_offset=5)


# ----------
#  GridPlot
# ----------
grid = gridplot([[raw_plot, perc_plot]])
show(grid)