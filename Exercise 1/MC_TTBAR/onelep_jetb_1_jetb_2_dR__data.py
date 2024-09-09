
import numpy as np
from numpy import nan

add_legend_handle = [
    'ttbar_anal.yoda'
]

xpoints = {
    'ttbar_anal.yoda' : [0.175, 0.5249999999999999, 0.875, 1.225, 1.575, 1.925, 2.2750000000000004, 2.625, 2.9749999999999996, 3.325, 3.675, 4.025, 4.375, 4.725, 5.075, 5.425, 5.775, 6.125, 6.475, 6.825],
}
xedges = {
    'ttbar_anal.yoda' : [0.0, 0.35, 0.7, 1.05, 1.4, 1.75, 2.1, 2.45, 2.8, 3.15, 3.5, 3.85, 4.2, 4.55, 4.9, 5.25, 5.6, 5.95, 6.3, 6.65, 7.0],
}
ref_xerrs = [
  [abs(xpoints['ttbar_anal.yoda'][i]   - xedges['ttbar_anal.yoda'][i]) for i in range(len(xpoints['ttbar_anal.yoda']))],
  [abs(xedges['ttbar_anal.yoda'][i+1] - xpoints['ttbar_anal.yoda'][i]) for i in range(len(xpoints['ttbar_anal.yoda']))]
]

yvals = {
    'ttbar_anal.yoda' : [0.0, 0.0, 3.174866, 2.976437, 3.968583, 4.56387, 3.571725, 5.754445, 5.952875, 2.579579, 1.389004, 1.984292, 0.5952875, 0.1984292, 0.1984292, 0.0, 0.0, 0.0, 0.0, 0.0],
}
xerrs = {
    'ttbar_anal.yoda' : [
        [0.175, 0.17500000000000004, 0.17500000000000004, 0.17499999999999982, 0.17500000000000004, 0.17500000000000004, 0.17499999999999982, 0.17499999999999982, 0.17500000000000027, 0.17499999999999982, 0.17500000000000027, 0.17499999999999982, 0.17499999999999982, 0.1750000000000007, 0.17499999999999982, 0.17499999999999982, 0.17499999999999982, 0.17499999999999982, 0.1750000000000007, 0.17499999999999982],
        [0.175, 0.17499999999999993, 0.17500000000000004, 0.17500000000000004, 0.17500000000000004, 0.17500000000000004, 0.17500000000000027, 0.17499999999999982, 0.17499999999999982, 0.17500000000000027, 0.17499999999999982, 0.17500000000000027, 0.17499999999999982, 0.17499999999999982, 0.17499999999999982, 0.17499999999999982, 0.1750000000000007, 0.17499999999999982, 0.17499999999999982, 0.17499999999999982],
    ],
}
yerrs = {
    'ttbar_anal.yoda' : [
        [0.0, 0.0, 0.7937166, 0.7685128, 0.8874021, 0.9516328, 0.8418636, 1.068574, 1.086841, 0.7154465, 0.5249942, 0.6274881, 0.3436894, 0.1984292, 0.1984292, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.7937166, 0.7685128, 0.8874021, 0.9516328, 0.8418636, 1.068574, 1.086841, 0.7154465, 0.5249942, 0.6274881, 0.3436894, 0.1984292, 0.1984292, 0.0, 0.0, 0.0, 0.0, 0.0],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'ttbar_anal.yoda' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
    'ttbar_anal.yoda' : [
        [1.0, 1.0, 0.2500000314973923, 0.2581989136675831, 0.2236067886195148, 0.2085144405953719, 0.23570224471368878, 0.1856954058992657, 0.18257413434684922, 0.2773501024779625, 0.3779644983023807, 0.3162277023744489, 0.57735027192743, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 0.2500000314973923, 0.2581989136675831, 0.2236067886195148, 0.2085144405953719, 0.23570224471368878, 0.1856954058992657, 0.18257413434684922, 0.2773501024779625, 0.3779644983023807, 0.3162277023744489, 0.57735027192743, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}