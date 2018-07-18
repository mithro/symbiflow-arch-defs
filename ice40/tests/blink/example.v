/* Binary counter displayed on LEDs (the 4 green ones on the right).
 * Changes value about once a second.
 */

`ifndef CLK_MHZ
`define CLK_MHZ 24
`endif

module top (
	input  clk,
	inout LED2,
	inout LED3,
	inout LED4,
	inout LED5
);

	wire flash_io0_di;
	wire flash_io1_di;
	wire flash_io2_di;
	wire flash_io3_di;
	SB_IO #(
		.PIN_TYPE(6'b 1010_01),
		.PULLUP(1'b 0)
	) io_buf [3:0] (
		.PACKAGE_PIN_I({LED2, LED3, LED4, LED5}),
		.PACKAGE_PIN_O({LED2, LED3, LED4, LED5}),
		.OUTPUT_ENABLE({outcnt[0], outcnt[1], outcnt[2], outcnt[3]}),
		.D_OUT_0({outcnt[2], outcnt[3], outcnt[4], outcnt[5]}),
		.D_IN_0({flash_io3_di, flash_io2_di, flash_io1_di, flash_io0_di})
	);

	localparam BITS = 4;
        localparam LOG2DELAY = $clog2($rtoi(`CLK_MHZ * 1e6));

	reg [BITS+LOG2DELAY-1:0] counter1 = 0;
	reg [BITS+LOG2DELAY-1:0] counter2 = 0;
	reg [BITS-1:0] outcnt;

	always @(posedge clk) begin
		counter1 <= counter1 + 1;
		outcnt <= counter1 >> LOG2DELAY;
		counter2 <= counter2 + {flash_io3_di, flash_io2_di, flash_io1_di, flash_io0_di};
	end
endmodule
