
//-
//-     $_DFFSR_PPP_ (C, S, R, D, Q)
//-
//- A positive edge D-type flip-flop with positive polarity set and reset.
//-
//- Truth table:    C S R D | Q
//-                ---------+---
//-                 - - 1 - | 0
//-                 - 1 - - | 1
//-                 / - - d | d
//-                 - - - - | q
//-
module \$_DFFSR_PPP_ (C, S, R, D, Q);
input C, S, R, D;
output reg Q;
always @(posedge C, posedge S, posedge R) begin
	if (R == 1)
		Q <= 0;
	else if (S == 1)
		Q <= 1;
	else
		Q <= D;
end
endmodule
