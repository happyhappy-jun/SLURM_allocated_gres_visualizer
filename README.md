# SLURM_allocated_gres_visualizer
**The app for visualizing allocated GPUs by SLURM**

![image](https://user-images.githubusercontent.com/25451196/222977415-c8b992e6-d46d-4856-9a26-558505e64956.png)

When you are using Slurm and you want to check which gpus are allocated, you must have done something like
- `ssh` to each computing node and run `nvidia-smi`. Then, repeat it.
- Run `scontrol show job -d | grep GRES` and roll your eyeballs.


both of which are very tedious. This project can solve this.

# Requirements

## Packages
- matplotlib
- sty
- prometheus-client
- requests
- pandas
- bs4

## Slurm
- Be sure that `slurmctld`(master) and `slurmd`(nodes) are active so that there are no problems for running `scontrol show nodes` or `scontrol show job`.
- Be sure that `AutoDetect=nvml` for all computing nodes to avoid GPU index mismatch.
- For all computing nodes, `node-exporter` are available at port `9100` and `dcgm-exporter` at `9400`.

# Installation

## System-wide Installation (Recommended)

For system-wide installation that makes `slurm-gres-viz` available to all users:

```bash
git clone https://github.com/happyhappy-jun/SLURM_allocated_gres_visualizer.git
cd SLURM_allocated_gres_visualizer

# Option 1: Using pip (recommended, modern approach)
sudo pip3 install .

# Option 2: Using pip with editable mode (for development)
sudo pip3 install -e .

# Option 3: Build and install wheel (most reliable)
pip3 install build
python3 -m build
sudo pip3 install dist/slurm_gres_viz-*.whl
```

## User-level Installation (No sudo required)

If you don't have sudo access or want to install only for your user:

```bash
git clone https://github.com/happyhappy-jun/SLURM_allocated_gres_visualizer.git
cd SLURM_allocated_gres_visualizer

# Install to user directory (~/.local/bin)
pip3 install --user .

# Make sure ~/.local/bin is in your PATH
export PATH="$HOME/.local/bin:$PATH"
# Add to ~/.bashrc or ~/.profile for persistence:
# echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

## Virtual Environment Installation (Isolated)

For isolated installation in a virtual environment:

```bash
git clone https://github.com/happyhappy-jun/SLURM_allocated_gres_visualizer.git
cd SLURM_allocated_gres_visualizer

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package
pip install .

# The command will be available while venv is activated
```

## Important Notes

- **Avoid conda environment**: Make sure you're using system Python or a virtual environment, not conda, when installing system-wide
- **Python version**: Requires Python 3.6 or higher
- **Dependencies**: All dependencies will be installed automatically
- **Entry point**: The `slurm-gres-viz` command will be available in your PATH after installation

# Usage
```bash
slurm-gres-viz

# GPU options
slurm-gres-viz -i  # stars are replaced to indices
slurm-gres-viz -gm -gu  # VRAM and GPU util
slurm-gres-viz -f  # Full information of GPUs
slurm-gres-viz -m  # mine: shows only my GPUs

# others
slurm-gres-viz -l 1  # looping every 1 second (same as nvidia-smi)
```

