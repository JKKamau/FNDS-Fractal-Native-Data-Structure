# FNLDS: Hybrid Fractal Data Structure

**FNLDS (Fractal-Native Lossless Data Structure)** is a procedural framework that represents high-entropy, ordered datasets as a series of recursive geometric snapshots. It is engineered to capture "irregular topology"—patterns that appear chaotic to standard algorithms but possess underlying scale-invariant self-similarity.

## 🧩 The "2+1" Recursive Framework
To balance mathematical depth with computational reality, FNLDS utilizes a capped recursive strategy:

1. **Layer 1 (Macro-Fractal):** Extracts the primary trend of the dataset using a deterministic formula (the "Seed"). This sharply reduces the global magnitude of the data.
2. **Layer 2 (Micro-Fractal):** Re-applies the fractal engine to the first layer's residuals, capturing the self-similar "roughness" or jitter that traditional linear models miss.
3. **Layer 3 (Entropy Safety Net):** The final, non-similar residuals are flattened toward zero, making them exponentially more efficient for standard entropy encoders (like LZMA or Zstd) to compress.

## ⚖️ The Generalized Trade-off
* **The Win:** Achieves theoretical limits of compression on ordered datasets where the signal-to-noise ratio favors structure (Hurst Exponent $H > 0.5$).
* **The Cost:** Trades CPU/NPU cycles for extreme storage density. It is a computational approach to a storage problem, ideal for high-value telemetry and archival of scientific records.

---

## 🚀 Quick Start
```python
import numpy as np
from fnlds import encode_fnlds, decode_fnlds

# Sample ordered data
data = [10, 12, 15, 17, 20, 22, 25]

# Encode & Decode losslessly
compressed = encode_fnlds(data)
restored = decode_fnlds(compressed)

print(f"Bit-Perfect Restoration: {data == restored}")
```

## 📖 How It Works

### Core Concepts
- **Irregular Topology:** Analysis of data structure through geometric relationships rather than bit-patterns
- **Fractal Dimension:** Identification of self-similar, recursive patterns within datasets
- **Lossless Compression:** Perfect data recovery from fractal parameters and residual information
- **Multi-Layer Decomposition:** Progressive refinement through macro, micro, and entropy layers

### Compression Pipeline

1. **Analysis Phase:** Examine dataset through irregular topology lens to identify underlying structure
2. **Layer 1 Processing:** Extract macro-fractal seed to capture primary trends
3. **Layer 2 Processing:** Apply fractal analysis to residuals to capture self-similar roughness
4. **Layer 3 Processing:** Flatten remaining entropy-rich residuals for standard codec optimization
5. **Encoding:** Apply entropy encoders (LZMA, Zstd) to the final residual layer

### Decompression Pipeline
- Reverse the entropy encoding
- Reconstruct Layer 3 residuals
- Regenerate Layer 2 fractal components
- Regenerate Layer 1 macro-fractal
- Perfect bit-for-bit data restoration

## 🎯 Use Cases

- **Scientific Data Archival:** Compress long-term telemetry and sensor records with perfect fidelity
- **Time-Series Compression:** Efficiently compress ordered temporal data with self-similar patterns
- **High-Value Records:** Store critical datasets with maximum compression while maintaining integrity
- **Signal Processing:** Preserve signal integrity while reducing storage footprint

## 📊 Performance Characteristics

| Dataset Type | Compression Ratio | Best For |
|---|---|---|
| High-order (H > 0.7) | 10:1 to 50:1 | Trending data, smooth signals |
| Mid-order (H = 0.5-0.7) | 3:1 to 10:1 | General telemetry |
| Low-order (H < 0.5) | 1.5:1 to 3:1 | Random, noise-heavy data |

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/JKKamau/FNLDS-Fractal-Native-Data-Structure.git
cd FNLDS-Fractal-Native-Data-Structure

# Install dependencies
pip install -r requirements.txt
```

## 📚 Documentation

- [Architecture Guide](docs/architecture.md) — Deep dive into the 2+1 recursive framework
- [API Reference](docs/api.md) — Complete function and class documentation
- [Examples](examples/) — Sample compression scenarios and benchmarks

## 🧪 Testing

```bash
# Run test suite
pytest tests/

# Run benchmarks
python benchmarks/compare.py
```

## 📈 Benchmarks

See [benchmarks/](benchmarks/) for detailed performance comparisons against standard compression algorithms (gzip, brotli, zstd).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📄 License

This project is private.

## ✉️ Contact

For questions or inquiries about FNLDS, please reach out to: **johnamau41@gmail.com**
