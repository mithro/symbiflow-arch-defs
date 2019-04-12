latches = {
    # Multi bit versions

    # parameter WIDTH = 0;
    # parameter CLK_POLARITY = 1'b1;
    # parameter EN_POLARITY = 1'b1;
    "$dffe_NN_": "vpr/latches/dffe_nn.sim.v",
    "$dffe_NP_": "vpr/latches/dffe_np.sim.v",
    "$dffe_PN_": "vpr/latches/dffe_pn.sim.v",
    "$dffe_PP_": "vpr/latches/dffe_pp.sim.v",

    # parameter WIDTH = 0;
    # parameter CLK_POLARITY = 1'b1;
    # parameter SET_POLARITY = 1'b1;
    # parameter CLR_POLARITY = 1'b1;
    "$dffsr_NNN_": "vpr/latches/dffsr_nnn.sim.v",
    "$dffsr_NNP_": "vpr/latches/dffsr_nnp.sim.v",
    "$dffsr_NPN_": "vpr/latches/dffsr_npn.sim.v",
    "$dffsr_NPP_": "vpr/latches/dffsr_npp.sim.v",
    "$dffsr_PNN_": "vpr/latches/dffsr_pnn.sim.v",
    "$dffsr_PNP_": "vpr/latches/dffsr_pnp.sim.v",
    "$dffsr_PPN_": "vpr/latches/dffsr_ppn.sim.v",
    "$dffsr_PPP_": "vpr/latches/dffsr_ppp.sim.v",

    # parameter WIDTH = 0;
    # parameter CLK_POLARITY = 1'b1;
    "$dff_N_": "vpr/latches/dff_n.sim.v",
    "$dff": "vpr/latches/dff_p.sim.v",

    # FIXME: Check this? Async?
    # $adff
    # parameter WIDTH = 0;
    # parameter CLK_POLARITY = 1'b1;
    # parameter ARST_POLARITY = 1'b1;
    # parameter ARST_VALUE = 0;
    "$adff_NN0_": "vpr/latches/dff_nn0.sim.v",
    "$adff_NN1_": "vpr/latches/dff_nn1.sim.v",
    "$adff_NP0_": "vpr/latches/dff_np0.sim.v",
    "$adff_NP1_": "vpr/latches/dff_np1.sim.v",
    "$adff_PN0_": "vpr/latches/dff_pn0.sim.v",
    "$adff_PN1_": "vpr/latches/dff_pn1.sim.v",
    "$adff_PP0_": "vpr/latches/dff_pp0.sim.v",
    "$adff_PP1_": "vpr/latches/dff_pp1.sim.v",

    # parameter WIDTH = 0;
    # parameter EN_POLARITY = 1'b1;
    # parameter SET_POLARITY = 1'b1;
    # parameter CLR_POLARITY = 1'b1;
    "$dlatchsr_NNN_": "vpr/latches/dlatchsr_nnn.sim.v",
    "$dlatchsr_NNP_": "vpr/latches/dlatchsr_nnp.sim.v",
    "$dlatchsr_NPN_": "vpr/latches/dlatchsr_npn.sim.v",
    "$dlatchsr_NPP_": "vpr/latches/dlatchsr_npp.sim.v",
    "$dlatchsr_PNN_": "vpr/latches/dlatchsr_pnn.sim.v",
    "$dlatchsr_PNP_": "vpr/latches/dlatchsr_pnp.sim.v",
    "$dlatchsr_PPN_": "vpr/latches/dlatchsr_ppn.sim.v",
    "$dlatchsr_PPP_": "vpr/latches/dlatchsr_ppp.sim.v",

    # parameter WIDTH = 0;
    # parameter EN_POLARITY = 1'b1;
    "$dlatch_N_": "vpr/latches/dlatch_n.sim.v",
    "$dlatch_P_": "vpr/latches/dlatch_p.sim.v",

    # parameter WIDTH = 0;
    "$ff": "vpr/latches/ff.sim.v",

    # parameter WIDTH = 0;
    # parameter SET_POLARITY = 1'b1;
    # parameter CLR_POLARITY = 1'b1;
    "$sr_NN_": "vpr/latches/sr_nn.sim.v",
    "$sr_NP_": "vpr/latches/sr_np.sim.v",
    "$sr_PN_": "vpr/latches/sr_pn.sim.v",
    "$sr_PP_": "vpr/latches/sr_pp.sim.v",
    # Single bit versions
    "$_DFFE_NN_": "vpr/latches/dffe_nn.sim.v",
    "$_DFFE_NP_": "vpr/latches/dffe_np.sim.v",
    "$_DFFE_PN_": "vpr/latches/dffe_pn.sim.v",
    "$_DFFE_PP_": "vpr/latches/dffe_pp.sim.v",
    "$_DFFSR_NNN_": "vpr/latches/dffsr_nnn.sim.v",
    "$_DFFSR_NNP_": "vpr/latches/dffsr_nnp.sim.v",
    "$_DFFSR_NPN_": "vpr/latches/dffsr_npn.sim.v",
    "$_DFFSR_NPP_": "vpr/latches/dffsr_npp.sim.v",
    "$_DFFSR_PNN_": "vpr/latches/dffsr_pnn.sim.v",
    "$_DFFSR_PNP_": "vpr/latches/dffsr_pnp.sim.v",
    "$_DFFSR_PPN_": "vpr/latches/dffsr_ppn.sim.v",
    "$_DFFSR_PPP_": "vpr/latches/dffsr_ppp.sim.v",
    "$_DFF_NN0_": "vpr/latches/dff_nn0.sim.v",
    "$_DFF_NN1_": "vpr/latches/dff_nn1.sim.v",
    "$_DFF_NP0_": "vpr/latches/dff_np0.sim.v",
    "$_DFF_NP1_": "vpr/latches/dff_np1.sim.v",
    "$_DFF_N_": "vpr/latches/dff_n.sim.v",
    "$_DFF_PN0_": "vpr/latches/dff_pn0.sim.v",
    "$_DFF_PN1_": "vpr/latches/dff_pn1.sim.v",
    "$_DFF_PP0_": "vpr/latches/dff_pp0.sim.v",
    "$_DFF_PP1_": "vpr/latches/dff_pp1.sim.v",
    "$_DFF_P_": "vpr/latches/dff_p.sim.v",
    "$_DLATCHSR_NNN_": "vpr/latches/dlatchsr_nnn.sim.v",
    "$_DLATCHSR_NNP_": "vpr/latches/dlatchsr_nnp.sim.v",
    "$_DLATCHSR_NPN_": "vpr/latches/dlatchsr_npn.sim.v",
    "$_DLATCHSR_NPP_": "vpr/latches/dlatchsr_npp.sim.v",
    "$_DLATCHSR_PNN_": "vpr/latches/dlatchsr_pnn.sim.v",
    "$_DLATCHSR_PNP_": "vpr/latches/dlatchsr_pnp.sim.v",
    "$_DLATCHSR_PPN_": "vpr/latches/dlatchsr_ppn.sim.v",
    "$_DLATCHSR_PPP_": "vpr/latches/dlatchsr_ppp.sim.v",
    "$_DLATCH_N_": "vpr/latches/dlatch_n.sim.v",
    "$_DLATCH_P_": "vpr/latches/dlatch_p.sim.v",
    "$_FF_": "vpr/latches/ff.sim.v",
    "$_SR_NN_": "vpr/latches/sr_nn.sim.v",
    "$_SR_NP_": "vpr/latches/sr_np.sim.v",
    "$_SR_PN_": "vpr/latches/sr_pn.sim.v",
    "$_SR_PP_": "vpr/latches/sr_pp.sim.v",
}
