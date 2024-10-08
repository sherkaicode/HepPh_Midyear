
import numpy as np
from numpy import nan

add_legend_handle = [
    'Data',
    'atlas.yoda'
]

xpoints = {
    'Data' : [1.0, 2.0, 3.0, 4.0],
    'atlas.yoda' : [1.0, 2.0, 3.0, 4.0],
}
xedges = {
    'Data' : [0.5, 1.5, 2.5, 3.5, 4.5],
    'atlas.yoda' : [0.5, 1.5, 2.5, 3.5, 4.5],
}
ref_xerrs = [
  [abs(xpoints['Data'][i]   - xedges['Data'][i]) for i in range(len(xpoints['Data']))],
  [abs(xedges['Data'][i+1] - xpoints['Data'][i]) for i in range(len(xpoints['Data']))]
]

yvals = {
    'Data' : [0.6068, 0.2781, 0.0885, 0.0267],
    'atlas.yoda' : [0.6029412, 0.25, 0.1323529, 0.01470588],
}
xerrs = {
    'Data' : [
        [0.5, 0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5, 0.5],
    ],
    'atlas.yoda' : [
        [0.5, 0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5, 0.5],
    ],
}
yerrs = {
    'Data' : [
        [0.020738611332488006, 0.014835430563350698, 0.008490583018850943, 0.004494441010848846],
        [0.020738611332488006, 0.014835430563350698, 0.008490583018850943, 0.004494441010848846],
    ],
    'atlas.yoda' : [
        [0.09416359, 0.06063391, 0.04411765, 0.01470588],
        [0.09416359, 0.06063391, 0.04411765, 0.01470588],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'Data' : [1.0, 1.0, 1.0, 1.0],
    'atlas.yoda' : [0.9936407382992748, 0.8989572096368212, 1.4955129943502825, 0.5507820224719101],
}
ratio0_yerrs = {
    'Data' : [
        [0.03417701274305868, 0.05334566905196223, 0.09593879117345698, 0.16833112400182942],
        [0.03417701274305868, 0.05334566905196223, 0.09593879117345698, 0.16833112400182942],
    ],
    'atlas.yoda' : [
        [0.15518060316413976, 0.2180291621718806, 0.49850451977401133, 0.5507820224719101],
        [0.15518060316413976, 0.2180291621718806, 0.49850451977401133, 0.5507820224719101],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}