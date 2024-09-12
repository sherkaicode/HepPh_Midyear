
import numpy as np
from numpy import nan

add_legend_handle = [
    'test_a.yoda'
]

xpoints = {
    'test_a.yoda' : [-0.96, -0.88, -0.8, -0.72, -0.64, -0.56, -0.48, -0.4, -0.32, -0.24000000000000002, -0.16, -0.08, 0.0, 0.08, 0.16, 0.24000000000000002, 0.32, 0.4, 0.48, 0.56, 0.64, 0.72, 0.8, 0.88, 0.96],
}
xedges = {
    'test_a.yoda' : [-1.0, -0.92, -0.84, -0.76, -0.68, -0.6, -0.52, -0.44, -0.36, -0.28, -0.2, -0.12, -0.04, 0.04, 0.12, 0.2, 0.28, 0.36, 0.44, 0.52, 0.6, 0.68, 0.76, 0.84, 0.92, 1.0],
}
ref_xerrs = [
  [abs(xpoints['test_a.yoda'][i]   - xedges['test_a.yoda'][i]) for i in range(len(xpoints['test_a.yoda']))],
  [abs(xedges['test_a.yoda'][i+1] - xpoints['test_a.yoda'][i]) for i in range(len(xpoints['test_a.yoda']))]
]

yvals = {
    'test_a.yoda' : [0.00188993, 0.03023889, 0.08504687, 0.1322951, 0.1833233, 0.2381312, 0.3401875, 0.4195646, 0.4781524, 0.5367402, 0.5594194, 0.7351829, 0.7295132, 0.8410191, 0.7729816, 0.8353493, 0.8712579, 0.8523586, 0.8107802, 0.7824312, 0.7162836, 0.5650892, 0.5008316, 0.3288479, 0.1530844],
}
xerrs = {
    'test_a.yoda' : [
        [0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.03999999999999998, 0.040000000000000036, 0.03999999999999998, 0.04000000000000001, 0.04000000000000001, 0.04, 0.04, 0.04000000000000001, 0.04000000000000001, 0.04000000000000001, 0.03999999999999998, 0.03999999999999998, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036],
        [0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.03999999999999998, 0.03999999999999998, 0.04000000000000001, 0.04000000000000001, 0.039999999999999994, 0.04, 0.03999999999999999, 0.04000000000000001, 0.04000000000000001, 0.03999999999999998, 0.040000000000000036, 0.03999999999999998, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925],
    ],
}
yerrs = {
    'test_a.yoda' : [
        [0.00188993, 0.007559722, 0.01267804, 0.01581229, 0.01861366, 0.02121442, 0.02535608, 0.02815933, 0.03006118, 0.03184967, 0.03251559, 0.03727525, 0.03713124, 0.03986813, 0.03822148, 0.03973351, 0.04057853, 0.040136, 0.03914484, 0.0384544, 0.03679302, 0.03267995, 0.03076584, 0.02492989, 0.01700937],
        [0.00188993, 0.007559722, 0.01267804, 0.01581229, 0.01861366, 0.02121442, 0.02535608, 0.02815933, 0.03006118, 0.03184967, 0.03251559, 0.03727525, 0.03713124, 0.03986813, 0.03822148, 0.03973351, 0.04057853, 0.040136, 0.03914484, 0.0384544, 0.03679302, 0.03267995, 0.03076584, 0.02492989, 0.01700937],
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
        [1.0, 0.24999998346500152, 0.1490712121445504, 0.11952286970568071, 0.10153461125781611, 0.08908710828316492, 0.07453560169024435, 0.06711560031518388, 0.06286945333747149, 0.05933908062038207, 0.05812381551301223, 0.05070200898307075, 0.05089865406136586, 0.047404547649393454, 0.049446817362793626, 0.047565144305501905, 0.046574647988844635, 0.04708816218901293, 0.04828045874825261, 0.04914732439094965, 0.051366553694653906, 0.05783148925868695, 0.06142951043823911, 0.0758097892673178, 0.11111106030398916],
        [1.0, 0.24999998346500152, 0.1490712121445504, 0.11952286970568071, 0.10153461125781611, 0.08908710828316492, 0.07453560169024435, 0.06711560031518388, 0.06286945333747149, 0.05933908062038207, 0.05812381551301223, 0.05070200898307075, 0.05089865406136586, 0.047404547649393454, 0.049446817362793626, 0.047565144305501905, 0.046574647988844635, 0.04708816218901293, 0.04828045874825261, 0.04914732439094965, 0.051366553694653906, 0.05783148925868695, 0.06142951043823911, 0.0758097892673178, 0.11111106030398916],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}