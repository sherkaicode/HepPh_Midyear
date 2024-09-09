
import numpy as np
from numpy import nan

add_legend_handle = [
    'ttbar_anal.yoda'
]

xpoints = {
    'ttbar_anal.yoda' : [20.61746, 21.890504999999997, 23.242155, 24.67726, 26.20098, 27.818785, 29.53648, 31.36024, 33.296605, 35.35253, 37.535405, 39.853065, 42.313829999999996, 44.926535, 47.700565, 50.645880000000005, 53.773055, 57.093325, 60.618605, 64.361555, 68.33562, 72.555065, 77.035045, 81.79164499999999, 86.841945, 92.20408, 97.89732000000001, 103.94210000000001, 110.3601, 117.17435, 124.40934999999999, 132.09115, 140.24725, 148.90695, 158.10135, 167.86345, 178.22835, 189.2332, 200.91755, 213.3234, 226.49525, 240.4804, 255.32909999999998, 271.09465, 287.83365000000003, 305.6062, 324.4761, 344.51115000000004, 365.78335000000004, 388.369],
}
xedges = {
    'ttbar_anal.yoda' : [20.0, 21.23492, 22.54609, 23.93822, 25.4163, 26.98566, 28.65191, 30.42105, 32.29943, 34.29378, 36.41128, 38.65953, 41.0466, 43.58106, 46.27201, 49.12912, 52.16264, 55.38347, 58.80318, 62.43403, 66.28908, 70.38216, 74.72797, 79.34212, 84.24117, 89.44272, 94.96544, 100.8292, 107.055, 113.6652, 120.6835, 128.1352, 136.0471, 144.4474, 153.3665, 162.8362, 172.8907, 183.566, 194.9004, 206.9347, 219.7121, 233.2784, 247.6824, 262.9758, 279.2135, 296.4538, 314.7586, 334.1936, 354.8287, 376.738, 400.0],
}
ref_xerrs = [
  [abs(xpoints['ttbar_anal.yoda'][i]   - xedges['ttbar_anal.yoda'][i]) for i in range(len(xpoints['ttbar_anal.yoda']))],
  [abs(xedges['ttbar_anal.yoda'][i+1] - xpoints['ttbar_anal.yoda'][i]) for i in range(len(xpoints['ttbar_anal.yoda']))]
]

yvals = {
    'ttbar_anal.yoda' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.07394709, 0.06964669, 0.1639909, 0.1235632, 0.3200379, 0.4932426, 0.7742634, 0.5347731, 0.7784042, 0.99189, 0.9748242, 1.185922, 1.080924, 1.18774, 1.038762, 0.9181463, 0.9781615, 0.8011099, 0.7042199, 0.698798, 0.5354517, 0.5463385, 0.3364471, 0.2982409, 0.2457846, 0.2066884, 0.2102419, 0.1393441, 0.04835176, 0.07806834, 0.07352827, 0.01154204, 0.04348324, 0.01535792, 0.009643189, 0.01816478, 0.0128313, 0.01611346, 0.0, 0.00357345, 0.0, 0.006339813, 0.005971121],
}
xerrs = {
    'ttbar_anal.yoda' : [
        [0.6174599999999977, 0.6555850000000021, 0.6960650000000008, 0.7390399999999993, 0.784679999999998, 0.8331250000000026, 0.8845700000000001, 0.93919, 0.9971749999999986, 1.0587499999999963, 1.1241249999999994, 1.1935349999999971, 1.267230000000005, 1.3454750000000004, 1.428555000000003, 1.5167599999999979, 1.6104150000000033, 1.7098549999999975, 1.8154249999999976, 1.9275250000000028, 2.046539999999993, 2.172905, 2.3070749999999975, 2.4495250000000084, 2.6007749999999987, 2.7613599999999963, 2.9318799999999925, 3.1128999999999962, 3.305099999999996, 3.509149999999991, 3.7258500000000083, 3.9559500000000014, 4.200149999999979, 4.459550000000007, 4.7348499999999945, 5.027250000000009, 5.3376499999999965, 5.66719999999998, 6.017149999999987, 6.3887, 6.783150000000006, 7.201999999999998, 7.64670000000001, 8.118850000000009, 8.620149999999967, 9.1524, 9.71750000000003, 10.317549999999983, 10.954649999999958, 11.630999999999972],
        [0.6174600000000012, 0.6555849999999985, 0.6960650000000008, 0.7390399999999993, 0.7846800000000016, 0.833124999999999, 0.8845700000000001, 0.93919, 0.9971749999999986, 1.0587500000000034, 1.1241249999999994, 1.1935350000000042, 1.2672299999999979, 1.3454750000000004, 1.4285549999999958, 1.516760000000005, 1.6104149999999962, 1.7098549999999975, 1.8154250000000047, 1.9275249999999957, 2.0465400000000074, 2.172905, 2.3070749999999975, 2.449524999999994, 2.6007749999999987, 2.7613600000000105, 2.9318800000000067, 3.1129000000000104, 3.305099999999996, 3.5091500000000053, 3.725849999999994, 3.9559500000000014, 4.200150000000008, 4.459550000000007, 4.7348499999999945, 5.027250000000009, 5.3376499999999965, 5.667200000000008, 6.017150000000015, 6.3887, 6.783150000000006, 7.201999999999998, 7.646699999999981, 8.118850000000009, 8.620150000000024, 9.1524, 9.717499999999973, 10.31755000000004, 10.954650000000015, 11.631000000000029],
    ],
}
yerrs = {
    'ttbar_anal.yoda' : [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05228849, 0.04924765, 0.07333898, 0.06178162, 0.09649505, 0.1162584, 0.1413605, 0.114014, 0.1334952, 0.1462462, 0.1407038, 0.1506123, 0.1395467, 0.1419621, 0.1288426, 0.1175566, 0.1177568, 0.1034228, 0.09410534, 0.09097576, 0.0772858, 0.07576352, 0.0577002, 0.05272205, 0.04644893, 0.04133768, 0.04046107, 0.03196772, 0.01827525, 0.02253639, 0.02122578, 0.008161453, 0.01537365, 0.008866902, 0.006818764, 0.009082388, 0.007408156, 0.008056731, 0.0, 0.00357345, 0.0, 0.004482925, 0.00422222],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05228849, 0.04924765, 0.07333898, 0.06178162, 0.09649505, 0.1162584, 0.1413605, 0.114014, 0.1334952, 0.1462462, 0.1407038, 0.1506123, 0.1395467, 0.1419621, 0.1288426, 0.1175566, 0.1177568, 0.1034228, 0.09410534, 0.09097576, 0.0772858, 0.07576352, 0.0577002, 0.05272205, 0.04644893, 0.04133768, 0.04046107, 0.03196772, 0.01827525, 0.02253639, 0.02122578, 0.008161453, 0.01537365, 0.008866902, 0.006818764, 0.009082388, 0.007408156, 0.008056731, 0.0, 0.00357345, 0.0, 0.004482925, 0.00422222],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'ttbar_anal.yoda' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
    'ttbar_anal.yoda' : [
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7071067975764834, 0.7071068273309183, 0.4472137173465113, 0.5000001618604892, 0.3015113210029187, 0.23570226902542482, 0.1825741730785673, 0.2132007013815766, 0.1714985607734388, 0.14744195424895903, 0.1443376149258502, 0.12700017370451008, 0.12909945565090608, 0.11952287537676597, 0.12403476446000143, 0.12803689346676014, 0.12038584630452127, 0.1290993907327821, 0.13363061736823967, 0.13018892441020152, 0.14433757517251325, 0.1386750521883411, 0.171498580311734, 0.17677672646508244, 0.18898226333138854, 0.2, 0.1924500777437799, 0.229415669554721, 0.3779645249728241, 0.2886751530774191, 0.28867509054680596, 0.7071066293306904, 0.3535534610576397, 0.577350448498234, 0.7071067465337452, 0.49999988989682237, 0.5773503853857365, 0.5000000620599175, 1.0, 1.0, 1.0, 0.7071068184503233, 0.7071067560010925],
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7071067975764834, 0.7071068273309183, 0.4472137173465113, 0.5000001618604892, 0.3015113210029187, 0.23570226902542482, 0.1825741730785673, 0.2132007013815766, 0.1714985607734388, 0.14744195424895903, 0.1443376149258502, 0.12700017370451008, 0.12909945565090608, 0.11952287537676597, 0.12403476446000143, 0.12803689346676014, 0.12038584630452127, 0.1290993907327821, 0.13363061736823967, 0.13018892441020152, 0.14433757517251325, 0.1386750521883411, 0.171498580311734, 0.17677672646508244, 0.18898226333138854, 0.2, 0.1924500777437799, 0.229415669554721, 0.3779645249728241, 0.2886751530774191, 0.28867509054680596, 0.7071066293306904, 0.3535534610576397, 0.577350448498234, 0.7071067465337452, 0.49999988989682237, 0.5773503853857365, 0.5000000620599175, 1.0, 1.0, 1.0, 0.7071068184503233, 0.7071067560010925],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}