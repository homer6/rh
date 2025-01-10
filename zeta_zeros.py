import mpmath as mp

def f_2d(u):
    """
    Here, u is a 1-element list or tuple [t].
    Return [re(zeta(0.5 + i*t)), im(zeta(0.5 + i*t))]
    """
    t = u[0]
    val = mp.zeta(0.5 + 1j*t)
    return [mp.re(val), mp.im(val)]

def find_zero_2d(t_guess):
    # We supply [t_guess] as the initial 1D "vector"
    zero_list = mp.findroot(f_2d, [t_guess], method='hybrid')
    # The result is typically a list (or tuple)
    return zero_list[0]

if __name__ == "__main__":
    mp.mp.prec = 80
    t_approx = find_zero_2d(14.0)
    print("Zero found near t =", t_approx)
