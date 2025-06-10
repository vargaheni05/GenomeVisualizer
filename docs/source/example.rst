Example Usage
=============

Interactive Colab Notebook
---------------------------

For an interactive demonstration of the GenomeVisualizer toolbox, visit the Colab notebook:

.. raw:: html

   <a href="" target="_blank">Colab Notebook</a>


Data Handling
-------------

The ``basic.py`` module offers utility functions for loading and analyzing genome sequences. These are used as the foundation for further analytical steps in replication analysis and motif detection.

**Steps:**

1. Load genome data from plain text.
2. Perform basic k-mer frequency analysis.
3. Identify most frequent substrings.

.. code-block:: python

   from GenomeVisualizer.basic import load_genome_from_txt, FrequencyMap, FrequentWords

   # Load genome
   genome = load_genome_from_txt("data/ecoli.txt")

   # Count k-mer frequencies
   freq_map = FrequencyMap(genome, 10)

   # Most frequent 10-mers
   print(FrequentWords(genome, 10))


Replication Analysis
--------------------

The ``replication.py`` module supports analysis related to DNA replication, including skew diagrams and symbol frequency plots that help infer the origin of replication (oriC).

**Steps:**

1. Compute skew array to estimate origin of replication.
2. Plot skew profile and symbol frequency variations.

.. code-block:: python

   from GenomeVisualizer.replication import SkewArray, MinimumSkew, FasterSymbolArray
   from GenomeVisualizer.visualization import plot_skew_array_with_ori, plot_symbol_array

   # Skew analysis
   skew = SkewArray(genome)
   ori_positions = MinimumSkew(genome)
   plot_skew_array_with_ori(skew, ori_positions, genome_label="E. coli")

   # Symbol frequency analysis
   symbol_array = FasterSymbolArray(genome, "C")
   plot_symbol_array(symbol_array, "C", genome_label="E. coli")


Motif Analysis
--------------

The ``motifs.py`` module contains implementations for motif finding algorithms such as Greedy Motif Search, Randomized Motif Search, and Gibbs Sampling. It also includes motif scoring and profile matrix utilities.

**Steps:**

1. Run Greedy or Gibbs-based motif search.
2. Generate motif profile.
3. Visualize motif conservation.

.. code-block:: python

   from GenomeVisualizer.motifs import GreedyMotifSearchWithPseudocounts, GibbsSampler
   from GenomeVisualizer.visualization import plot_motiflogo

   Dna = [
       "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
       "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
       "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
       "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
       "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
   ]

   # Run Gibbs Sampler
   motifs = GibbsSampler(Dna, 8, 5, 100)
   print("Best motifs:", motifs)

   # Plot motif logo
   plot_motiflogo(motifs)

**Explanation:**

The algorithms return candidate motifs that are most conserved across DNA sequences. Visualization with a sequence logo reveals information-rich regions.

This walkthrough demonstrates how GenomeVisualizer can support DNA replication analysis and motif discovery with robust utilities and clear visualizations. For hands-on exploration, check the Colab link above.