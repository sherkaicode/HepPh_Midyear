
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
    'test_z.yoda' : [0.01038961, 0.1571429, 0.2298701, 0.3337662, 0.3597403, 0.4363636, 0.4233766, 0.4623377, 0.4532468, 0.487013, 0.5012987, 0.5428571, 0.5649351, 0.6246753, 0.5857143, 0.5896104, 0.6324675, 0.6376623, 0.6233766, 0.6883117, 0.6935065, 0.7025974, 0.674026, 0.6376623, 0.4480519],
}
xerrs = {
    'test_z.yoda' : [
        [0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.03999999999999998, 0.040000000000000036, 0.03999999999999998, 0.04000000000000001, 0.04000000000000001, 0.04, 0.04, 0.04000000000000001, 0.04000000000000001, 0.04000000000000001, 0.03999999999999998, 0.03999999999999998, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036],
        [0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.03999999999999998, 0.03999999999999998, 0.04000000000000001, 0.04000000000000001, 0.039999999999999994, 0.04, 0.03999999999999999, 0.04000000000000001, 0.04000000000000001, 0.03999999999999998, 0.040000000000000036, 0.03999999999999998, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925, 0.040000000000000036, 0.040000000000000036, 0.039999999999999925],
    ],
}
yerrs = {
    'test_z.yoda' : [
        [0.003673282, 0.01428571, 0.0172781, 0.02081977, 0.0216147, 0.02380559, 0.02344866, 0.02450385, 0.02426174, 0.02514924, 0.02551543, 0.02655201, 0.02708656, 0.02848274, 0.02758021, 0.02767179, 0.02865984, 0.0287773, 0.02845312, 0.02989835, 0.03001096, 0.03020702, 0.02958646, 0.0287773, 0.02412231],
        [0.003673282, 0.01428571, 0.0172781, 0.02081977, 0.0216147, 0.02380559, 0.02344866, 0.02450385, 0.02426174, 0.02514924, 0.02551543, 0.02655201, 0.02708656, 0.02848274, 0.02758021, 0.02767179, 0.02865984, 0.0287773, 0.02845312, 0.02989835, 0.03001096, 0.03020702, 0.02958646, 0.0287773, 0.02412231],
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
        [0.35355340575825267, 0.09090903884298941, 0.07516462558636379, 0.062378305532435584, 0.060084177391301445, 0.05455448162954014, 0.05538487483720168, 0.05299989596349162, 0.05352876181365208, 0.051639771422939434, 0.05089865583134367, 0.04891160122986326, 0.04794632162172256, 0.04559607207136251, 0.04708816226614238, 0.04693233023026731, 0.045314328404226306, 0.04512937333758009, 0.04564354837829973, 0.043437224734084866, 0.043274230306421066, 0.042993355796648265, 0.0438951316418061, 0.04512937333758009, 0.0538382049043872],
        [0.35355340575825267, 0.09090903884298941, 0.07516462558636379, 0.062378305532435584, 0.060084177391301445, 0.05455448162954014, 0.05538487483720168, 0.05299989596349162, 0.05352876181365208, 0.051639771422939434, 0.05089865583134367, 0.04891160122986326, 0.04794632162172256, 0.04559607207136251, 0.04708816226614238, 0.04693233023026731, 0.045314328404226306, 0.04512937333758009, 0.04564354837829973, 0.043437224734084866, 0.043274230306421066, 0.042993355796648265, 0.0438951316418061, 0.04512937333758009, 0.0538382049043872],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}