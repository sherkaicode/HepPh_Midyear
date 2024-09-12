
import numpy as np
from numpy import nan

add_legend_handle = [
    'test_z.yoda'
]

xpoints = {
    'test_z.yoda' : [-0.96, -0.88, -0.8, -0.72, -0.64, -0.56, -0.48, -0.4, -0.32, -0.24000000000000002, -0.16, -0.08, 0.0, 0.08, 0.16, 0.24000000000000002, 0.32, 0.4, 0.48, 0.56, 0.64, 0.72, 0.8, 0.88, 0.96],
}
xedges = {
    'test_z.yoda' : [-1.0, -0.92, -0.84, -0.76, -0.68, -0.6, -0.52, -0.44, -0.36, -0.28, -0.2, -0.12, -0.04, 0.04, 0.12, 0.2, 0.28, 0.36, 0.44, 0.52, 0.6, 0.68, 0.76, 0.84, 0.92, 1.0],
}
ref_xerrs = [
  [abs(xpoints['test_z.yoda'][i]   - xedges['test_z.yoda'][i]) for i in range(len(xpoints['test_z.yoda']))],
  [abs(xedges['test_z.yoda'][i+1] - xpoints['test_z.yoda'][i]) for i in range(len(xpoints['test_z.yoda']))]
]

yvals = {
    'test_z.yoda' : [0.2292208, 0.3974026, 0.4519481, 0.5181818, 0.5266234, 0.5623377, 0.5233766, 0.55, 0.5428571, 0.5383117, 0.5435065, 0.5837662, 0.5649351, 0.5837662, 0.5435065, 0.5383117, 0.5428571, 0.55, 0.5233766, 0.5623377, 0.5266234, 0.5181818, 0.4519481, 0.3974026, 0.2292208],
}
xerrs = {
    'test_z.yoda' : [
        [0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.03999999999999998, 0.040000000000000036, 0.03999999999999998, 0.04000000000000001, 0.04000000000000001, 0.04, 0.04, 0.04000000000000001, 0.04000000000000001, 0.04000000000000001, 0.03999999999999998, 0.03999999999999998, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036],
        [0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.03999999999999998, 0.03999999999999998, 0.04000000000000001, 0.04000000000000001, 0.039999999999999994, 0.04, 0.03999999999999999, 0.04000000000000001, 0.04000000000000001, 0.03999999999999998, 0.040000000000000036, 0.03999999999999998, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925],
    ],
}
yerrs = {
    'test_z.yoda' : [
        [0.01220019, 0.01606405, 0.01713105, 0.01834344, 0.01849225, 0.01910901, 0.01843516, 0.01889822, 0.01877511, 0.01869634, 0.01878633, 0.01946969, 0.01915309, 0.01946969, 0.01878633, 0.01869634, 0.01877511, 0.01889822, 0.01843516, 0.01910901, 0.01849225, 0.01834344, 0.01713105, 0.01606405, 0.01220019],
        [0.01220019, 0.01606405, 0.01713105, 0.01834344, 0.01849225, 0.01910901, 0.01843516, 0.01889822, 0.01877511, 0.01869634, 0.01878633, 0.01946969, 0.01915309, 0.01946969, 0.01878633, 0.01869634, 0.01877511, 0.01889822, 0.01843516, 0.01910901, 0.01849225, 0.01834344, 0.01713105, 0.01606405, 0.01220019],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'test_z.yoda' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
    'test_z.yoda' : [
        [0.05322462010428373, 0.04042260921292412, 0.03790490545263936, 0.035399622294723584, 0.035114751832144186, 0.03398137809362594, 0.035223508273010296, 0.0343604, 0.034585731677820926, 0.03473143905287587, 0.034565051199939655, 0.033351862440819634, 0.033903168700263095, 0.033351862440819634, 0.034565051199939655, 0.03473143905287587, 0.034585731677820926, 0.0343604, 0.035223508273010296, 0.03398137809362594, 0.035114751832144186, 0.035399622294723584, 0.03790490545263936, 0.04042260921292412, 0.05322462010428373],
        [0.05322462010428373, 0.04042260921292412, 0.03790490545263936, 0.035399622294723584, 0.035114751832144186, 0.03398137809362594, 0.035223508273010296, 0.0343604, 0.034585731677820926, 0.03473143905287587, 0.034565051199939655, 0.033351862440819634, 0.033903168700263095, 0.033351862440819634, 0.034565051199939655, 0.03473143905287587, 0.034585731677820926, 0.0343604, 0.035223508273010296, 0.03398137809362594, 0.035114751832144186, 0.035399622294723584, 0.03790490545263936, 0.04042260921292412, 0.05322462010428373],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}