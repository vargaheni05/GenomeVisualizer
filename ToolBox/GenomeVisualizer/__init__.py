from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("GenomeVisualizer")
except PackageNotFoundError:
    __version__ = "0.0.1"

from .motifs import Count, Profile, Consensus, Score, Pr, ProfileMostProbableKmer, GreedyMotifSearch, CountWithPseudocounts, ProfileWithPseudocounts, GreedyMotifSearchWithPseudocounts, Motifs, RandomMotifs, RandomizedMotifSearch, Normalize, WeightedDie, ProfileGeneratedString, GibbsSampler
from .replication import PatternCount, Reverse, Complement, ReverseComplement, PatternMatching, FasterSymbolArray, SkewArray, MinimumSkew, HammingDistance, ApproximatePatternMatching, ApproximatePatternCount, FrequencyMap, FrequentWords
#from .visualization import 

__all__ = [
    # Motifs
    "Count", "Profile", "Consensus", "Score", "Pr", "ProfileMostProbableKmer",
    "GreedyMotifSearch", "CountWithPseudocounts", "ProfileWithPseudocounts",
    "GreedyMotifSearchWithPseudocounts", "Motifs", "RandomMotifs",
    "RandomizedMotifSearch", "Normalize", "WeightedDie",
    "ProfileGeneratedString", "GibbsSampler",
    # Replication
    "PatternCount", "Reverse", "Complement", "ReverseComplement",
    "PatternMatching", "FasterSymbolArray", "SkewArray", "MinimumSkew",
    "HammingDistance", "ApproximatePatternMatching", "ApproximatePatternCount",
    "FrequencyMap", "FrequentWords",
    # Visualization

    # Meta
    "__version__",
]