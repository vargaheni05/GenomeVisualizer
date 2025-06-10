Welcome to GenomeVisualizer's documentation!
============================

A toolbox for detecting DNA replication origins and regulatory motifs in genomic sequences.
The toolbox includes modules for skew analysis, origin prediction, motif search, and graphical genome representation.

Current version: 0.0.2

Planned release: June 2025

Introduction
------------
GenomeVisualizer was developed to support students, researchers, and enthusiasts in exploring the structure of prokaryotic genomes.  
It provides tools to identify biologically significant regions such as replication origins (ori) and sequence motifs associated with regulatory processes.

Description
-----------
The toolbox is divided into the following modules:

- **Basic:** Simple pattern counting, frequency mapping, and file loading utilities.
- **Replication:** Tools to locate replication origin using GC-skew, Hamming distance, and approximate pattern matching.
- **Motifs:** Motif search algorithms including Greedy Motif Search, Randomized Motif Search and Gibbs Sampling.
- **Visualization:** Genome-wide plots for skew array, symbol distribution, and motif locations using matplotlib.

Web Tools
---------
We have also developed a small set of interactive web-based tools for genome analysis, you can try them here:
**https://genomevisualizer.fly.dev/**

These tools offer a simplified UI for experimenting with the core functionalities of the GenomeVisualizer package — directly in your browser.

Installation
------------
pip project: https://pypi.org/project/GenomeVisualizer/

git repository: https://github.com/vargaheni05/GenomeVisualizer

For comprehensive installation instructions and usage guidelines, please refer to the documentation:  
https://genomevisualizer.readthedocs.io/en/latest/usage.html

Requirements
------------

Python Requirements:
~~~~~~~~~~~~~~~~~~~~

Python >= 3.10

matplotlib >= 3.9.2

numpy>=1.25.2

pandas>=2.2.2

logomaker>=0.8

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
Henrietta Varga

varga.henrietta.julianna@hallgato.ppke.hu