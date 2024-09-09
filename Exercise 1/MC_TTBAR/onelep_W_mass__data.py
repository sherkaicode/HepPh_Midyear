
import numpy as np
from numpy import nan

add_legend_handle = [
    'ttbar_anal.yoda'
]

xpoints = {
    'ttbar_anal.yoda' : [31.0, 33.0, 35.0, 37.0, 39.0, 41.0, 43.0, 45.0, 47.0, 49.0, 51.0, 53.0, 55.0, 57.0, 59.0, 61.0, 63.0, 65.0, 67.0, 69.0, 71.0, 73.0, 75.0, 77.0, 79.0, 81.0, 83.0, 85.0, 87.0, 89.0, 91.0, 93.0, 95.0, 97.0, 99.0, 101.0, 103.0, 105.0, 107.0, 109.0, 111.0, 113.0, 115.0, 117.0, 119.0, 121.0, 123.0, 125.0, 127.0, 129.0, 131.0, 133.0, 135.0, 137.0, 139.0, 141.0, 143.0, 145.0, 147.0, 149.0, 151.0, 153.0, 155.0, 157.0, 159.0, 161.0, 163.0, 165.0, 167.0, 169.0, 171.0, 173.0, 175.0, 177.0, 179.0],
}
xedges = {
    'ttbar_anal.yoda' : [30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 54.0, 56.0, 58.0, 60.0, 62.0, 64.0, 66.0, 68.0, 70.0, 72.0, 74.0, 76.0, 78.0, 80.0, 82.0, 84.0, 86.0, 88.0, 90.0, 92.0, 94.0, 96.0, 98.0, 100.0, 102.0, 104.0, 106.0, 108.0, 110.0, 112.0, 114.0, 116.0, 118.0, 120.0, 122.0, 124.0, 126.0, 128.0, 130.0, 132.0, 134.0, 136.0, 138.0, 140.0, 142.0, 144.0, 146.0, 148.0, 150.0, 152.0, 154.0, 156.0, 158.0, 160.0, 162.0, 164.0, 166.0, 168.0, 170.0, 172.0, 174.0, 176.0, 178.0, 180.0],
}
ref_xerrs = [
  [abs(xpoints['ttbar_anal.yoda'][i]   - xedges['ttbar_anal.yoda'][i]) for i in range(len(xpoints['ttbar_anal.yoda']))],
  [abs(xedges['ttbar_anal.yoda'][i+1] - xpoints['ttbar_anal.yoda'][i]) for i in range(len(xpoints['ttbar_anal.yoda']))]
]

yvals = {
    'ttbar_anal.yoda' : [0.0, 0.0347251, 0.0, 0.0347251, 0.0694502, 0.0347251, 0.0694502, 0.0347251, 0.0694502, 0.0, 0.1041753, 0.1041753, 0.1041753, 0.1041753, 0.0347251, 0.2083506, 0.2430757, 0.2430757, 0.2430757, 0.2083506, 0.2778008, 0.3819761, 0.6597769, 1.111203, 1.493179, 1.423729, 1.493179, 1.284829, 0.8334024, 1.041753, 0.5208765, 0.5208765, 0.3125259, 0.4861514, 0.4167012, 0.2778008, 0.5556016, 0.3125259, 0.347251, 0.4167012, 0.2430757, 0.3125259, 0.1736255, 0.0694502, 0.0694502, 0.1389004, 0.1389004, 0.2430757, 0.0694502, 0.1736255, 0.0694502, 0.0694502, 0.2083506, 0.1389004, 0.0347251, 0.1736255, 0.1041753, 0.1736255, 0.1041753, 0.2083506, 0.0694502, 0.1041753, 0.0694502, 0.1041753, 0.0694502, 0.1389004, 0.0694502, 0.0694502, 0.0347251, 0.0347251, 0.1389004, 0.0347251, 0.0347251, 0.0347251, 0.0694502],
}
xerrs = {
    'ttbar_anal.yoda' : [
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    ],
}
yerrs = {
    'ttbar_anal.yoda' : [
        [0.0, 0.0347251, 0.0, 0.0347251, 0.04910871, 0.0347251, 0.04910871, 0.0347251, 0.04910871, 0.0, 0.06014564, 0.06014564, 0.06014564, 0.06014564, 0.0347251, 0.08505878, 0.09187398, 0.09187398, 0.09187398, 0.08505878, 0.09821742, 0.1151701, 0.1513632, 0.1964348, 0.2277077, 0.2223491, 0.2277077, 0.2112245, 0.1701176, 0.1901972, 0.1344897, 0.1344897, 0.1041753, 0.1299294, 0.1202913, 0.09821742, 0.1389004, 0.1041753, 0.1098104, 0.1202913, 0.09187398, 0.1041753, 0.07764769, 0.04910871, 0.04910871, 0.0694502, 0.0694502, 0.09187398, 0.04910871, 0.07764769, 0.04910871, 0.04910871, 0.08505878, 0.0694502, 0.0347251, 0.07764769, 0.06014564, 0.07764769, 0.06014564, 0.08505878, 0.04910871, 0.06014564, 0.04910871, 0.06014564, 0.04910871, 0.0694502, 0.04910871, 0.04910871, 0.0347251, 0.0347251, 0.0694502, 0.0347251, 0.0347251, 0.0347251, 0.04910871],
        [0.0, 0.0347251, 0.0, 0.0347251, 0.04910871, 0.0347251, 0.04910871, 0.0347251, 0.04910871, 0.0, 0.06014564, 0.06014564, 0.06014564, 0.06014564, 0.0347251, 0.08505878, 0.09187398, 0.09187398, 0.09187398, 0.08505878, 0.09821742, 0.1151701, 0.1513632, 0.1964348, 0.2277077, 0.2223491, 0.2277077, 0.2112245, 0.1701176, 0.1901972, 0.1344897, 0.1344897, 0.1041753, 0.1299294, 0.1202913, 0.09821742, 0.1389004, 0.1041753, 0.1098104, 0.1202913, 0.09187398, 0.1041753, 0.07764769, 0.04910871, 0.04910871, 0.0694502, 0.0694502, 0.09187398, 0.04910871, 0.07764769, 0.04910871, 0.04910871, 0.08505878, 0.0694502, 0.0347251, 0.07764769, 0.06014564, 0.07764769, 0.06014564, 0.08505878, 0.04910871, 0.06014564, 0.04910871, 0.06014564, 0.04910871, 0.0694502, 0.04910871, 0.04910871, 0.0347251, 0.0347251, 0.0694502, 0.0347251, 0.0347251, 0.0347251, 0.04910871],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'ttbar_anal.yoda' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
    'ttbar_anal.yoda' : [
        [1.0, 1.0, 1.0, 1.0, 0.7071068189868424, 1.0, 0.7071068189868424, 1.0, 0.7071068189868424, 1.0, 0.5773502932076989, 0.5773502932076989, 0.5773502932076989, 0.5773502932076989, 1.0, 0.40824830838020143, 0.3779644777326569, 0.3779644777326569, 0.3779644777326569, 0.40824830838020143, 0.3535534094934212, 0.30151127256391175, 0.2294157312873488, 0.17677670056686312, 0.15249859527893173, 0.15617375216772292, 0.15249859527893173, 0.16439892001192377, 0.20412420218612282, 0.18257418025194075, 0.258198824481427, 0.258198824481427, 0.3333333333333333, 0.26726118653571707, 0.28867519459987157, 0.3535534094934212, 0.25, 0.3333333333333333, 0.3162277430446565, 0.28867519459987157, 0.3779644777326569, 0.3333333333333333, 0.44721362933440084, 0.7071068189868424, 0.7071068189868424, 0.5, 0.5, 0.3779644777326569, 0.7071068189868424, 0.44721362933440084, 0.7071068189868424, 0.7071068189868424, 0.40824830838020143, 0.5, 1.0, 0.44721362933440084, 0.5773502932076989, 0.44721362933440084, 0.5773502932076989, 0.40824830838020143, 0.7071068189868424, 0.5773502932076989, 0.7071068189868424, 0.5773502932076989, 0.7071068189868424, 0.5, 0.7071068189868424, 0.7071068189868424, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.7071068189868424],
        [1.0, 1.0, 1.0, 1.0, 0.7071068189868424, 1.0, 0.7071068189868424, 1.0, 0.7071068189868424, 1.0, 0.5773502932076989, 0.5773502932076989, 0.5773502932076989, 0.5773502932076989, 1.0, 0.40824830838020143, 0.3779644777326569, 0.3779644777326569, 0.3779644777326569, 0.40824830838020143, 0.3535534094934212, 0.30151127256391175, 0.2294157312873488, 0.17677670056686312, 0.15249859527893173, 0.15617375216772292, 0.15249859527893173, 0.16439892001192377, 0.20412420218612282, 0.18257418025194075, 0.258198824481427, 0.258198824481427, 0.3333333333333333, 0.26726118653571707, 0.28867519459987157, 0.3535534094934212, 0.25, 0.3333333333333333, 0.3162277430446565, 0.28867519459987157, 0.3779644777326569, 0.3333333333333333, 0.44721362933440084, 0.7071068189868424, 0.7071068189868424, 0.5, 0.5, 0.3779644777326569, 0.7071068189868424, 0.44721362933440084, 0.7071068189868424, 0.7071068189868424, 0.40824830838020143, 0.5, 1.0, 0.44721362933440084, 0.5773502932076989, 0.44721362933440084, 0.5773502932076989, 0.40824830838020143, 0.7071068189868424, 0.5773502932076989, 0.7071068189868424, 0.5773502932076989, 0.7071068189868424, 0.5, 0.7071068189868424, 0.7071068189868424, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.7071068189868424],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}