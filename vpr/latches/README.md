# Flipflop / Latch types

 * Set-Reset Latch                   (`$_SR_XX_`)

 * D-type Latch
   * D-type Latch                    (`$_DLATCH_X_`)
   * D-type Latch with Set and Reset (`$_DLATCHSR_XXX_`)

 * D-flipflop                        (`$_DFF*_`)
   * D-flipflop                      (`$_DFF_X_`)
   * D-flipflop with Reset           (`$_DFF_XXX_`)
   * D-flipflop with Set and Reset   (`$_DFFSR_XXX_`)
   * D-flipflop with Enable          (`$_DFFE_XX_`)

# Table

| Type           | Value |
| -------------- | ----- |
| Data           | **D** |
| Gate           | **D** |
| Clock          | **C** |
| Clock Enable   | **E** |
| Enable (Latch) | **E** |
| Set            | **S** |
| Reset          | **R** |
| Data Out       | **Q** |

| Type              | Type          | Features           | **D** | **C** | **E** | **S** | **R** | **Q** |
| ----------------- | ------------- | ------------------ | ----- | ----- | ----- | ----- | ----- | ----- |
| `$_SR_XX_`        | Latch         | Set-Reset          |       |       |       |   X   |   X   |   X   |
| `$_DLATCH_X_`     | Latch         |                    |   X   |       |   X   |       |       |   X   |
| `$_DLATCHSR_XXX_` | Latch         | Set-Reset          |   X   |       |   X   |   X   |   X   |   X   |
| `$_DFF_X_`        | Flipflop      |                    |   X   |   X   |       |       |       |   X   |
| `$_DFF_XXX_`      | Flipflop      | Reset              |   X   |   X   |       |       |   X   |   X   |
| `$_DFFSR_XXX_`    | Flipflop      | Set-Reset          |   X   |   X   |       |   X   |   X   |   X   |
| `$_DFFE_XX_`      | Flipflop      | Enable             |   X   |   X   |   X   |       |       |   X   |


A **Set** signal always forces the output to **1**.
A **Reset** signal forces the output to an **initial** value (which could be 0 or 1).

#### Latch Truth Table

A latch has an **Enable** signal.

 * When Enable is 1, output is equal to input.
 * When Enable is 0, output is held at last value.

|  E  |  D  |  Q  |
| --- | --- | --- |
|  1  |  d  |  d  |
|  -  |  -  |  q  |

#### Flipflop Truth Table

A flipflop has a **Clock** signal.

 * On edge of Clock signal, output is set to input.
 * Otherwise, output is held at last value.

|  C  |  D  |  Q  |
| --- | --- | --- |
|  /  |  d  |  d  |
|  -  |  -  |  q  |

# Set-Reset Latch

```verilog
module \$_SR_XX_ (S, R, Q);
	input S, R;
	output reg Q;
endmodule
```

### Parameters

| Parameter      | Values  | Used for           |
| -------------- | ------- | ------------------ |
| `$_SR_**X**X_` | `N`/`P` | Polarity of SET    |
| `$_SR_X**X**_` | `N`/`P` | Polarity of RESET  |

# D-type Latch

Latches are generally uncommon in FPGAs.

## Basic D-Type Latch

```verilog
module \$_DLATCH_X_ (E, D, Q);
input E, D;
output reg Q;
endmodule
```

### Parameters

| Parameter         | Values  | Used for           |
| ----------------- | ------- | ------------------ |
| `$_DLATCH_**X**_` | `N`/`P` | Polarity of ENABLE |

## D-type Latch with Set and Reset

```verilog
module \$_DLATCHSR_XXX_ (E, S, R, D, Q);
input E, S, R, D;
output reg Q;
endmodule
```

### Parameters

| Parameter           | Values  | Used for           |
| ------------------- | ------- | ------------------ |
| `$_DLATCH_**X**XX_` | `N`/`P` | Polarity of ENABLE |
| `$_DLATCH_X**X**X_` | `N`/`P` | Polarity of SET    |
| `$_DLATCH_XX**X**_` | `N`/`P` | Polarity of RESET  |

# D-type Flipflop

D-type Flipflops are the most common type found in FPGAs. They come with a
rather wide variety of features.

## Basic D-Type Flipflop

```verilog
module \$_DFF_X_ (D, C, Q);
input D, C;
output reg Q;
endmodule
```

### Parameters

 * `$_DFF_**X**_` - `N`/`P` - Edge of the clock signal

## D-Type Flipflop with Reset

```verilog
module \$_DFF_XXX_ (D, C, R, Q);
input D, C, R;
output reg Q;
endmodule
```

### Parameters

| Parameter        | Values   | Used for                  |
| ---------------- | -------- | ------------------------- |
| `$_DFF_**X**XX_` |- `N`/`P` | Edge of the clock signal  |
| `$_DFF_X**X**X_` |- `N`/`P` | Polarity of RESET         |
| `$_DFF_XX**X**_` |- `0`/`1` | Value is set or reset (?) |


## D-Type Flipflop with Set and Reset

```verilog
module \$_DFFSR_XXX_ (C, S, R, D, Q);
input C, S, R, D;
output reg Q;
endmodule
```

### Parameters

| Parameter          | Values  | Used for                 |
| ------------------ | ------- | ------------------------ |
| `$_DFFSR_**X**XX_` | `N`/`P` | Edge of the clock signal |
| `$_DFFSR_X**X**X_` | `N`/`P` | Polarity of SET          |
| `$_DFFSR_XX**X**_` | `N`/`P` | Polarity of RESET        |

## D-Type Flipflop with Enable

```verilog
module \$_DFFE_XX_ (D, C, E, Q);
input D, C, E;
output reg Q;
endmodule
```

### Parameters

| Parameter        | Values  | Used for                 |
| ---------------- | ------- | ------------------------ |
| `$_DFFE_**X**X_` | `N`/`P` | Edge of the clock signal |
| `$_DFFE_X**X**_` | `N`/`P` | Polarity of ENABLE       |

