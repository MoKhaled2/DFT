
# Discrete Fourier Transform (DFT) Implementation

This Python project implements the Discrete Fourier Transform (DFT) algorithm, allowing users to calculate the DFT of a signal. The program supports calculating the complex results, magnitude, and phase of the signal.

## Features

1. **Custom Complex Number Representation:**
   - Converts real and imaginary components into a readable string format.
   - Handles cases where the real or imaginary part is zero.

2. **DFT Algorithm:**
   - Computes the DFT for a given signal of size `N`.
   - Outputs the complex result, magnitude, and phase for each frequency component.

3. **Interactive User Input:**
   - Allows users to specify the number of points (`N`) for the DFT computation.
   - Pads the input signal with zeros if its length is less than `N`.

## Code Overview

### Complex Representation Function

The `Complex(real, imag)` function formats complex numbers as strings for easy readability:

- If the real part is `0`, it returns only the imaginary part with an `i` suffix.
- Handles positive and negative imaginary values appropriately.

### Phase Calculation

The `phase(sum_reals, sum_imags)` function calculates the phase angle of the complex number:

- Returns the angle in degrees.
- Handles special cases where the real part is `0` or when the phase is undefined.

### DFT Algorithm

The `calculate(input_signal, N)` function computes the DFT:

1. Pads the input signal with zeros until its length matches `N`.
2. Iterates through each frequency component `k` to calculate:
   - The sum of real and imaginary parts using the DFT formula.
   - The phase and magnitude of the result.
3. Returns the complex results, magnitudes, and phases as separate lists.

### Input and Output

- Prompts the user for the number of DFT points (`N`).
- Computes and displays:
  - **DFT Result:** List of formatted complex numbers.
  - **Magnitude:** List of magnitudes for each frequency component.
  - **Phase:** List of phase angles in degrees.

## How to Run the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/MoKhaled2/dft-complex.git
   cd dft-complex
   ```

2. Run the script:
   ```bash
   python dft.py
   ```

3. Enter the desired number of points (`N`) when prompted.
4. View the DFT result, magnitude, and phase outputs.

## Example

### Input:
```
How many points do you want ? 4
```

### Output:
```
DFT Result:
['1.5 + 0.0i', '-0.5 - 0.5i', '-0.5 + 0.0i', '-0.5 + 0.5i']
------------------------------------------------------------------------------------
Magnitude_result:
[1.5, 0.707, 0.5, 0.707]
-------------------------------------------------------------------------------------
Phase_result:
[0, -135.0, 180.0, 135.0]
```

## License

This project is licensed under the [MIT License](LICENSE).
