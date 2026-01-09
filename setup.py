from setuptools import setup
import os


def read_requirements():
    """Read requirements from requirements.txt file."""
    with open('requirements.txt', 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]


required_packages = read_requirements()

setup(
    name="slurm_gres_viz",
    version="2.1.1",
    author="Hyogun Lee(Haawron)",
    author_email="gunsbrother@khu.ac.kr",
    python_requires='>=3.6',
    install_requires=required_packages,
    description="The app for visualizing allocated GPUs by SLURM",
    license="MIT",
    url="https://github.com/Haawron/SLURM_allocated_gres_visualizer",
    packages=['slurm_gres_viz'],
    package_dir={'slurm_gres_viz': 'slurm_gres_viz'},
    entry_points={
        'console_scripts' : [
            'slurm-gres-viz=slurm_gres_viz.main:main'
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
)
