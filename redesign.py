import pandas
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Range1d, NumeralTickFormatter, SingleIntervalTicker
from bokeh.layouts import gridplot
from bokeh.palettes import Blues, GnBu

# unifying variables
font = "helvetica"
palette = GnBu[3]  # Blues[3]
bar_color = palette[0]
perc_color = "#7ecd92"  # palette[1]
stack_color = palette[2]

# ----------
#    Data
# ----------
df = pandas.read_csv("data.csv")

# Raw Plot
raw = df
raw = raw.sort_values('dollars', ascending=False)
raw_src = ColumnDataSource(raw)

# Percentage Plot
sum = df['dollars'].sum()
perc = df
perc['dollars'] = df['dollars'] / sum
perc['remainder'] = 1 - df['dollars']
perc = perc.sort_values('dollars', ascending=False)
src = ColumnDataSource(perc)

# --------------
#    Raw Plot
# --------------
# Create figure
raw_plot = figure(
    plot_width=600, plot_height=600,
    title="Tier One Organization Budget Breakdown (raw numbers)",
    x_axis_label="Funding (in dollars)", y_axis_label="Organization",
    # x_range=Range1d(0, 190000), y_range=[row[0] for row in raw.values]
    x_range=Range1d(0, 170000), y_range=[row[0] for row in raw.values]
)
raw_plot.title.align = "center"

# Plot data
raw_plot.hbar(y='Organization', left=0, right='dollars',
              height=.75, color=bar_color,
              source=raw_src)

# Format axes
raw_plot.xaxis[0].formatter = NumeralTickFormatter(format="$0,000")
raw_plot.xaxis.ticker = SingleIntervalTicker(interval=50000)

# Format grid
raw_plot.xgrid.ticker = SingleIntervalTicker(interval=25000)
raw_plot.ygrid.grid_line_color = None

# Data labels
raw_plot.text([raw.values[row][1] for row in range(1, len(raw.values))],
              [raw.values[row][0] for row in range(1, len(raw.values))],
              text=["${:,.0f}".format(round(raw.values[row][1])) for row in range(1, len(raw.values))],
              text_font_size="8pt",
              text_baseline="middle", x_offset=5)
raw_plot.text([raw.values[0][1]], [raw.values[0][0]],
              text=["${:,.0f}".format(round(raw.values[0][1]))],
              text_color="#FFFFFF",
              text_font_size="8pt",
              text_baseline="middle", x_offset=-50)

# ------------------
#  Percentage Plot
# ------------------

# Create figure
perc_plot = figure(
    plot_width=600, plot_height=600,
    title="Tier One Organization Budget Breakdown (% of whole budget)",
    x_axis_label="Percentage of Whole Tier One Budget",  # y_axis_label="Organization",
    x_range=Range1d(0, 1), y_range=[row[0] for row in perc.values]
)
perc_plot.title.align = "center"

# Plot data
perc_plot.hbar_stack(['dollars', 'remainder'], y='Organization',
                     height=.75, color=[perc_color, stack_color],
                     source=src)

# Format axes
perc_plot.xaxis[0].formatter = NumeralTickFormatter(format="0%")
perc_plot.xgrid.grid_line_color = None

# Data labels
vals = []
for row in perc.values:
    vals.append("{:.2%}".format(row[1]))
perc_plot.text([row[1] for row in perc.values], [row[0] for row in perc.values],
               text=["{:.1%}".format(row[1]) for row in perc.values],
               text_font_size="8pt",
               text_baseline="middle", x_offset=5)

# ----------
#  Gridplot
# ----------
grid = gridplot([[raw_plot, perc_plot]])
show(grid)
