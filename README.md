# dual-migration

This repository provides code for 
- simulating the evolution equation and
- visualizing the results of eigenvalue analysis

in the following paper. I would appreciate your citing the following paper when you publish your results using this code.

Ohtake, K. (2024). City formation by dual migration of firms and workers. arXiv preprint arXiv:2311.05292.  
https://doi.org/10.48550/arXiv.2311.05292

# Overview

## dual_migration.ipynb  
This is code for simulating the evolution equation proposed in this paper.  
In the second cell, specify the values of $\tau>0$ (transport cost index) as the list used in the outer loop.  
Then, specify the parameter $\sigma>1$ (elasticity of substitution) in the list used in the inner loop.  
For a set of parameters, five simulations are performed for randomly generated initial values.  

Language: 
Julia ver 1.11.4  
Packages:  
CSV ver. 0.10.15  
DataFrames ver. 1.7.0  
Distributions ver. 0.25.118  
Format ver. 1.3.7  
IJulia ver. 1.26.0  
Plots ver. 1.40.11  

## eigenvalue_plot.py
This is code for computing and plotting eigenvalues of the linearized problem.  

Language: Python ver 3.12.4  
Packages:  
numpy 2.3.5  
matplotlib ver 3.10.7    
seaborn 0.13.2
