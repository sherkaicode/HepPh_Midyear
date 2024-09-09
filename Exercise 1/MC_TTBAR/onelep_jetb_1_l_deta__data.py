
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
    'ttbar_anal.yoda' : [8.730883, 8.929312, 6.151304, 4.167012, 3.770154, 1.389004, 0.9921458, 0.9921458, 0.5952875, 0.5952875, 0.5952875, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
xerrs = {
    'ttbar_anal.yoda' : [
        [0.175, 0.17500000000000004, 0.17500000000000004, 0.17499999999999982, 0.17500000000000004, 0.17500000000000004, 0.17499999999999982, 0.17499999999999982, 0.17500000000000027, 0.17499999999999982, 0.17500000000000027, 0.17499999999999982, 0.17499999999999982, 0.1750000000000007, 0.17499999999999982, 0.17499999999999982, 0.17499999999999982, 0.17499999999999982, 0.1750000000000007, 0.17499999999999982],
        [0.175, 0.17499999999999993, 0.17500000000000004, 0.17500000000000004, 0.17500000000000004, 0.17500000000000004, 0.17500000000000027, 0.17499999999999982, 0.17499999999999982, 0.17500000000000027, 0.17499999999999982, 0.17500000000000027, 0.17499999999999982, 0.17499999999999982, 0.17499999999999982, 0.17499999999999982, 0.1750000000000007, 0.17499999999999982, 0.17499999999999982, 0.17499999999999982],
    ],
}
yerrs = {
    'ttbar_anal.yoda' : [
        [1.31623, 1.331103, 1.104807, 0.9093166, 0.8649326, 0.5249942, 0.4437011, 0.4437011, 0.3436894, 0.3436894, 0.3436894, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [1.31623, 1.331103, 1.104807, 0.9093166, 0.8649326, 0.5249942, 0.4437011, 0.4437011, 0.3436894, 0.3436894, 0.3436894, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
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
        [0.15075565667298485, 0.14907117144075602, 0.1796053324628404, 0.21821789810060543, 0.22941572147981226, 0.3779644983023807, 0.4472136050971541, 0.4472136050971541, 0.57735027192743, 0.57735027192743, 0.57735027192743, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [0.15075565667298485, 0.14907117144075602, 0.1796053324628404, 0.21821789810060543, 0.22941572147981226, 0.3779644983023807, 0.4472136050971541, 0.4472136050971541, 0.57735027192743, 0.57735027192743, 0.57735027192743, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}