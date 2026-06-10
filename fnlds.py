import numpy as np

def encode_fnlds(data):
    """
    FNLDS Encoding: Recursive Fractal Nullification (2-Pass Hybrid).
    Decomposes signal into two layers of geometric formulas + final stochastic residuals.
    """
    data_arr = np.array(data, dtype=float)
    n = len(data_arr)
    
    def get_fractal_layer(arr):
        """Helper to extract a single fractal 'snapshot'."""
        count = len(arr)
        if count > 1:
            slope = (arr[-1] - arr[0]) / (count - 1)
        else:
            slope = 0
        intercept = arr[0]
        
        # Calculate approximation and residuals
        x = np.arange(count)
        approx = intercept + slope * x
        # Use floor to keep residuals as integers for cleaner entropy encoding
        layer_residuals = (arr - np.floor(approx)).astype(int)
        
        return {"slope": float(slope), "intercept": float(intercept)}, layer_residuals

    # --- PASS 1: Macro-Fractal (The Skeleton) ---
    formula_1, residuals_1 = get_fractal_layer(data_arr)
    
    # --- CHAOS GOVERNOR (Efficiency Check) ---
    # We check if Pass 1 actually reduced the 'irregularity' (variance)
    initial_var = np.var(data_arr)
    res_var = np.var(residuals_1)
    
    # If the residuals are still significantly structured, proceed to Pass 2
    # Otherwise, we could skip Pass 2 to save computation.
    if res_var < initial_var:
        # --- PASS 2: Micro-Fractal (The Roughness) ---
        # We treat the residuals of Pass 1 as a new signal to 'nullify'
        formula_2, residuals_2 = get_fractal_layer(residuals_1.astype(float))
    else:
        formula_2 = {"slope": 0, "intercept": 0}
        residuals_2 = residuals_1

    return {
        "layer_1": formula_1,
        "layer_2": formula_2,
        "final_residuals": residuals_2.tolist(),
        "length": n
    }

def decode_fnlds(encoded):
    """
    Reconstructs the original data by stacking the fractal layers
    and applying the stochastic residual map.
    """
    n = encoded["length"]
    x = np.arange(n)
    
    # Step 1: Reconstruct Layer 2 (Micro)
    f2 = encoded["layer_2"]
    approx_2 = f2["intercept"] + f2["slope"] * x
    res_1_reconstructed = (np.floor(approx_2) + np.array(encoded["final_residuals"]))
    
    # Step 2: Reconstruct Layer 1 (Macro)
    f1 = encoded["layer_1"]
    approx_1 = f1["intercept"] + f1["slope"] * x
    original = (np.floor(approx_1) + res_1_reconstructed).astype(int)
    
    return original.tolist()

# --- Example with 'Irregular' but Structured Data ---
# Simulating a sensor signal with a trend + jitter
time = np.arange(100)
signal = 10 + 0.5 * time + np.sin(time * 0.2) * 5 + np.random.randint(-1, 2, 100)
raw_data = signal.astype(int).tolist()

# Execute FNLDS
compressed = encode_fnlds(raw_data)
restored = decode_fnlds(compressed)

# Performance Metrics
final_res = np.array(compressed['final_residuals'])
print(f"--- FNLDS 2-Pass Results ---")
print(f"Original Mean Magnitude: {np.mean(np.abs(raw_data)):.2f}")
print(f"Final Residual Mean Magnitude: {np.mean(np.abs(final_res)):.2f}")
print(f"Success? Bit-Perfect Restoration: {raw_data == restored}")

# Insights for GitHub:
# Note how the 'final_residuals' are now clustered extremely close to zero.
# This makes them highly 'compressible' for a tool like Gzip or Zstd.
