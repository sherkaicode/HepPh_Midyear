
import numpy as np
from numpy import nan

add_legend_handle = [
    'Data',
    'atlas.yoda'
]

xpoints = {
    'Data' : [30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 102.5, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0, 260.0, 285.0, 320.0, 360.0, 400.0, 460.0, 505.0],
    'atlas.yoda' : [30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 102.5, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0, 260.0, 285.0, 320.0, 360.0, 400.0, 460.0, 505.0],
}
xedges = {
    'Data' : [25.0, 35.0, 45.0, 55.0, 65.0, 75.0, 85.0, 95.0, 110.0, 130.0, 150.0, 170.0, 190.0, 210.0, 230.0, 250.0, 270.0, 300.0, 340.0, 380.0, 420.0, 500.0, 510.0],
    'atlas.yoda' : [25.0, 35.0, 45.0, 55.0, 65.0, 75.0, 85.0, 95.0, 110.0, 130.0, 150.0, 170.0, 190.0, 210.0, 230.0, 250.0, 270.0, 300.0, 340.0, 380.0, 420.0, 500.0, 510.0],
}
ref_xerrs = [
  [abs(xpoints['Data'][i]   - xedges['Data'][i]) for i in range(len(xpoints['Data']))],
  [abs(xedges['Data'][i+1] - xpoints['Data'][i]) for i in range(len(xpoints['Data']))]
]

yvals = {
    'Data' : [0.8217, 0.8668, 0.8916, 0.9096, 0.9289, 0.9404, 0.9479, 0.9555, 0.9648, 0.9733, 0.9802, 0.9845, 0.9882, 0.9906, 0.9923, 0.9936, 0.995, 0.9965, 0.9977, 0.999, 0.9992, 0.9998],
    'atlas.yoda' : [0.75, 0.7941176, 0.8382353, 0.8676471, 0.8676471, 0.8970588, 0.8970588, 0.9117647, 0.9117647, 0.9558824, 0.9558824, 0.9705882, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
xerrs = {
    'Data' : [
        [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 7.5, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 15.0, 20.0, 20.0, 20.0, 40.0, 5.0],
        [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 7.5, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 15.0, 20.0, 20.0, 20.0, 40.0, 5.0],
    ],
    'atlas.yoda' : [
        [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 7.5, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 15.0, 20.0, 20.0, 20.0, 40.0, 5.0],
        [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 7.5, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 15.0, 20.0, 20.0, 20.0, 40.0, 5.0],
    ],
}
yerrs = {
    'Data' : [
        [0.012628935030318273, 0.008810221336606703, 0.007782673062643708, 0.00641404708432983, 0.005408326913195984, 0.004640043103248072, 0.004280186911806539, 0.003920459156782532, 0.003720215047547655, 0.0036359317925395685, 0.002884441020371191, 0.002692582403567252, 0.0026419689627245812, 0.002247220505424423, 0.0018027756377319948, 0.0014212670403551896, 0.0012041594578792295, 0.0013038404810405298, 0.001, 0.0007211102550927978, 0.000565685424949238, 0.0003605551275463989],
        [0.012628935030318273, 0.008810221336606703, 0.007782673062643708, 0.00641404708432983, 0.005408326913195984, 0.004640043103248072, 0.004280186911806539, 0.003920459156782532, 0.003720215047547655, 0.0036359317925395685, 0.002884441020371191, 0.002692582403567252, 0.0026419689627245812, 0.002247220505424423, 0.0018027756377319948, 0.0014212670403551896, 0.0012041594578792295, 0.0013038404810405298, 0.001, 0.0007211102550927978, 0.000565685424949238, 0.0003605551275463989],
    ],
    'atlas.yoda' : [
        [0.0525105, 0.04903402, 0.04465503, 0.04109452, 0.04109452, 0.03685111, 0.03685111, 0.03439601, 0.03439601, 0.02490313, 0.02490313, 0.02048913, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0525105, 0.04903402, 0.04465503, 0.04109452, 0.04109452, 0.03685111, 0.03685111, 0.03439601, 0.03439601, 0.02490313, 0.02490313, 0.02048913, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
    'Data' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    'atlas.yoda' : [0.9127418765972983, 0.916148592524227, 0.9401472633467923, 0.9538776385224275, 0.9340586715469911, 0.9539119523606976, 0.9463643844287373, 0.9542278388278388, 0.9450297470978442, 0.982104592623035, 0.9751911854723526, 0.9858691721686135, 1.0119409026512851, 1.0094891984655763, 1.007759750075582, 1.0064412238325282, 1.0050251256281406, 1.0035122930255895, 1.0023053021950485, 1.001001001001001, 1.00080064051241, 1.0002000400080016],
}
ratio0_yerrs = {
    'Data' : [
        [0.015369277145330745, 0.010164076299730852, 0.008728884098972307, 0.007051502951110192, 0.005822291864781983, 0.004934116443266772, 0.004515441409227281, 0.0041030446434144755, 0.0038559442864299904, 0.0037356742962494282, 0.0029427066112744245, 0.0027349745084481987, 0.0026735164569161923, 0.0022685448267963084, 0.001816764726123143, 0.0014304217394879122, 0.0012102105104313866, 0.0013084199508685698, 0.0010023053021950487, 0.0007218320871799777, 0.0005661383356177323, 0.00036062725299699827],
        [0.015369277145330745, 0.010164076299730852, 0.008728884098972307, 0.007051502951110192, 0.005822291864781983, 0.004934116443266772, 0.004515441409227281, 0.0041030446434144755, 0.0038559442864299904, 0.0037356742962494282, 0.0029427066112744245, 0.0027349745084481987, 0.0026735164569161923, 0.0022685448267963084, 0.001816764726123143, 0.0014304217394879122, 0.0012102105104313866, 0.0013084199508685698, 0.0010023053021950487, 0.0007218320871799777, 0.0005661383356177323, 0.00036062725299699827],
    ],
    'atlas.yoda' : [
        [0.06390470974808324, 0.05656901245962159, 0.050084152086137285, 0.04517867194371153, 0.04423998277532566, 0.0391866333475117, 0.03887657980799662, 0.03599791732077446, 0.03565092247097844, 0.02558628377684167, 0.025406172209753112, 0.02081171152869477, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.06390470974808324, 0.05656901245962159, 0.050084152086137285, 0.04517867194371153, 0.04423998277532566, 0.0391866333475117, 0.03887657980799662, 0.03599791732077446, 0.03565092247097844, 0.02558628377684167, 0.025406172209753112, 0.02081171152869477, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ],
}
ratio0_variation_vals = {
}
ratio_band_edges = {
}