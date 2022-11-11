#!/bin/bash
#SBATCH --job-name=run-3dWCA
#SBATCH --nodes=1
#SBATCH --tasks-per-node=4
#SBATCH --cpus-per-task=1
#SBATCH --mem=8GB
#SBATCH --time=10:00:00
##SBATCH --gres=gpu:1 ## TO ask for a gpu, remove #
source /scratch/work/courses/CHEM-GA-2671-2022fa/software/lammps-gcc-30Oct2022/setup_lammps.bash
for i in 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5
do
        mpirun lmp -var density $i -in ./3dWCA.in -log LOGFILE$i.log
done
