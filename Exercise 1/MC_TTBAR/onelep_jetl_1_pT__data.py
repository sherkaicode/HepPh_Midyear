
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
    'ttbar_anal.yoda' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.03697354, 0.03482334, 0.0, 0.2471265, 0.2618492, 0.5480473, 0.4129405, 0.3160023, 0.5265676, 0.4528193, 0.5077209, 0.4973222, 0.4323696, 0.5090313, 0.4155048, 0.5870116, 0.3118776, 0.4940178, 0.3269592, 0.3671651, 0.2900363, 0.3677278, 0.2473876, 0.2143607, 0.1843385, 0.2397585, 0.116801, 0.1173424, 0.1105183, 0.06505695, 0.0551462, 0.04616815, 0.05978945, 0.0, 0.03375116, 0.02270597, 0.0171084, 0.02014183, 0.003794096, 0.007146899, 0.006731271, 0.006339813, 0.00298556],
}
xerrs = {
    'ttbar_anal.yoda' : [
        [0.6174599999999977, 0.6555850000000021, 0.6960650000000008, 0.7390399999999993, 0.784679999999998, 0.8331250000000026, 0.8845700000000001, 0.93919, 0.9971749999999986, 1.0587499999999963, 1.1241249999999994, 1.1935349999999971, 1.267230000000005, 1.3454750000000004, 1.428555000000003, 1.5167599999999979, 1.6104150000000033, 1.7098549999999975, 1.8154249999999976, 1.9275250000000028, 2.046539999999993, 2.172905, 2.3070749999999975, 2.4495250000000084, 2.6007749999999987, 2.7613599999999963, 2.9318799999999925, 3.1128999999999962, 3.305099999999996, 3.509149999999991, 3.7258500000000083, 3.9559500000000014, 4.200149999999979, 4.459550000000007, 4.7348499999999945, 5.027250000000009, 5.3376499999999965, 5.66719999999998, 6.017149999999987, 6.3887, 6.783150000000006, 7.201999999999998, 7.64670000000001, 8.118850000000009, 8.620149999999967, 9.1524, 9.71750000000003, 10.317549999999983, 10.954649999999958, 11.630999999999972],
        [0.6174600000000012, 0.6555849999999985, 0.6960650000000008, 0.7390399999999993, 0.7846800000000016, 0.833124999999999, 0.8845700000000001, 0.93919, 0.9971749999999986, 1.0587500000000034, 1.1241249999999994, 1.1935350000000042, 1.2672299999999979, 1.3454750000000004, 1.4285549999999958, 1.516760000000005, 1.6104149999999962, 1.7098549999999975, 1.8154250000000047, 1.9275249999999957, 2.0465400000000074, 2.172905, 2.3070749999999975, 2.449524999999994, 2.6007749999999987, 2.7613600000000105, 2.9318800000000067, 3.1129000000000104, 3.305099999999996, 3.5091500000000053, 3.725849999999994, 3.9559500000000014, 4.200150000000008, 4.459550000000007, 4.7348499999999945, 5.027250000000009, 5.3376499999999965, 5.667200000000008, 6.017150000000015, 6.3887, 6.783150000000006, 7.201999999999998, 7.646699999999981, 8.118850000000009, 8.620150000000024, 9.1524, 9.717499999999973, 10.31755000000004, 10.954650000000015, 11.631000000000029],
    ],
}
yerrs = {
    'ttbar_anal.yoda' : [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.03697354, 0.03482334, 0.0, 0.0873724, 0.08728305, 0.1225471, 0.1032351, 0.08764326, 0.1097969, 0.09881328, 0.1015442, 0.0975329, 0.08825707, 0.09293598, 0.08148719, 0.09399708, 0.06649252, 0.08121603, 0.06412198, 0.06594479, 0.05688081, 0.06215735, 0.04947751, 0.04469729, 0.04022595, 0.04452204, 0.0301579, 0.02933559, 0.02762958, 0.02057281, 0.01838207, 0.01632291, 0.0180272, 0.0, 0.01275674, 0.01015442, 0.008554201, 0.009007699, 0.003794096, 0.005053621, 0.004759727, 0.004482925, 0.00298556],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.03697354, 0.03482334, 0.0, 0.0873724, 0.08728305, 0.1225471, 0.1032351, 0.08764326, 0.1097969, 0.09881328, 0.1015442, 0.0975329, 0.08825707, 0.09293598, 0.08148719, 0.09399708, 0.06649252, 0.08121603, 0.06412198, 0.06594479, 0.05688081, 0.06215735, 0.04947751, 0.04469729, 0.04022595, 0.04452204, 0.0301579, 0.02933559, 0.02762958, 0.02057281, 0.01838207, 0.01632291, 0.0180272, 0.0, 0.01275674, 0.01015442, 0.008554201, 0.009007699, 0.003794096, 0.005053621, 0.004759727, 0.004482925, 0.00298556],
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
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3535533421142613, 0.33333326968346666, 0.22360679452302748, 0.24999993945859028, 0.27735006992037714, 0.20851434839515381, 0.21821790723142764, 0.20000003939172092, 0.1961161194895382, 0.20412413361161377, 0.182574195339265, 0.19611612188354985, 0.16012814738243675, 0.213200691553353, 0.164398995339844, 0.19611615149535475, 0.17960527838838714, 0.1961161758028219, 0.1690308701164285, 0.1999999595776021, 0.20851438719877294, 0.21821784380365472, 0.1856953559519266, 0.25819898802236285, 0.24999991477931252, 0.2500000452413763, 0.3162277051106761, 0.3333333937787191, 0.3535534778846456, 0.3015113870423628, 1.0, 0.3779644907019492, 0.4472136623099564, 0.5000000584508195, 0.44721353521502266, 1.0, 0.7071068165367945, 0.7071067262037141, 0.7071068184503233, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3535533421142613, 0.33333326968346666, 0.22360679452302748, 0.24999993945859028, 0.27735006992037714, 0.20851434839515381, 0.21821790723142764, 0.20000003939172092, 0.1961161194895382, 0.20412413361161377, 0.182574195339265, 0.19611612188354985, 0.16012814738243675, 0.213200691553353, 0.164398995339844, 0.19611615149535475, 0.17960527838838714, 0.1961161758028219, 0.1690308701164285, 0.1999999595776021, 0.20851438719877294, 0.21821784380365472, 0.1856953559519266, 0.25819898802236285, 0.24999991477931252, 0.2500000452413763, 0.3162277051106761, 0.3333333937787191, 0.3535534778846456, 0.3015113870423628, 1.0, 0.3779644907019492, 0.4472136623099564, 0.5000000584508195, 0.44721353521502266, 1.0, 0.7071068165367945, 0.7071067262037141, 0.7071068184503233, 1.0],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}