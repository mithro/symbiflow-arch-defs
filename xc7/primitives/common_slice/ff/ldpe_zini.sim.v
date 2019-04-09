/* FIXME: This is probably wrong */
(* blackbox *) (* CLASS="flipflop" *)
module LDPE_ZINI (D, G, GE, PRE, Q);
	output reg Q;

	input wire G;
	input wire GE;
	input wire D;
	input wire PRE;

	parameter [0:0] ZINI = 1'b0;
	parameter [0:0] IS_G_INVERTED = 1'b0;
	parameter [0:0] IS_D_INVERTED = 1'b0;
	parameter [0:0] IS_PRE_INVERTED = 1'b0;

	initial Q <= !ZINI;
	generate case (|IS_G_INVERTED)
		1'b0: always @(posedge G) if (PRE == !IS_PRE_INVERTED) Q <= 1'b1; else if (GE) Q <= D ^ IS_D_INVERTED;
		1'b1: always @(negedge G) if (PRE == !IS_PRE_INVERTED) Q <= 1'b1; else if (GE) Q <= D ^ IS_D_INVERTED;
	endcase endgenerate
endmodule
