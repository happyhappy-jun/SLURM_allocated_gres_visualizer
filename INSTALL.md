# Installation Guide

This guide provides detailed instructions for installing `slurm_gres_viz` system-wide or for individual users.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- System access (for system-wide installation) or user directory write access (for user installation)
- SLURM cluster access

## Installation Methods

### Method 1: System-wide Installation (Recommended for Multi-user Systems)

This method installs the package system-wide, making it available to all users.

```bash
# Clone the repository
git clone https://github.com/Haawron/SLURM_allocated_gres_visualizer.git
cd SLURM_allocated_gres_visualizer

# Install system-wide (requires sudo)
sudo pip3 install .

# Verify installation
slurm-gres-viz --help
```

**Advantages:**
- Available to all users on the system
- Single installation point
- Easier to maintain

**Disadvantages:**
- Requires sudo/root access
- May conflict with system package managers

### Method 2: User-level Installation (No sudo required)

This method installs the package in your home directory.

```bash
# Clone the repository
git clone https://github.com/Haawron/SLURM_allocated_gres_visualizer.git
cd SLURM_allocated_gres_visualizer

# Install to user directory
pip3 install --user .

# Add to PATH if not already there
export PATH="$HOME/.local/bin:$PATH"

# Make it permanent (add to ~/.bashrc or ~/.profile)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify installation
slurm-gres-viz --help
```

**Advantages:**
- No sudo required
- User-specific installation
- Doesn't affect system Python

**Disadvantages:**
- Each user needs to install separately
- Requires PATH configuration

### Method 3: Virtual Environment Installation (Isolated)

This method creates an isolated Python environment.

```bash
# Clone the repository
git clone https://github.com/Haawron/SLURM_allocated_gres_visualizer.git
cd SLURM_allocated_gres_visualizer

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package
pip install .

# Verify installation
slurm-gres-viz --help

# To use later, reactivate the virtual environment
source venv/bin/activate
```

**Advantages:**
- Complete isolation from system Python
- No conflicts with other packages
- Easy to remove (just delete venv directory)

**Disadvantages:**
- Must activate environment before use
- Not available system-wide

### Method 4: Build and Install Wheel (Most Reliable)

This method builds a wheel package first, then installs it.

```bash
# Clone the repository
git clone https://github.com/Haawron/SLURM_allocated_gres_visualizer.git
cd SLURM_allocated_gres_visualizer

# Install build tool
pip3 install build

# Build wheel package
python3 -m build

# Install the wheel (system-wide)
sudo pip3 install dist/slurm_gres_viz-*.whl

# Or install for user only
pip3 install --user dist/slurm_gres_viz-*.whl
```

**Advantages:**
- Most reliable installation method
- Can distribute the wheel file
- Faster reinstallation

**Disadvantages:**
- Extra build step required

## Troubleshooting

### Command not found after installation

1. **Check installation location:**
   ```bash
   pip3 show -f slurm_gres_viz | grep Location
   ```

2. **Find the executable:**
   ```bash
   python3 -m pip show -f slurm_gres_viz | grep -E "slurm-gres-viz"
   ```

3. **Check PATH:**
   ```bash
   echo $PATH
   ```

4. **Add to PATH if needed:**
   - For user installation: `export PATH="$HOME/.local/bin:$PATH"`
   - For system installation: Usually in `/usr/local/bin` or `/usr/bin`

### Conda environment conflicts

If you're using conda, make sure to deactivate it before installation:

```bash
conda deactivate
# Then proceed with installation using system Python
/usr/bin/python3 -m pip install .
```

### Permission errors

- Use `--user` flag for user-level installation
- Or use `sudo` for system-wide installation
- Check file permissions on installation directory

### Uninstall

```bash
# System-wide
sudo pip3 uninstall slurm_gres_viz

# User-level
pip3 uninstall slurm_gres_viz
```

## Verification

After installation, verify it works:

```bash
# Check version (if available)
slurm-gres-viz --version

# Run the tool
slurm-gres-viz

# Check help
slurm-gres-viz --help
```

## Updating

To update to a newer version:

```bash
cd SLURM_allocated_gres_visualizer
git pull
pip3 install --upgrade .  # or sudo pip3 install --upgrade .
```

