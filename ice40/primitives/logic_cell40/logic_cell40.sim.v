/*
  LogicCell40 #(
    .C_ON(1'b0),
    .LUT_INIT(16'b0000000000000110),
    .SEQ_MODE(4'b1000)
  ) lc40_11_10_5 (
    .carryin(gnd),
    .carryout(),
    .ce(),
    .clk(net_23811),
    .in0(net_23794),
    .in1(net_23795),
    .in2(gnd),
    .in3(gnd),
    .lcout(net_21703),
    .ltout(),
    .sr(gnd)
  );
*/


module ICESTORM_LC (
	input I0, I1, I2, I3, CIN, CLK, CEN, SR,
	output LO, O, COUT
);
	parameter [15:0] LUT_INIT = 0;

	parameter [0:0] NEG_CLK      = 0;
	parameter [0:0] CARRY_ENABLE = 0;
	parameter [0:0] DFF_ENABLE   = 0;
	parameter [0:0] SET_NORESET  = 0;
	parameter [0:0] ASYNC_SR     = 0;

	parameter [0:0] CIN_CONST    = 0;
	parameter [0:0] CIN_SET      = 0;

	wire mux_cin = CIN_CONST ? CIN_SET : CIN;

	assign COUT = CARRY_ENABLE ? (I1 && I2) || ((I1 || I2) && mux_cin) : 1'bx;

	wire [7:0] lut_s3 = I3 ? LUT_INIT[15:8] : LUT_INIT[7:0];
	wire [3:0] lut_s2 = I2 ?   lut_s3[ 7:4] :   lut_s3[3:0];
	wire [1:0] lut_s1 = I1 ?   lut_s2[ 3:2] :   lut_s2[1:0];
	wire       lut_o  = I0 ?   lut_s1[   1] :   lut_s1[  0];

	assign LO = lut_o;

	wire polarized_clk;
	assign polarized_clk = CLK ^ NEG_CLK;

	reg o_reg;
	always @(posedge polarized_clk)
		if (CEN)
			o_reg <= SR ? SET_NORESET : lut_o;

	reg o_reg_async;
	always @(posedge polarized_clk, posedge SR)
		if (SR)
			o_reg <= SET_NORESET;
		else if (CEN)
			o_reg <= lut_o;

	assign O = DFF_ENABLE ? ASYNC_SR ? o_reg_async : o_reg : lut_o;
endmodule
