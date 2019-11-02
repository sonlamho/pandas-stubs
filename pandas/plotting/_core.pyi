# Stubs for pandas.plotting._core (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple
from pandas.core.base import PandasObject
from typing import Any, Optional

class MPLPlot:
    orientation: Any = ...
    data: Any = ...
    by: Any = ...
    kind: Any = ...
    sort_columns: Any = ...
    subplots: Any = ...
    sharex: bool = ...
    sharey: Any = ...
    figsize: Any = ...
    layout: Any = ...
    xticks: Any = ...
    yticks: Any = ...
    xlim: Any = ...
    ylim: Any = ...
    title: Any = ...
    use_index: Any = ...
    fontsize: Any = ...
    rot: Any = ...
    grid: Any = ...
    legend: Any = ...
    legend_handles: Any = ...
    legend_labels: Any = ...
    ax: Any = ...
    fig: Any = ...
    axes: Any = ...
    errors: Any = ...
    secondary_y: Any = ...
    colormap: Any = ...
    table: Any = ...
    kwds: Any = ...
    def __init__(self, data: Any, kind: Optional[Any] = ..., by: Optional[Any] = ..., subplots: bool = ..., sharex: Optional[Any] = ..., sharey: bool = ..., use_index: bool = ..., figsize: Optional[Any] = ..., grid: Optional[Any] = ..., legend: bool = ..., rot: Optional[Any] = ..., ax: Optional[Any] = ..., fig: Optional[Any] = ..., title: Optional[Any] = ..., xlim: Optional[Any] = ..., ylim: Optional[Any] = ..., xticks: Optional[Any] = ..., yticks: Optional[Any] = ..., sort_columns: bool = ..., fontsize: Optional[Any] = ..., secondary_y: bool = ..., colormap: Optional[Any] = ..., table: bool = ..., layout: Optional[Any] = ..., **kwds: Any) -> None: ...
    @property
    def nseries(self): ...
    def draw(self) -> None: ...
    def generate(self) -> None: ...
    @property
    def result(self): ...
    @property
    def legend_title(self): ...
    def plt(self): ...
    def on_right(self, i: Any): ...

class PlanePlot(MPLPlot):
    x: Any = ...
    y: Any = ...
    def __init__(self, data: Any, x: Any, y: Any, **kwargs: Any) -> None: ...
    @property
    def nseries(self): ...

class ScatterPlot(PlanePlot):
    c: Any = ...
    def __init__(self, data: Any, x: Any, y: Any, s: Optional[Any] = ..., c: Optional[Any] = ..., **kwargs: Any) -> None: ...

class HexBinPlot(PlanePlot):
    C: Any = ...
    def __init__(self, data: Any, x: Any, y: Any, C: Optional[Any] = ..., **kwargs: Any) -> None: ...

class LinePlot(MPLPlot):
    orientation: str = ...
    data: Any = ...
    x_compat: Any = ...
    def __init__(self, data: Any, **kwargs: Any) -> None: ...

class AreaPlot(LinePlot):
    def __init__(self, data: Any, **kwargs: Any) -> None: ...

class BarPlot(MPLPlot):
    orientation: str = ...
    bar_width: Any = ...
    tick_pos: Any = ...
    bottom: Any = ...
    left: Any = ...
    log: Any = ...
    tickoffset: Any = ...
    lim_offset: Any = ...
    ax_pos: Any = ...
    def __init__(self, data: Any, **kwargs: Any) -> None: ...

class BarhPlot(BarPlot):
    orientation: str = ...

class HistPlot(LinePlot):
    bins: Any = ...
    bottom: Any = ...
    def __init__(self, data: Any, bins: int = ..., bottom: int = ..., **kwargs: Any) -> None: ...
    @property
    def orientation(self): ...

class KdePlot(HistPlot):
    orientation: str = ...
    bw_method: Any = ...
    ind: Any = ...
    def __init__(self, data: Any, bw_method: Optional[Any] = ..., ind: Optional[Any] = ..., **kwargs: Any) -> None: ...

class PiePlot(MPLPlot):
    def __init__(self, data: Any, kind: Optional[Any] = ..., **kwargs: Any) -> None: ...

class BoxPlot(LinePlot):

BP = namedtuple('Boxplot', ['ax', 'lines'])
    return_type: Any = ...
    def __init__(self, data: Any, return_type: str = ..., **kwargs: Any) -> None: ...
    def maybe_color_bp(self, bp: Any) -> None: ...
    @property
    def orientation(self): ...
    @property
    def result(self): ...

df_kind: str
series_kind: str
df_coord: str
series_coord: str
df_unique: str
series_unique: str
df_ax: str
series_ax: str
df_note: str
series_note: str

def plot_frame(data: Any, x: Optional[Any] = ..., y: Optional[Any] = ..., kind: str = ..., ax: Optional[Any] = ..., subplots: bool = ..., sharex: Optional[Any] = ..., sharey: bool = ..., layout: Optional[Any] = ..., figsize: Optional[Any] = ..., use_index: bool = ..., title: Optional[Any] = ..., grid: Optional[Any] = ..., legend: bool = ..., style: Optional[Any] = ..., logx: bool = ..., logy: bool = ..., loglog: bool = ..., xticks: Optional[Any] = ..., yticks: Optional[Any] = ..., xlim: Optional[Any] = ..., ylim: Optional[Any] = ..., rot: Optional[Any] = ..., fontsize: Optional[Any] = ..., colormap: Optional[Any] = ..., table: bool = ..., yerr: Optional[Any] = ..., xerr: Optional[Any] = ..., secondary_y: bool = ..., sort_columns: bool = ..., **kwds: Any): ...
def plot_series(data: Any, kind: str = ..., ax: Optional[Any] = ..., figsize: Optional[Any] = ..., use_index: bool = ..., title: Optional[Any] = ..., grid: Optional[Any] = ..., legend: bool = ..., style: Optional[Any] = ..., logx: bool = ..., logy: bool = ..., loglog: bool = ..., xticks: Optional[Any] = ..., yticks: Optional[Any] = ..., xlim: Optional[Any] = ..., ylim: Optional[Any] = ..., rot: Optional[Any] = ..., fontsize: Optional[Any] = ..., colormap: Optional[Any] = ..., table: bool = ..., yerr: Optional[Any] = ..., xerr: Optional[Any] = ..., label: Optional[Any] = ..., secondary_y: bool = ..., **kwds: Any): ...
def boxplot(data: Any, column: Optional[Any] = ..., by: Optional[Any] = ..., ax: Optional[Any] = ..., fontsize: Optional[Any] = ..., rot: int = ..., grid: bool = ..., figsize: Optional[Any] = ..., layout: Optional[Any] = ..., return_type: Optional[Any] = ..., **kwds: Any): ...
def boxplot_frame(self, column: Optional[Any] = ..., by: Optional[Any] = ..., ax: Optional[Any] = ..., fontsize: Optional[Any] = ..., rot: int = ..., grid: bool = ..., figsize: Optional[Any] = ..., layout: Optional[Any] = ..., return_type: Optional[Any] = ..., **kwds: Any): ...
def scatter_plot(data: Any, x: Any, y: Any, by: Optional[Any] = ..., ax: Optional[Any] = ..., figsize: Optional[Any] = ..., grid: bool = ..., **kwargs: Any): ...
def hist_frame(data: Any, column: Optional[Any] = ..., by: Optional[Any] = ..., grid: bool = ..., xlabelsize: Optional[Any] = ..., xrot: Optional[Any] = ..., ylabelsize: Optional[Any] = ..., yrot: Optional[Any] = ..., ax: Optional[Any] = ..., sharex: bool = ..., sharey: bool = ..., figsize: Optional[Any] = ..., layout: Optional[Any] = ..., bins: int = ..., **kwds: Any): ...
def hist_series(self, by: Optional[Any] = ..., ax: Optional[Any] = ..., grid: bool = ..., xlabelsize: Optional[Any] = ..., xrot: Optional[Any] = ..., ylabelsize: Optional[Any] = ..., yrot: Optional[Any] = ..., figsize: Optional[Any] = ..., bins: int = ..., **kwds: Any): ...
def grouped_hist(data: Any, column: Optional[Any] = ..., by: Optional[Any] = ..., ax: Optional[Any] = ..., bins: int = ..., figsize: Optional[Any] = ..., layout: Optional[Any] = ..., sharex: bool = ..., sharey: bool = ..., rot: int = ..., grid: bool = ..., xlabelsize: Optional[Any] = ..., xrot: Optional[Any] = ..., ylabelsize: Optional[Any] = ..., yrot: Optional[Any] = ..., **kwargs: Any): ...
def boxplot_frame_groupby(grouped: Any, subplots: bool = ..., column: Optional[Any] = ..., fontsize: Optional[Any] = ..., rot: int = ..., grid: bool = ..., ax: Optional[Any] = ..., figsize: Optional[Any] = ..., layout: Optional[Any] = ..., sharex: bool = ..., sharey: bool = ..., **kwds: Any): ...

class BasePlotMethods(PandasObject):
    def __init__(self, data: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...

class SeriesPlotMethods(BasePlotMethods):
    def __call__(self, kind: str = ..., ax: Optional[Any] = ..., figsize: Optional[Any] = ..., use_index: bool = ..., title: Optional[Any] = ..., grid: Optional[Any] = ..., legend: bool = ..., style: Optional[Any] = ..., logx: bool = ..., logy: bool = ..., loglog: bool = ..., xticks: Optional[Any] = ..., yticks: Optional[Any] = ..., xlim: Optional[Any] = ..., ylim: Optional[Any] = ..., rot: Optional[Any] = ..., fontsize: Optional[Any] = ..., colormap: Optional[Any] = ..., table: bool = ..., yerr: Optional[Any] = ..., xerr: Optional[Any] = ..., label: Optional[Any] = ..., secondary_y: bool = ..., **kwds: Any): ...
    def line(self, **kwds: Any): ...
    def bar(self, **kwds: Any): ...
    def barh(self, **kwds: Any): ...
    def box(self, **kwds: Any): ...
    def hist(self, bins: int = ..., **kwds: Any): ...
    def kde(self, bw_method: Optional[Any] = ..., ind: Optional[Any] = ..., **kwds: Any): ...
    density: Any = ...
    def area(self, **kwds: Any): ...
    def pie(self, **kwds: Any): ...

class FramePlotMethods(BasePlotMethods):
    def __call__(self, x: Optional[Any] = ..., y: Optional[Any] = ..., kind: str = ..., ax: Optional[Any] = ..., subplots: bool = ..., sharex: Optional[Any] = ..., sharey: bool = ..., layout: Optional[Any] = ..., figsize: Optional[Any] = ..., use_index: bool = ..., title: Optional[Any] = ..., grid: Optional[Any] = ..., legend: bool = ..., style: Optional[Any] = ..., logx: bool = ..., logy: bool = ..., loglog: bool = ..., xticks: Optional[Any] = ..., yticks: Optional[Any] = ..., xlim: Optional[Any] = ..., ylim: Optional[Any] = ..., rot: Optional[Any] = ..., fontsize: Optional[Any] = ..., colormap: Optional[Any] = ..., table: bool = ..., yerr: Optional[Any] = ..., xerr: Optional[Any] = ..., secondary_y: bool = ..., sort_columns: bool = ..., **kwds: Any): ...
    def line(self, x: Optional[Any] = ..., y: Optional[Any] = ..., **kwds: Any): ...
    def bar(self, x: Optional[Any] = ..., y: Optional[Any] = ..., **kwds: Any): ...
    def barh(self, x: Optional[Any] = ..., y: Optional[Any] = ..., **kwds: Any): ...
    def box(self, by: Optional[Any] = ..., **kwds: Any): ...
    def hist(self, by: Optional[Any] = ..., bins: int = ..., **kwds: Any): ...
    def kde(self, bw_method: Optional[Any] = ..., ind: Optional[Any] = ..., **kwds: Any): ...
    density: Any = ...
    def area(self, x: Optional[Any] = ..., y: Optional[Any] = ..., **kwds: Any): ...
    def pie(self, y: Optional[Any] = ..., **kwds: Any): ...
    def scatter(self, x: Any, y: Any, s: Optional[Any] = ..., c: Optional[Any] = ..., **kwds: Any): ...
    def hexbin(self, x: Any, y: Any, C: Optional[Any] = ..., reduce_C_function: Optional[Any] = ..., gridsize: Optional[Any] = ..., **kwds: Any): ...