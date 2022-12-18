#!/bin/bash
#SBATCH --mail-user=jade.m.mcdaniel@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --ntasks=4 
#SBATCH --nodes=1 
#SBATCH --time=10-00:00:00 
#SBATCH --mem=16G
#SBATCH --output=full_md_log.out

sander -O -i prod.in -o mab1.prod.out -p mab1.prmtop -c mab1.eq2.rst -r mab1.prod.rst -x mab1.prod.nc