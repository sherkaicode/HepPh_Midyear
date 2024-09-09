
import numpy as np
from numpy import nan

add_legend_handle = [
    'ttbar_anal.yoda'
]

xpoints = {
    'ttbar_anal.yoda' : [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
}
xedges = {
    'ttbar_anal.yoda' : [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5],
}
ref_xerrs = [
  [abs(xpoints['ttbar_anal.yoda'][i]   - xedges['ttbar_anal.yoda'][i]) for i in range(len(xpoints['ttbar_anal.yoda']))],
  [abs(xedges['ttbar_anal.yoda'][i+1] - xpoints['ttbar_anal.yoda'][i]) for i in range(len(xpoints['ttbar_anal.yoda']))]
]

yvals = {
    'ttbar_anal.yoda' : [0.0, 0.0, 0.0, 0.0, 38.47541, 24.44647, 10.07028, 2.778008, 1.250104, 0.347251, 0.0694502],
}
xerrs = {
    'ttbar_anal.yoda' : [
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    ],
}
yerrs = {
    'ttbar_anal.yoda' : [
        [0.0, 0.0, 0.0, 0.0, 1.634664, 1.303001, 0.8362912, 0.4392416, 0.2946523, 0.1552954, 0.0694502],
        [0.0, 0.0, 0.0, 0.0, 1.634664, 1.303001, 0.8362912, 0.4392416, 0.2946523, 0.1552954, 0.0694502],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'ttbar_anal.yoda' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
    'ttbar_anal.yoda' : [
        [1.0, 1.0, 1.0, 1.0, 0.04248594102051154, 0.05330016971775475, 0.0830454763919176, 0.15811387152232825, 0.23570222957449938, 0.4472136869296273, 1.0],
        [1.0, 1.0, 1.0, 1.0, 0.04248594102051154, 0.05330016971775475, 0.0830454763919176, 0.15811387152232825, 0.23570222957449938, 0.4472136869296273, 1.0],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}