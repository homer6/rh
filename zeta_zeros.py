import mpmath as mp

# Increase precision for accurate calculations (80 bits here = ~24 decimal digits)
mp.mp.prec = 80

def zeta_magnitude(t):
    """
    Returns the magnitude of zeta(0.5 + i*t).
    This is the function we want to minimize to find zeros.
    """
    val = mp.zeta(0.5 + 1j * t)
    return mp.sqrt(mp.re(val)**2 + mp.im(val)**2)

def find_zero_on_line(t_guess):
    """
    Finds a zero of zeta(0.5 + i*t) near the guess 't_guess' by minimizing |zeta|.
    Uses mpmath's findroot function.
    """
    # Use findroot with a single-variable function, zeta_magnitude
    zero_t = mp.findroot(zeta_magnitude, t_guess, solver='mnewton')  # Modified Newton's method
    return zero_t

def approximate_riemann_zeros(n_zeros=5, start_guess=14.0, spacing=10.0):
    """
    Finds a specified number of zeros of the Riemann zeta function along
    the critical line Re(s) = 0.5.
    
    :param n_zeros: Number of zeros to find
    :param start_guess: Starting guess for the first zero's imaginary part
    :param spacing: Increment to guess the next zero (approximate range)
    :return: List of zeros (imaginary parts of s)
    """
    zeros_found = []
    t_guess = start_guess
    for _ in range(n_zeros):
        # Find the zero near the current guess
        t_root = find_zero_on_line(t_guess)
        zeros_found.append(t_root)
        # Update the guess for the next zero
        t_guess = t_root + spacing
    return zeros_found

if __name__ == "__main__":
    # Let's find the first 5 zeros of the Riemann zeta function
    print("Finding zeros of the Riemann zeta function on the critical line...")
    
    # Known approximate imaginary parts of first few zeros:
    # 14.134725..., 21.022040..., 25.010856..., 30.424876..., 32.935061...
    try:
        first_5_zeros = approximate_riemann_zeros(n_zeros=5, start_guess=14.0, spacing=10.0)
        print("\nZeros found:")
        for i, t in enumerate(first_5_zeros, 1):
            zeta_value = mp.zeta(0.5 + 1j * t)
            print(f"Zero #{i}: t ≈ {t}")
            print(f"   zeta(0.5 + i*{t}) ≈ {zeta_value}")
            print(f"   Magnitude ≈ {mp.sqrt(zeta_value.real**2 + zeta_value.imag**2)}")
            print()
    except Exception as e:
        print("An error occurred:", str(e))
