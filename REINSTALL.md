# Reinstalling slurm-gres-viz to Fix Entry Point Script

The entry point script wasn't created during the initial installation. Follow these steps to fix it:

## Step 1: Uninstall the current installation

```bash
cd /fsx/byungjun/SLURM_allocated_gres_visualizer
sudo python3 -m pip uninstall -y slurm_gres_viz
```

## Step 2: Reinstall with fixed setup.py

```bash
sudo python3 -m pip install .
```

## Step 3: Verify the installation

```bash
# Check if the script was created
ls -la /usr/local/bin/slurm-gres-viz

# Or find it
sudo find /usr/local -name "slurm-gres-viz" 2>/dev/null

# Test the command
slurm-gres-viz --help
```

## Alternative: Manual Script Creation

If the script still isn't created, you can create it manually:

```bash
sudo bash -c 'cat > /usr/local/bin/slurm-gres-viz << "EOF"
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from slurm_gres_viz.main import main

if __name__ == "__main__":
    sys.exit(main())
EOF'

sudo chmod +x /usr/local/bin/slurm-gres-viz
```

## Troubleshooting

If `/usr/local/bin` is not in your PATH:

```bash
# Check your PATH
echo $PATH

# Add /usr/local/bin to PATH if needed
export PATH="/usr/local/bin:$PATH"

# Make it permanent
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

