# Riemann Zeta Zeros Finder

A small Python script demonstrating how to use the **mpmath** library to numerically approximate a few nontrivial zeros of the Riemann zeta function on the critical line (\(\mathrm{Re}(s) = 1/2\)).

## 1. Features

- Uses **mpmath** to evaluate \(\zeta(s)\) for complex \(s\).  
- Demonstrates root-finding on the line \(\mathrm{Re}(s) = 0.5\).  
- Illustrates how one might identify the imaginary part \(t\) such that \(\zeta(0.5 + i\,t) = 0\).  
- Educational example, *not* optimized for large-scale zero searches.

## 2. Requirements

- [Pipenv](https://pipenv.pypa.io/en/latest/) for virtual environment and dependency management.
- Basic Python 3 environment.

## 3. Setup Instructions

1. **Clone** or **download** this repository.

2. **Navigate** into the project folder (where `Pipfile` will reside once created).

3. **Create and activate** a Pipenv environment:
   ```bash
   pipenv --python 3.9
   pipenv shell
   ```
   Replace `3.9` with whatever version of Python 3 you prefer.

4. **Install the dependencies**:
   ```bash
   pipenv install mpmath
   ```

   This will add `mpmath` to your Pipfile and lockfile.

## 4. Running the Code

Once inside the Pipenv shell, simply run:

```bash
python zeta_zeros.py
```

where `zeta_zeros.py` is the Python script containing the code to:

1. Define a function to locate zeros via `mp.findroot`.
2. Loop over a set of guesses and print out the approximate zero locations.
3. Verify each zero is numerically close to 0 in value.

**Example Output** might look like:

```
Zero #1 near t = 14.134725141734693
   zeta(0.5 + i*14.134725141734693) ≈ (-2.23e-22 + 1.01e-22j)

Zero #2 near t = 21.022039638771555
   zeta(0.5 + i*21.022039638771555) ≈ (3.11e-24 + 8.12e-24j)
...
```

## 5. Notes and Limitations

- **Precision**: By default, `mpmath` uses moderate precision (~15–16 digits). If you explore higher zeros or require more accuracy, increase the precision with `mp.mp.prec = 200` (or higher).  
- **Performance**: This script is *not* optimized for large-scale searches. Real-world verification of zeros uses the Riemann–Siegel formula, Turing’s method, and other sophisticated techniques.  
- **No Guarantee of Missing/Extra Zeros**: This simple approach checks around specific guesses and uses `mp.findroot`. A thorough sweep (Turing’s method) is required to ensure no zeros are missed in each interval.  

## 6. License

This code is provided under an MIT License. Feel free to use or modify it for educational or personal research purposes.
