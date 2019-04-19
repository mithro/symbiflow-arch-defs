(* blackbox *)
module PRECYINIT_MUX(I, O);
	input wire I;
	output wire O;

	parameter CI_INIT = 0;

	if (CI_INIT == 1) assign O = I;
endmodule
