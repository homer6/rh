import mpmath as mp

mp.mp.prec = 80

def zeta_magnitude(t):
    """Returns the magnitude of zeta(0.5 + i*t)."""
    val = mp.zeta(0.5 + 1j*t)
    return mp.sqrt(mp.re(val)**2 + mp.im(val)**2)

def find_zero_on_line(t_guess):
    """
    Find a zero near t_guess by minimizing the magnitude.
    """
    zero_t = mp.findroot(zeta_magnitude, t_guess)
    return zero_t

def approximate_riemann_zeros(n_zeros=5, start_guess=14.0, spacing=10.0):
    zeros_found = []
    t_guess = start_guess
    for _ in range(n_zeros):
        t_root = find_zero_on_line(t_guess)
        zeros_found.append(t_root)
        t_guess = t_root + spacing
    return zeros_found

if __name__ == "__main__":
    first_5 = approximate_riemann_zeros()
    for i, zt in enumerate(first_5, 1):
        print(f"Zero #{i} near t = {zt}")
        val = mp.zeta(0.5 + 1j*zt)
        print(f"   zeta(0.5 + i*{zt}) = {val}")
        print(f"   Magnitude = {mp.sqrt(val.real**2 + val.imag**2)}")
        print()
