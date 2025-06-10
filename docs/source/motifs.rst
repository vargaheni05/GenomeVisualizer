Motifs Module
===========================

This module provides algorithms and utilities for identifying conserved DNA motifs across multiple sequences.  
It includes both deterministic and stochastic methods for motif detection, scoring, and probabilistic modeling.

Basic Functions
---------------

.. autofunction:: GenomeVisualizer.motifs.Count
.. autofunction:: GenomeVisualizer.motifs.Profile
.. autofunction:: GenomeVisualizer.motifs.Consensus
.. autofunction:: GenomeVisualizer.motifs.Score

Profile Evaluation
------------------

.. autofunction:: GenomeVisualizer.motifs.Pr
.. autofunction:: GenomeVisualizer.motifs.ProfileMostProbableKmer
.. autofunction:: GenomeVisualizer.motifs.Motifs

Motif Search Algorithms
------------------------

Greedy Search:

.. autofunction:: GenomeVisualizer.motifs.GreedyMotifSearch
.. autofunction:: GenomeVisualizer.motifs.GreedyMotifSearchWithPseudocounts

Randomized Algorithms:

.. autofunction:: GenomeVisualizer.motifs.RandomizedMotifSearch
.. autofunction:: GenomeVisualizer.motifs.GibbsSampler

Pseudocount Utilities
---------------------

.. autofunction:: GenomeVisualizer.motifs.CountWithPseudocounts
.. autofunction:: GenomeVisualizer.motifs.ProfileWithPseudocounts

Probabilistic Sampling Tools
----------------------------

.. autofunction:: GenomeVisualizer.motifs.RandomMotifs
.. autofunction:: GenomeVisualizer.motifs.Normalize
.. autofunction:: GenomeVisualizer.motifs.WeightedDie
.. autofunction:: GenomeVisualizer.motifs.ProfileGeneratedString