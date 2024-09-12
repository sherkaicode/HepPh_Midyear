
import numpy as np
from numpy import nan

add_legend_handle = [
    'test_az.yoda'
]

xpoints = {
    'test_az.yoda' : [-0.96, -0.88, -0.8, -0.72, -0.64, -0.56, -0.48, -0.4, -0.32, -0.24000000000000002, -0.16, -0.08, 0.0, 0.08, 0.16, 0.24000000000000002, 0.32, 0.4, 0.48, 0.56, 0.64, 0.72, 0.8, 0.88, 0.96],
}
xedges = {
    'test_az.yoda' : [-1.0, -0.92, -0.84, -0.76, -0.68, -0.6, -0.52, -0.44, -0.36, -0.28, -0.2, -0.12, -0.04, 0.04, 0.12, 0.2, 0.28, 0.36, 0.44, 0.52, 0.6, 0.68, 0.76, 0.84, 0.92, 1.0],
}
ref_xerrs = [
  [abs(xpoints['test_az.yoda'][i]   - xedges['test_az.yoda'][i]) for i in range(len(xpoints['test_az.yoda']))],
  [abs(xedges['test_az.yoda'][i+1] - xpoints['test_az.yoda'][i]) for i in range(len(xpoints['test_az.yoda']))]
]

yvals = {
    'test_az.yoda' : [0.2185609, 0.3537604, 0.4147052, 0.4735485, 0.5414985, 0.5337929, 0.5583109, 0.5583109, 0.5695192, 0.5730217, 0.5428996, 0.5975398, 0.629063, 0.5975398, 0.5428996, 0.5730217, 0.5695192, 0.5583109, 0.5583109, 0.5337929, 0.5414985, 0.4735485, 0.4147052, 0.3537604, 0.2185609],
}
xerrs = {
    'test_az.yoda' : [
        [0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.03999999999999998, 0.040000000000000036, 0.03999999999999998, 0.04000000000000001, 0.04000000000000001, 0.04, 0.04, 0.04000000000000001, 0.04000000000000001, 0.04000000000000001, 0.03999999999999998, 0.03999999999999998, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036],
        [0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.03999999999999998, 0.03999999999999998, 0.04000000000000001, 0.04000000000000001, 0.039999999999999994, 0.04, 0.03999999999999999, 0.04000000000000001, 0.04000000000000001, 0.03999999999999998, 0.040000000000000036, 0.03999999999999998, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925],
    ],
}
yerrs = {
    'test_az.yoda' : [
        [0.01237357, 0.01574213, 0.01704428, 0.01821341, 0.01947635, 0.01933728, 0.01977639, 0.01977639, 0.01997391, 0.02003524, 0.01950153, 0.02045937, 0.0209921, 0.02045937, 0.01950153, 0.02003524, 0.01997391, 0.01977639, 0.01977639, 0.01933728, 0.01947635, 0.01821341, 0.01704428, 0.01574213, 0.01237357],
        [0.01237357, 0.01574213, 0.01704428, 0.01821341, 0.01947635, 0.01933728, 0.01977639, 0.01977639, 0.01997391, 0.02003524, 0.01950153, 0.02045937, 0.0209921, 0.02045937, 0.01950153, 0.02003524, 0.01997391, 0.01977639, 0.01977639, 0.01933728, 0.01947635, 0.01821341, 0.01704428, 0.01574213, 0.01237357],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'test_az.yoda' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
    'test_az.yoda' : [
        [0.0566138316597342, 0.04449941259677454, 0.041099749894623935, 0.03846155145671457, 0.03596750498847181, 0.0362261843497731, 0.03542182321713583, 0.03542182321713583, 0.03507153051205297, 0.034964190710404165, 0.035921061647494305, 0.034239342718259104, 0.03337042553766475, 0.034239342718259104, 0.035921061647494305, 0.034964190710404165, 0.03507153051205297, 0.03542182321713583, 0.03542182321713583, 0.0362261843497731, 0.03596750498847181, 0.03846155145671457, 0.041099749894623935, 0.04449941259677454, 0.0566138316597342],
        [0.0566138316597342, 0.04449941259677454, 0.041099749894623935, 0.03846155145671457, 0.03596750498847181, 0.0362261843497731, 0.03542182321713583, 0.03542182321713583, 0.03507153051205297, 0.034964190710404165, 0.035921061647494305, 0.034239342718259104, 0.03337042553766475, 0.034239342718259104, 0.035921061647494305, 0.034964190710404165, 0.03507153051205297, 0.03542182321713583, 0.03542182321713583, 0.0362261843497731, 0.03596750498847181, 0.03846155145671457, 0.041099749894623935, 0.04449941259677454, 0.0566138316597342],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}