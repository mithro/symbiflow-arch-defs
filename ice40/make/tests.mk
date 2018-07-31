# Defaults for the iCE40 architecture.
PROG_CMD ?= $(PROG_TOOL)
DEVICE_DIR     = $(TOP_DIR)/ice40/devices
DEVICE_TYPE   ?= top-routing-virt
DEVICE_FULL   = $(DEVICE)-$(PACKAGE)
BS_EXTENSION  ?= asc #.bin later
#YOSYS_SCRIPT  ?= synth_ice40 -nodffe -nocarry; ice40_opt -unlut; abc -lut 4;
YOSYS_SCRIPT  ?= synth_ice40; ice40_opt -unlut; abc -lut 4; opt_clean; write_blif -attr -cname -param $@
#YOSYS_SCRIPT  ?= synth_ice40 -top top -vpr -nocarry -blif $@;
#RR_PATCH_TOOL ?= $(TOP_DIR)/ice40/utils/ice40_generate_routing.py
RR_PATCH_TOOL ?= $(TOP_DIR)/ice40/utils/ice40_import_routing_from_icebox.py
RR_PATCH_CMD  ?= $(RR_PATCH_TOOL) \
	--verbose \
	--device=$(DEVICE) \
	--read_rr_graph $(OUT_RRXML_VIRT) \
	--write_rr_graph $(OUT_RRXML_REAL)

INPUT_IO_FILE=$(wildcard $(TEST_DIR)/$(BOARD).pcf)

ifneq ($(INPUT_IO_FILE),)
PLACE_TOOL    ?= $(TOP_DIR)/ice40/utils/ice40_create_ioplace.py
PLACE_TOOL_CMD ?= $(PLACE_TOOL) \
	--map $(TOP_DIR)/ice40/devices/layouts/icebox/$(DEVICE).$(PACKAGE).pinmap.csv \
	--blif $(OUT_EBLIF) \
	--pcf $(INPUT_IO_FILE)
endif

ICEBOX ?= $(ICESTORM)/icebox/
ICE_DEVICE := $(shell echo $(DEVICE) | sed -e's/^..//')

# Convert a HLC file to a bit (asc) file
HLC_TO_BIT ?= $(ICEBOX)/icebox_hlc2asc.py
HLC_TO_BIT_CMD = $(HLC_TO_BIT) $(OUT_HLC) > $(OUT_BITSTREAM) || rm $(OUT_BITSTREAM)

# Convert a bit (asc) file back into HLC
BIT_TO_HLC ?= $(ICEBOX)/icebox_asc2hlc.py

# Convert a bit (asc) file into Verilog output
BIT_TO_V ?= $(ICEBOX)/icebox_vlog.py
BIT_TO_V_CMD = $(BIT_TO_V) -L -D -c -n top -p $(INPUT_IO_FILE) -d $(PACKAGE) $(OUT_BITSTREAM) > $(OUT_BIT_VERILOG) || rm $(OUT_BIT_VERILOG)

# Run timing analysis on a bit (asc) file
ifeq ($(BIT_TIME),)
BIT_TIME ?= $(ICESTORM)/icetime/icetime

$(BIT_TIME):
	(cd $(ICESTORM)/icetime; make PREFIX=$(TOP_DIR)/env/conda icetime)
endif
BIT_TIME_CMD = $(BIT_TIME) -v -t -p $(INPUT_IO_FILE) -d $(DEVICE) $(OUT_BITSTREAM) -o $(OUT_TIME_VERILOG)

# For equivalence checking
CELLS_SIM = ice40/cells_sim.v
EQUIV_CHECK_SCRIPT = rename top gate; $(EQUIV_READ); rename top gold; hierarchy; proc; clk2fflogic; miter -equiv -flatten -ignore_gold_x -make_outputs -make_outcmp gold gate miter; sat -dump_vcd $(OUT_LOCAL)/out.vcd -verify-no-timeout -timeout 600 -seq 1000 -prove trigger 0 -prove-skip 1 -show-inputs -show-outputs miter

# Arachne for comparison
# ------------------------------------------
ARACHNE_PNR ?= arachne-pnr

OUT_BLIF=$(OUT_LOCAL)/$(SOURCE).blif
arachne-pnr: $(BIT_TIME) | $(OUT_LOCAL)
	mkdir -p $(OUT_LOCAL)
	$(YOSYS) -p "synth_ice40 -nocarry -blif $(OUT_BLIF)" $(SOURCE_FILES)
	$(ARACHNE_PNR) -d $(ICE_DEVICE) \
		--post-pack-blif $(OUT_LOCAL)/arachne-pack.blif \
		--post-pack-verilog $(OUT_LOCAL)/arachne-pack.v \
		--post-place-blif $(OUT_LOCAL)/arachne-place.blif \
		--pcf-file $(INPUT_IO_FILE) \
		--package $(PACKAGE) \
		-o $(OUT_LOCAL)/arachne.asc \
		$(OUT_BLIF)
	$(BIT_TO_HLC) $(OUT_LOCAL)/arachne.asc > $(OUT_LOCAL)/arachne.hlc
	$(HLC_TO_BIT) $(OUT_LOCAL)/arachne.hlc > $(OUT_LOCAL)/arachne_from_hlc.asc
	$(BIT_TO_V) -c -n top -p $(INPUT_IO_FILE) -d $(PACKAGE) $(OUT_LOCAL)/arachne.asc > $(OUT_LOCAL)/arachne_bitstream.v
	$(BIT_TO_V) -c -n top -p $(INPUT_IO_FILE) -d $(PACKAGE) $(OUT_LOCAL)/arachne_from_hlc.asc > $(OUT_LOCAL)/arachne_bitstream_hlc.v
	#$(YOSYS) -p "rename top gate; $(EQUIV_READ); rename top gold; hierarchy; proc; miter -equiv -flatten -ignore_gold_x -make_outputs -make_outcmp gold gate miter; sat -dump_vcd $(OUT_LOCAL)/arachne-out.vcd -verify-no-timeout -timeout 20 -seq 1000 -prove trigger 0 -prove-skip 1 -show-inputs -show-outputs miter" $(OUT_LOCAL)/arachne_bitstream_hlc.v
	$(BIT_TIME) -v -t -p $(INPUT_IO_FILE) -d $(DEVICE) $(OUT_LOCAL)/arachne.asc -o $(OUT_LOCAL)/arache_time.v

arachne-prog: | $(OUT_LOCAL)
	icepack $(OUT_LOCAL)/arachne.asc > $(OUT_LOCAL)/arachne.bin
	$(PROG_CMD) $(OUT_LOCAL)/arachne.bin

.PHONY: arachne-pnr arachne-prog

# Canonicalize the HLC output to make it easy to compare.
sort:
	$(ICEBOX)/icebox_hlcsort.py $(OUT_LOCAL)/arachne.hlc > $(OUT_LOCAL)/arachne.sorted.hlc
	$(BIT_TO_HLC) $(OUT_LOCAL)/$(SOURCE).asc > $(OUT_LOCAL)/$(SOURCE).hlc
	$(ICEBOX)/icebox_hlcsort.py $(OUT_LOCAL)/$(SOURCE).hlc > $(OUT_LOCAL)/$(SOURCE).sorted.hlc
