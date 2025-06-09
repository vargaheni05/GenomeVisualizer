Welcome to GenomeVisualizer's documentation!
============================

A toolbox for detecting DNA replication origins and regulatory motifs in genomic sequences.
The toolbox includes modules for skew analysis, origin prediction, motif search, and graphical genome representation.

Current version: 0.0.1

Planned release: June 2025

Introduction
------------
GenomeVisualizer was developed to support students, researchers, and enthusiasts in exploring the structure of prokaryotic genomes.  
It provides tools to identify biologically significant regions such as replication origins (ori) and sequence motifs associated with regulatory processes like circadian rhythms.

Description
-----------
The toolbox is divided into the following modules:

- **Basic:** Simple pattern counting, frequency mapping, and file loading utilities.
- **Replication:** Tools to locate replication origin using GC-skew, Hamming distance, and approximate pattern matching.
- **Motifs:** Motif search algorithms including Greedy Motif Search and Gibbs Sampling.
- **Visualization:** Genome-wide plots for skew array, symbol distribution, and motif locations using matplotlib.

Datasets
--------


Installation
------------
pip project: https://pypi.org/project/GenomeVisualizer/

git repository: "https://github.com/vargaheni05/GenomeVisualizer"

For comprehensive installation instructions and usage guidelines, please refer to the documentation:  
LINK

Requirements
------------

Python Requirements:
~~~~~~~~~~~~~~~~~~~~

Python >= 3.10

matplotlib >= 3.9.2

All the python requirements are installed when the toolbox is installed, so there is no need for any additional commands.

Documentation
--------------

https://genomevisualizer.readthedocs.io/en/latest/

.. toctree::
   usage
   basic
   replication
   motifs
   visualization
   :maxdepth: 2
   :caption: Contents:

.. toctree::
   :caption: Tutorials:
   :maxdepth: 1

   example

Correspondence
--------------
Henrietta Varga PPCU-ITK, Budapest, Hungary

varga.henrietta.julianna@hallgato.ppke.hu