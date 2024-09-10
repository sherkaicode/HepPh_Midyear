
import numpy as np
from numpy import nan

add_legend_handle = [
    'Data',
    'atlas.yoda'
]

xpoints = {
    'Data' : [30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 102.5, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0, 260.0, 285.0, 305.0],
    'atlas.yoda' : [30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 102.5, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0, 260.0, 285.0, 305.0],
}
xedges = {
    'Data' : [25.0, 35.0, 45.0, 55.0, 65.0, 75.0, 85.0, 95.0, 110.0, 130.0, 150.0, 170.0, 190.0, 210.0, 230.0, 250.0, 270.0, 300.0, 310.0],
    'atlas.yoda' : [25.0, 35.0, 45.0, 55.0, 65.0, 75.0, 85.0, 95.0, 110.0, 130.0, 150.0, 170.0, 190.0, 210.0, 230.0, 250.0, 270.0, 300.0, 310.0],
}
ref_xerrs = [
  [abs(xpoints['Data'][i]   - xedges['Data'][i]) for i in range(len(xpoints['Data']))],
  [abs(xedges['Data'][i+1] - xpoints['Data'][i]) for i in range(len(xpoints['Data']))]
]

yvals = {
    'Data' : [0.4945, 0.5977, 0.669, 0.7212, 0.7748, 0.8105, 0.8332, 0.8546, 0.884, 0.9037, 0.929, 0.9447, 0.9583, 0.9688, 0.976, 0.9819, 0.9844, 0.9884],
    'atlas.yoda' : [0.4761905, 0.4761905, 0.6190476, 0.6666667, 0.6666667, 0.7142857, 0.8095238, 0.8571429, 0.8571429, 0.8571429, 0.9047619, 0.952381, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
xerrs = {
    'Data' : [
        [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 7.5, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 15.0, 5.0],
        [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 7.5, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 15.0, 5.0],
    ],
    'atlas.yoda' : [
        [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 7.5, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 15.0, 5.0],
        [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 7.5, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 15.0, 5.0],
    ],
}
yerrs = {
    'Data' : [
        [0.03140143308831621, 0.019449421585229724, 0.01711286066091815, 0.015811388300841896, 0.014403124660989364, 0.012665701717630968, 0.011869709347747316, 0.010998636279102969, 0.010076705810928491, 0.009840731680114035, 0.008091971329657563, 0.007700649323271383, 0.006543699259593155, 0.005531726674375732, 0.00560357029044876, 0.004640043103248072, 0.00420119030752, 0.00420119030752],
        [0.03140143308831621, 0.019449421585229724, 0.01711286066091815, 0.015811388300841896, 0.014403124660989364, 0.012665701717630968, 0.011869709347747316, 0.010998636279102969, 0.010076705810928491, 0.009840731680114035, 0.008091971329657563, 0.007700649323271383, 0.006543699259593155, 0.005531726674375732, 0.00560357029044876, 0.004640043103248072, 0.00420119030752, 0.00420119030752],
    ],
    'atlas.yoda' : [
        [0.1089852, 0.1089852, 0.1059712, 0.1028689, 0.1028689, 0.09858079, 0.08568909, 0.07636035, 0.07636035, 0.07636035, 0.06405645, 0.04647143, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.1089852, 0.1089852, 0.1059712, 0.1028689, 0.1028689, 0.09858079, 0.08568909, 0.07636035, 0.07636035, 0.07636035, 0.06405645, 0.04647143, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'Data' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    'atlas.yoda' : [0.9629737108190092, 0.796704868663209, 0.9253327354260089, 0.9243853300055463, 0.8604371450696953, 0.8812901912399753, 0.9715840134421507, 1.0029755441142054, 0.969618665158371, 0.9484816864003542, 0.9739094725511303, 1.008130623478353, 1.0435145570280704, 1.0322047894302229, 1.0245901639344261, 1.0184336490477646, 1.0158472165786265, 1.011736139214893],
}
ratio0_yerrs = {
    'Data' : [
        [0.06350138137172136, 0.03254044099921319, 0.02557976182498976, 0.021923721992293258, 0.018589474265603204, 0.01562702247702772, 0.014245930566187368, 0.012869923097475975, 0.011398988473901008, 0.010889378864793665, 0.008710410473258948, 0.008151423016059473, 0.006828445434199264, 0.0057098747671095506, 0.005741363002508976, 0.004725576029379848, 0.0042677674802112965, 0.004250496061837313],
        [0.06350138137172136, 0.03254044099921319, 0.02557976182498976, 0.021923721992293258, 0.018589474265603204, 0.01562702247702772, 0.014245930566187368, 0.012869923097475975, 0.011398988473901008, 0.010889378864793665, 0.008710410473258948, 0.008151423016059473, 0.006828445434199264, 0.0057098747671095506, 0.005741363002508976, 0.004725576029379848, 0.0042677674802112965, 0.004250496061837313],
    ],
    'atlas.yoda' : [
        [0.22039474216380184, 0.1823409737326418, 0.15840239162929745, 0.14263574597892403, 0.1327683273102736, 0.12162959901295496, 0.10284336293807007, 0.08935215305406037, 0.08638048642533935, 0.08449745490760208, 0.06895204520990311, 0.04919173282523553, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.22039474216380184, 0.1823409737326418, 0.15840239162929745, 0.14263574597892403, 0.1327683273102736, 0.12162959901295496, 0.10284336293807007, 0.08935215305406037, 0.08638048642533935, 0.08449745490760208, 0.06895204520990311, 0.04919173282523553, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}