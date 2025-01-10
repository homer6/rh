import mpmath as mp
import time

# Increase precision for accuracy (80 bits = ~24 decimals)
mp.mp.prec = 80

def zeta_magnitude(t):
    """
    Returns the magnitude of zeta(0.5 + i*t).
    Used to identify zeros along the critical line.
    """
    val = mp.zeta(0.5 + 1j * t)
    return mp.sqrt(mp.re(val)**2 + mp.im(val)**2)

def find_zero_on_line(t_guess):
    """
    Finds a zero of zeta(0.5 + i*t) near the guess 't_guess'.
    Uses mpmath's findroot function.
    """
    zero_t = mp.findroot(zeta_magnitude, t_guess, solver='mnewton')  # Modified Newton's method
    return zero_t

def validate_zero(t):
    """
    Validates whether a zero found at t lies on the critical line.
    Returns True if the zero is valid (on the critical line), False otherwise.
    """
    val = mp.zeta(0.5 + 1j * t)
    if abs(val) > 1e-10:
        return False  # Magnitude should be close to 0
    return True

def log_progress(zeros_found, start_time):
    """
    Logs the progress of the computation to the console.
    """
    elapsed_time = time.time() - start_time
    print(f"\nProgress Update:")
    print(f"  Zeros Found: {len(zeros_found)}")
    print(f"  Last Zero: t ≈ {zeros_found[-1] if zeros_found else 'None'}")
    print(f"  Elapsed Time: {elapsed_time:.2f} seconds\n")

def save_progress(zeros_found, filename="zeros_found.txt"):
    """
    Saves the progress (zeros found so far) to a file.
    """
    with open(filename, "w") as f:
        for t in zeros_found:
            f.write(f"{t}\n")

def run_long_computation(n_zeros_target=100, start_guess=14.0, spacing=10.0, save_interval=10):
    """
    Runs a long computation to find zeros of the Riemann zeta function on the critical line.
    
    :param n_zeros_target: Number of zeros to find before stopping (use -1 for infinite loop)
    :param start_guess: Starting guess for the first zero's imaginary part
    :param spacing: Increment to guess the next zero (approximate range)
    :param save_interval: Save progress to a file every 'save_interval' zeros
    """
    zeros_found = []
    t_guess = start_guess
    start_time = time.time()
    iteration = 0

    try:
        while n_zeros_target == -1 or len(zeros_found) < n_zeros_target:
            iteration += 1
            
            # Find the next zero near the current guess
            t_root = find_zero_on_line(t_guess)
            
            # Validate the zero is on the critical line
            if not validate_zero(t_root):
                print(f"\nRelevant Discovery: Found a zero not on the critical line!")
                print(f"  Imaginary part: t ≈ {t_root}")
                print(f"  Magnitude of zeta(0.5 + i*{t_root}): {zeta_magnitude(t_root)}")
                print("Stopping computation.")
                break
            
            # Add the zero to the list and update the guess for the next zero
            zeros_found.append(t_root)
            t_guess = t_root + spacing

            # Periodic logging
            if iteration % save_interval == 0:
                log_progress(zeros_found, start_time)
                save_progress(zeros_found)

    except KeyboardInterrupt:
        print("\nComputation interrupted by user.")
    
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
    
    # Final save and summary
    save_progress(zeros_found)
    print("\nFinal Progress:")
    print(f"  Total Zeros Found: {len(zeros_found)}")
    if zeros_found:
        print(f"  Last Zero: t ≈ {zeros_found[-1]}")
    print(f"Results saved to 'zeros_found.txt'.")

if __name__ == "__main__":
    print("Finding zeros of the Riemann zeta function on the critical line...")
    run_long_computation(n_zeros_target=-1, start_guess=14.0, spacing=10.0, save_interval=10)
