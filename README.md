# Diffusion Limited Aggregation
## Second year university project
### Overview
This project implements a 3D Diffusion-Limited Accretion (DLA) simulation using a stochastic random-walk model.

DLA is a particle aggregation process that produces fractal growth structures. It is commonly used to model:
- Crystal growth
- Electrodeposition
- Dielectric breakdown
- Mineral aggregation
- Biological branching structures

The simulation generates a 3D lattice by sequentially releasing particles from a spherical boundary and allowing them to undergo random walks until they attach to an existing cluster.

### Mathematical Background
Each particle:
1. Is initialised on a sphere of radius 
2. Performs a discrete random walk:

$$(x, y, z) = (x + \Delta x, y + \Delta y, z + \Delta z)$$

where:

$$\Delta x, \Delta y, \Delta z, \in [-1, 0, 1]$$

3. Aggregates when the minimum squared Euclidean distance to the cluster satisfies:

$$min[(x-x_i)^2 + (y-y_i)^2 + (z-z_i)^2] \leq 1$$

The cluster grows dynamically. The bounding sphere radius increases when a particle attaches to the boundary.

### Features
- 3D random walk particle simulation
- Dynamic growth boundary resizing
- Cluster visualisation using matplotlib
- Output of particle coordinates for further analysis
- Post-processing via DLAnalysis module
- Runtime measurement

### Project Structure
```
Diffusion Limited Accretion/
│
├── DLA2D.py              # Main 2D simulation
├── DLA3D.py              # Main 3D simulation
├── DLAnalysis.py         # Fractal / structural analysis
├── analysis.py           # Additional processing utilities
├── runner.py             # Execution wrapper
│
├── DLA3D_data.py         # Generated particle coordinate output
├── DLA3D_<seed>_<N>.png  # Generated 3D cluster image
├── DLA2D_<seed>_<N>.png  # Generated 2D cluster image
│
├── Useful files          # Extra files used during the project
└── Others works/         # Related articles and Example DLA
```

### Parameters
```
N = 10000     # Number of particles
seed = 0      # Random seed
```

- Increasing N increases cluster complexity but increases runtime significantly.
- Computational complexity grows approximately $O(N^2) due to distance comparisons.

### Example Output
The simulation produces a 3D fractal-like aggregation pattern.
- Colour mapping reflects radial distance from the origin.
- The final image is saved as: DLA3D<seed>_<N>.png

### Dependencies
- Python 3.x
- NumPy
- Matplotlib
- mpl_toolkits.mplot3d

Install required packages:

```bash
pip install numpy matplotlib
```

### Skills Demonstrated
- Stochastic modelling
- Monte Carlo simulation
- 3D and 2D coordinate transformations
- Algorithmic design
- Computational physics
- Performance considerations in iterative simulations
- Scientific visualisation
- Modular analysis design

### Performance Notes

For $N = 10,000$:

- Runtime depends heavily on hardware.
- The primary bottleneck is repeated distance calculation across existing lattice points.

Per particle, the algorithm performs approximately: $$O(N)$$

Total worst-case complexity: $$O(N²)$$

Optimisation opportunities include:

- Spatial partitioning (k-d trees or voxel grids)
- Neighbour lists
- Numba acceleration
- Parallel random walk simulation

### How to Run

Clone the repository and run: python DLA3D.py

The script:
1. Runs the simulation
2. Saves the output image
3. Writes particle coordinates to `DLA3D_data.py`
4. Performs structural analysis via `DLAnalysis3D`


### Possible Extensions

- Estimate fractal dimension using mass–radius scaling:

$$M(r) ∝ r^D$$

- Implement spatial acceleration structures
- Parallelise random walk updates
- Compare 2D vs 3D fractal dimensions
- Port simulation to GPU (CUDA / PyTorch)
- Convert to continuous Brownian motion
