#!/usr/bin/env python3

from collections import namedtuple

Times = namedtuple("Times", ("min", "typical", "max"))

IoPath = namedtuple("IoPath", ("src", "dst", "low2high", "high2low"))

"""
    (CELLTYPE "LogicCell40")
    (INSTANCE *)
    (DELAY
      (ABSOLUTE
        (IOPATH in0           ltout (293.136 : 324.149 : 364.700) (310.048 : 342.850 : 385.740))
        (IOPATH in1           ltout (259.313 : 286.747 : 322.619) (304.411 : 336.616 : 378.727))
        (IOPATH in2           ltout (248.039 : 274.280 : 308.592) (276.225 : 305.448 : 343.659))
        (IOPATH in3           ltout (214.215 : 236.878 : 266.511) (219.852 : 243.112 : 273.525))

        (IOPATH in0           lcout (360.783 : 398.952 : 448.861) (310.048 : 342.850 : 385.740))
        (IOPATH in1           lcout (321.323 : 355.317 : 399.767) (304.411 : 336.616 : 378.727))
        (IOPATH in2           lcout (304.411 : 336.616 : 378.727) (281.862 : 311.682 : 350.673))
        (IOPATH in3           lcout (253.676 : 280.513 : 315.606) (231.127 : 255.579 : 287.552))

        (IOPATH (posedge clk) lcout (434.067 : 479.990 : 540.036) (434.067 : 479.990 : 540.036))
        (IOPATH sr            lcout (      0 :       0 :       0) (481.612 : 532.564 : 599.188))
        (IOPATH sr            lcout (481.589 : 532.539 : 599.160) (      0 :       0 :       0))
      )
    )
    (TIMINGCHECK
      (HOLD     (negedge sr)  (posedge clk) (-158.688 :-175.477 :-197.429))
      (HOLD     (posedge sr)  (posedge clk) (-143.975 :-159.207 :-179.124))
      (RECOVERY (negedge sr)  (posedge clk) ( 128.360 : 141.940 : 159.696))
      (SETUP    (negedge sr)  (posedge clk) ( 112.745 : 124.673 : 140.269))
      (SETUP    (posedge sr)  (posedge clk) ( 163.480 : 180.775 : 203.390))

      (SETUP    (negedge in0) (posedge clk) ( 321.323 : 355.317 : 399.767))
      (SETUP    (negedge in1) (posedge clk) ( 304.411 : 336.616 : 378.727))
      (SETUP    (negedge in2) (posedge clk) ( 259.313 : 286.747 : 322.619))
      (SETUP    (negedge in3) (posedge clk) ( 174.754 : 193.243 : 217.417))

      (SETUP    (posedge in0) (posedge clk) ( 377.695 : 417.653 : 469.902))
      (SETUP    (posedge in1) (posedge clk) ( 321.323 : 355.317 : 399.767))
      (SETUP    (posedge in2) (posedge clk) ( 298.774 : 330.382 : 371.713))
      (SETUP    (posedge in3) (posedge clk) ( 219.852 : 243.112 : 273.525))

    )
"""

lt_paths = [
    IoPath("in0", "ltout", Times(293.136, 324.149, 364.700), Times(310.048, 342.850, 385.740)),
    IoPath("in1", "ltout", Times(259.313, 286.747, 322.619), Times(304.411, 336.616, 378.727)),
    IoPath("in2", "ltout", Times(248.039, 274.280, 308.592), Times(276.225, 305.448, 343.659)),
    IoPath("in3", "ltout", Times(214.215, 236.878, 266.511), Times(219.852, 243.112, 273.525)),
]

lc_paths = [
    IoPath("in0", "lcout", Times(360.783, 398.952, 448.861), Times(310.048, 342.850, 385.740)),
    IoPath("in1", "lcout", Times(321.323, 355.317, 399.767), Times(304.411, 336.616, 378.727)),
    IoPath("in2", "lcout", Times(304.411, 336.616, 378.727), Times(281.862, 311.682, 350.673)),
    IoPath("in3", "lcout", Times(253.676, 280.513, 315.606), Times(231.127, 255.579, 287.552)),
]

# posedge -> posedge clk
posedge_paths = [
    IoPath("in0",   "clk", Times(377.695, 417.653, 469.902), None),
    IoPath("in1",   "clk", Times(321.323, 355.317, 399.767), None),
    IoPath("in2",   "clk", Times(298.774, 330.382, 371.713), None),
    IoPath("in3",   "clk", Times(219.852, 243.112, 273.525), None),
]

x_paths = [
    IoPath("(posedge clk)", "lcout", Times(434.067, 479.990, 540.036), Times(434.067, 479.990, 540.036)),
    IoPath("sr"           , "lcout", Times(      0,       0,       0), Times(481.612, 532.564, 599.188)),
    IoPath("sr"           , "lcout", Times(481.589, 532.539, 599.160), Times(      0,       0,       0)),
]


# negedge -> posedge clk
negedge_paths = [
      IoPath("in0", "clk", Times(321.323, 355.317, 399.767), None),
      IoPath("in1", "clk", Times(304.411, 336.616, 378.727), None),
      IoPath("in2", "clk", Times(259.313, 286.747, 322.619), None),
      IoPath("in3", "clk", Times(174.754, 193.243, 217.417), None),
]


for p2ltout, p2lcout, p2clk in zip(lt_paths, lc_paths, posedge_paths):
    assert p2ltout.src == p2clk.src, (p2ltout.src, p2clk.src)
    assert p2ltout.src == p2lcout.src, (p2ltout.src, p2lcout.src)

    print("{}".format(p2ltout.src))
    print("            {:11s} {:11s} lout->clk   lcout->clk    ".format(p2ltout.dst, p2clk.dst))
    for n, p2ltout_l2h, p2lcout_l2h, p2clk_l2h in zip(("min", "typical", "max"), p2ltout.low2high, p2lcout.low2high, p2clk.low2high):
        print("  {:>8s} {:11f} {:11f} {:11f} {:11f}".format(n, p2ltout_l2h, p2clk_l2h, p2clk_l2h - p2ltout_l2h, p2clk_l2h - p2lcout_l2h))
    print()

