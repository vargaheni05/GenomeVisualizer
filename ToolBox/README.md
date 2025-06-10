# GenomeVisualizer - A toolbox for detecting DNA replication origins and regulatory motifs in genomic sequences

A toolbox for detecting DNA replication origins and regulatory motifs in genomic sequences.
The toolbox includes modules for skew analysis, origin prediction, motif search, and graphical genome representation.

---

### Current Version: `0.0.2`  
### Planned Release: June 2025  

---

## Introduction  

`GenomeVisualizer` was developed to support students, researchers, and enthusiasts in exploring the structure of prokaryotic genomes.  
It provides tools to identify biologically significant regions such as replication origins (ori) and sequence motifs associated with regulatory processes like circadian rhythms.

---

## Description  

The toolbox is divided into the following modules:

- **Basic:**  
  - Simple pattern counting, frequency mapping, and file loading utilities.

- **Replication:**  
  - Tools to locate replication origin using GC-skew, Hamming distance, and approximate pattern matching.

- **Motifs:**  
  - Motif search algorithms including Greedy Motif Search, Randomized Motif Search and Gibbs Sampling.

- **Visualization:**  
  - Genome-wide plots for skew array, symbol distribution, and motif locations using matplotlib.

---

**For more information, visit the [official documentation](https://genomevisualizer.readthedocs.io/en/latest/)**.


## Installation
### From PyPi
Install `GenomeVisualizer` using pip

```
pip install GenomeVisualizer
```

### From source
Clone the git repository
```
git clone "https://github.com/vargaheni05/GenomeVisualizer.git"
```
Change directory to the cloned repository
```
cd GenomeVisualizer/Toolbox
```
Install with pip
```
pip install .
```

## Building the documentation
Install required packages
```
pip install -r docs/requirements.txt
```
Call Sphinx build command
```
sphinx-build -M html docs/source docs/build
```
On Windows you can also run the `make.bat` file
```
.\docs\make.bat html
```

The documentation should be available in the `docs/build` directory as html files<br>
This includes the example codes as tutorials

## Correspondence
Henrietta Varga (varga.henrietta.julianna@hallgato.ppke.hu)