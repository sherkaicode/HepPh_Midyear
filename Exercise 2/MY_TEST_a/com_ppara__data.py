
import numpy as np
from numpy import nan

add_legend_handle = [
    'test_a.yoda'
]

xpoints = {
    'test_a.yoda' : [-48.0, -44.0, -40.0, -36.0, -32.0, -28.0, -24.0, -20.0, -16.0, -12.0, -8.0, -4.0, 0.0, 4.0, 8.0, 12.0, 16.0, 20.0, 24.0, 28.0, 32.0, 36.0, 40.0, 44.0, 48.0],
}
xedges = {
    'test_a.yoda' : [-50.0, -46.0, -42.0, -38.0, -34.0, -30.0, -26.0, -22.0, -18.0, -14.0, -10.0, -6.0, -2.0, 2.0, 6.0, 10.0, 14.0, 18.0, 22.0, 26.0, 30.0, 34.0, 38.0, 42.0, 46.0, 50.0],
}
ref_xerrs = [
  [abs(xpoints['test_a.yoda'][i]   - xedges['test_a.yoda'][i]) for i in range(len(xpoints['test_a.yoda']))],
  [abs(xedges['test_a.yoda'][i+1] - xpoints['test_a.yoda'][i]) for i in range(len(xpoints['test_a.yoda']))]
]

yvals = {
    'test_a.yoda' : [0.0001700937, 0.0003590868, 0.0005291805, 0.0009071666, 0.001190656, 0.001682038, 0.002797097, 0.004970517, 0.0081645, 0.01453357, 0.02617554, 0.03889477, 0.04724826, 0.03889477, 0.02617554, 0.01453357, 0.0081645, 0.004970517, 0.002797097, 0.001682038, 0.001190656, 0.0009071666, 0.0005291805, 0.0003590868, 0.0001700937],
}
xerrs = {
    'test_a.yoda' : [
        [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
        [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
    ],
}
yerrs = {
    'test_a.yoda' : [
        [5.669791e-05, 8.238016e-05, 0.0001000057, 0.0001309382, 0.0001500086, 0.0001782957, 0.00022992, 0.0003064952, 0.0003928147, 0.0005240938, 0.0007033487, 0.0008573704, 0.0009449652, 0.0008573704, 0.0007033487, 0.0005240938, 0.0003928147, 0.0003064952, 0.00022992, 0.0001782957, 0.0001500086, 0.0001309382, 0.0001000057, 8.238016e-05, 5.669791e-05],
        [5.669791e-05, 8.238016e-05, 0.0001000057, 0.0001309382, 0.0001500086, 0.0001782957, 0.00022992, 0.0003064952, 0.0003928147, 0.0005240938, 0.0007033487, 0.0008573704, 0.0009449652, 0.0008573704, 0.0007033487, 0.0005240938, 0.0003928147, 0.0003064952, 0.00022992, 0.0001782957, 0.0001500086, 0.0001309382, 0.0001000057, 8.238016e-05, 5.669791e-05],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'test_a.yoda' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
    'test_a.yoda' : [
        [0.33333339212445845, 0.22941572901036741, 0.18898220928397774, 0.14433754505511998, 0.125988194743066, 0.10599980499846019, 0.0821995089909288, 0.06166263992256742, 0.048112523730785714, 0.036060912769539766, 0.02687045615868861, 0.02204333384668427, 0.02, 0.02204333384668427, 0.02687045615868861, 0.036060912769539766, 0.048112523730785714, 0.06166263992256742, 0.0821995089909288, 0.10599980499846019, 0.125988194743066, 0.14433754505511998, 0.18898220928397774, 0.22941572901036741, 0.33333339212445845],
        [0.33333339212445845, 0.22941572901036741, 0.18898220928397774, 0.14433754505511998, 0.125988194743066, 0.10599980499846019, 0.0821995089909288, 0.06166263992256742, 0.048112523730785714, 0.036060912769539766, 0.02687045615868861, 0.02204333384668427, 0.02, 0.02204333384668427, 0.02687045615868861, 0.036060912769539766, 0.048112523730785714, 0.06166263992256742, 0.0821995089909288, 0.10599980499846019, 0.125988194743066, 0.14433754505511998, 0.18898220928397774, 0.22941572901036741, 0.33333339212445845],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}