# A helper file to remove checkpoints until we figure out a solution
from glob import glob
from shutil import rmtree
chkpoints = glob('./**/.ipynb_checkpoints', recursive=True)
for ichk in chkpoints:
    rmtree(ichk)