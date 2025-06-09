Replication Module
==================

This module provides functions for analyzing DNA sequences to detect replication origins (ori),
based on GC-skew, pattern matching, and approximate motif searches.

Pattern-based Functions
-----------------------

.. autofunction:: GenomeVisualizer.replication.PatternCount
.. autofunction:: GenomeVisualizer.replication.PatternMatching
.. autofunction:: GenomeVisualizer.replication.Reverse
.. autofunction:: GenomeVisualizer.replication.Complement
.. autofunction:: GenomeVisualizer.replication.ReverseComplement

GC-Skew and Symbol Analysis
---------------------------

.. autofunction:: GenomeVisualizer.replication.SkewArray
.. autofunction:: GenomeVisualizer.replication.MinimumSkew
.. autofunction:: GenomeVisualizer.replication.FasterSymbolArray

Distance and Approximate Matching
---------------------------------

.. autofunction:: GenomeVisualizer.replication.HammingDistance
.. autofunction:: GenomeVisualizer.replication.ApproximatePatternMatching
.. autofunction:: GenomeVisualizer.replication.ApproximatePatternCount