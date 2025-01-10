import mpmath as mp

# Increase working precision as needed (default is 53 bits ~ 15-16 decimals)
mp.mp.prec = 80

def find_zero_on_line(t_guess):
    """
    Use mp.findroot to locate a zero of zeta(0.5 + i*t) 
    near the imaginary axis guess 't_guess'.
    """
    # We pass a function that returns BOTH the real and imaginary parts
    # of zeta(0.5 + i t). We want them both to be zero simultaneously.
    f_real = lambda t: mp.re(mp.zeta(0.5 + t*1j))
    f_imag = lambda t: mp.im(mp.zeta(0.5 + t*1j))
    
    # We do a 2D root find using the built-in 'findroot' with a starting tuple (t_guess, t_guess+0.1).
    # In 2D, findroot expects a tuple of functions and a tuple of initial guesses.
    # We only have a single variable t, so we pass the same guess for both.
    zero_t = mp.findroot([f_real, f_imag], (t_guess, t_guess + 0.1))
    return zero_t

def approximate_riemann_zeros(n_zeros=5, start_guess=14.0, spacing=10.0):
    """
    Find a few zeros of the Riemann zeta function on the critical line.
    
    :param n_zeros:  how many zeros to attempt to locate
    :param start_guess: the imaginary part guess for the first zero
    :param spacing:   how far apart each guess is for subsequent zeros
    :return:          list of approximate zeros [t_1, t_2, ...]
    """
    zeros_found = []
    t_guess = start_guess
    
    for _ in range(n_zeros):
        # Find zero near t_guess
        t_root = find_zero_on_line(t_guess)
        zeros_found.append(t_root)
        
        # Update guess for the next zero
        # Usually the zeros lie increasingly higher, so we bump the guess.
        t_guess = t_root + spacing
    
    return zeros_found

if __name__ == "__main__":
    # Let's try to find the first 5 nontrivial zeros
    # Known approximate imaginary parts of first few zeros:
    # 14.134725..., 21.022040..., 25.010856..., 30.424876..., 32.935061...
    
    first_5 = approximate_riemann_zeros(n_zeros=5,
                                        start_guess=14.0,
                                        spacing=10.0)
    for i, zt in enumerate(first_5, 1):
        print(f"Zero #{i} near t = {zt}")
        val = mp.zeta(0.5 + zt*1j)
        print(f"   zeta(0.5 + i*{zt}) ≈ {val}")
        print()
