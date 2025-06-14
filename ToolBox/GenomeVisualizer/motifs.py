import random

def Count(Motifs: list[str]) -> dict[str, list[int]]:
    """
    Counts the occurrences of each nucleotide at every position in a list of motifs.

    This function constructs a count matrix from a list of equal-length DNA strings (motifs),
    where each entry `count[symbol][j]` represents the number of times nucleotide `symbol`
    (A, C, G, or T) appears in position `j` across all motifs.

    Args:
        Motifs (list[str]): A list of DNA strings (motifs) of equal length.

    Returns:
        dict[str, list[int]]: A dictionary with keys 'A', 'C', 'G', 'T', and values as lists of counts for each position.

    Example:
        >>> Count(["ATG", "ACG", "AAG", "AGG", "ATG"])
        {'A': [5, 0, 0],
         'C': [0, 1, 0],
         'G': [0, 1, 5],
         'T': [0, 3, 0]}
    """
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Profile(Motifs: list[str]) -> dict[str, list[float]]:
    """
    Computes the profile matrix of a list of motifs.

    The profile matrix is a normalized version of the count matrix, where each entry 
    `profile[symbol][j]` represents the frequency of nucleotide `symbol` at position `j`
    across all motifs. The values are computed as relative frequencies (i.e., between 0 and 1).

    Args:
        Motifs (list[str]): A list of DNA strings (motifs) of equal length.

    Returns:
        dict[str, list[float]]: A dictionary with keys 'A', 'C', 'G', 'T', and values as lists of 
        nucleotide frequencies at each position.

    Example:
        >>> Profile(["ATG", "ACG", "AAG", "AGG", "ATG"])
        {'A': [1.0, 0.0, 0.0],
         'C': [0.0, 0.2, 0.0],
         'G': [0.0, 0.2, 1.0],
         'T': [0.0, 0.6, 0.0]}
    """
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile = Count(Motifs)
    for i in profile:
        for j in range(k):
            profile[i][j]/=t
    return profile

def Consensus(Motifs: list[str]) -> str:
    """
    Determines the consensus string from a list of motifs.

    The consensus string is formed by selecting the most frequent nucleotide at each position
    across all motifs. It summarizes the most likely motif pattern present in the input sequences.

    Args:
        Motifs (list[str]): A list of DNA strings (motifs) of equal length.

    Returns:
        str: The consensus DNA string formed from the most common nucleotides at each position.

    Example:
        >>> Consensus(["ATG", "ACG", "AAG", "AGG", "ATG"])
        'ATG'
    """
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs: list[str]) -> int:
    """
    Calculates the total score of a set of motifs based on their similarity to the consensus.

    The score is defined as the total number of mismatches between each motif and the consensus string.
    A lower score indicates a more conserved motif set, while a higher score indicates greater variability.

    Args:
        Motifs (list[str]): A list of DNA strings (motifs) of equal length.

    Returns:
        int: The total number of mismatches compared to the consensus across all positions and motifs.

    Example:
        >>> Score(["ATG", "ACG", "AAG", "AGG", "ATG"])
        3
    """
    consensus=Consensus(Motifs)
    score = 0
    k = len(Motifs[0])
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            if Motifs[i][j] != consensus[j]:
                score += 1
    return score

def Pr(Text: str, Profile: dict[str, list[float]]) -> float:
    """
    Computes the probability of a DNA string given a profile matrix.

    This function calculates the probability that the given DNA string `Text` 
    was generated by the given profile matrix. It multiplies the corresponding 
    probabilities from the profile for each nucleotide at each position.

    Args:
        Text (str): A DNA string (motif) of length k.
        Profile (dict[str, list[float]]): A profile matrix containing nucleotide probabilities at each position, with keys 'A', 'C', 'G', 'T'.

    Returns:
        float: The probability of the motif according to the profile.

    Example:
        >>> profile = {
        ...     'A': [0.2, 0.2, 0.3],
        ...     'C': [0.4, 0.3, 0.1],
        ...     'G': [0.3, 0.3, 0.4],
        ...     'T': [0.1, 0.2, 0.2]
        ... }
        >>> Pr("ACG", profile)
        0.2 * 0.3 * 0.4 = 0.024
    """
    p = 1
    for i in range(len(Text)):
        p=p*Profile[Text[i]][i]
    return p

def ProfileMostProbableKmer(text: str, k: int, profile: dict[str, list[float]]) -> str:
    """
    Finds the most probable k-mer in a DNA sequence based on a given profile matrix.

    Given a DNA string `text`, an integer `k`, and a 4 x k profile matrix,
    this function finds the k-mer in `text` that is most likely to have been
    generated by the profile. In the case of a tie (multiple k-mers with equal maximum probability),
    the function returns the first one that occurs in `text`.

    Args:
        text (str): The DNA sequence to search within.
        k (int): The length of the k-mers.
        profile (dict[str, list[float]]): A profile matrix containing nucleotide probabilities at each position (keys: 'A', 'C', 'G', 'T').

    Returns:
        str: The k-mer from the input `text` that has the highest probability based on the profile.

    Example:
        >>> profile = {
        ...     'A': [0.2, 0.2, 0.3, 0.2, 0.3],
        ...     'C': [0.4, 0.3, 0.1, 0.5, 0.1],
        ...     'G': [0.3, 0.3, 0.5, 0.2, 0.4],
        ...     'T': [0.1, 0.2, 0.1, 0.1, 0.2]
        ... }
        >>> text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
        >>> ProfileMostProbableKmer(text, 5, profile)
        'CCGAG'
    """
    most_probable=""
    most_probable_value=-1
    for i in range(len(text)-k+1):
        k_mer=text[i:(i+k)]
        k_mer_probability=Pr(k_mer, profile)
        if(k_mer_probability > most_probable_value):
            most_probable_value = k_mer_probability
            most_probable = k_mer
    return most_probable

def GreedyMotifSearch(Dna: list[str], k: int, t: int) -> list[str]:
    """
    Finds the best-scoring collection of motifs across multiple DNA strings using the greedy motif search algorithm.

    This function implements the classic GreedyMotifSearch algorithm, which iteratively selects the most probable k-mer 
    in each string based on a profile matrix built from previously selected motifs. The search is initialized by 
    trying every possible k-mer from the first DNA string.

    At each iteration, a new profile is built from the existing motifs, and the next string contributes its 
    most probable k-mer according to that profile. The score of the resulting motif set is compared to the 
    current best, and updated if an improvement is found.

    Args:
        Dna (list[str]): A list of `t` DNA strings (all of equal length).
        k (int): The length of the motif to search for.
        t (int): The number of DNA strings.

    Returns:
        list[str]: A list of `t` k-mers (one from each string), representing the best motif set found.

    Notes:
        - In case of ties in the profile-most probable k-mer selection, the leftmost occurrence is chosen.
        - This basic version does not include pseudocounts; therefore, the presence of zeroes in the profile matrix 
          can suppress potential motifs. A pseudocount-enhanced version is more robust.

    Example:
        >>> k = 3
        >>> t = 5
        >>> Dna = [
        ...     "GGCGTTCAGGCA",
        ...     "AAGAATCAGTCA",
        ...     "CAAGGAGTTCGC",
        ...     "CACGTCAATCAC",
        ...     "CAATAATATTCG"
        ... ]
        >>> GreedyMotifSearch(Dna, k, t)
        ['CAG', 'CAG', 'CAA', 'CAA', 'CAA']
    """
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
        
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
                BestMotifs = Motifs
            
    return BestMotifs

def CountWithPseudocounts(Motifs: list[str]) -> dict[str, list[int]]:
    """
    Computes the count matrix of motifs with pseudocounts (Laplace's Rule of Succession).

    This function is a modified version of `Count()`, where each position in the count 
    matrix is initialized with 1 instead of 0. This prevents zero values in subsequent 
    profile computations and is especially useful in motif discovery algorithms to avoid 
    assigning zero probability to unseen symbols.

    Args:
        Motifs (list[str]): A list of DNA strings (motifs) of equal length.

    Returns:
        dict[str, list[int]]: A dictionary mapping each nucleotide ('A', 'C', 'G', 'T') 
        to a list of integer counts per position, each initialized with 1 (pseudocount).

    Example:
        >>> motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
        >>> CountWithPseudocounts(motifs)
        {
            'A': [2, 3, 2, 1, 1, 3],
            'C': [3, 2, 5, 3, 1, 1],
            'G': [2, 2, 1, 3, 2, 2],
            'T': [2, 2, 1, 2, 5, 3]
        }
    """

def ProfileWithPseudocounts(Motifs: list[str]) -> dict[str, list[float]]:
    """
    Computes the nucleotide profile matrix for a list of motifs using pseudocounts.

    Unlike the basic profile computation, this version adds 1 to each nucleotide count 
    before normalization, preventing zero probabilities and improving the robustness 
    of the profile in greedy or probabilistic motif search algorithms.

    Args:
        Motifs (list[str]): A list of DNA strings (motifs) of equal length.

    Returns:
        dict[str, list[float]]: A dictionary mapping each nucleotide ('A', 'C', 'G', 'T') 
        to a list of probabilities for each position.

    Notes:
        - This function avoids zero-probability pitfalls in probabilistic models.
        - Normalization uses (t + 4) to account for the pseudocounts.

    Example:
        >>> motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
        >>> ProfileWithPseudocounts(motifs)
        {
            'A': [0.222, 0.333, 0.222, 0.111, 0.111, 0.333],
            'C': [0.333, 0.222, 0.556, 0.333, 0.111, 0.111],
            'G': [0.222, 0.222, 0.111, 0.333, 0.222, 0.222],
            'T': [0.222, 0.222, 0.111, 0.222, 0.556, 0.333]
        }
    """
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile = CountWithPseudocounts(Motifs)
    for i in profile:
        for j in range(k):
            profile[i][j]/=(t+4)
    return profile

def GreedyMotifSearchWithPseudocounts(Dna: list[str], k: int, t: int) -> list[str]:
    """
    Executes the greedy motif search algorithm using a pseudocount-corrected profile matrix.

    This enhanced version of GreedyMotifSearch prevents zero probabilities in profile matrices 
    by applying Laplace correction (pseudocounts). It initializes with the first k-mer from each 
    string, then explores all possible k-mers in the first DNA string, building a motif matrix 
    by iteratively adding the profile-most probable k-mer from the remaining strings.

    Args:
        Dna (list[str]): A list of `t` DNA strings (assumed to be of equal or similar length).
        k (int): Length of the motif to identify.
        t (int): Number of DNA strings in the input list.

    Returns:
        list[str]: A list of `t` k-mers (one from each string) representing the highest scoring motifs.

    Notes:
        - Profile construction uses `ProfileWithPseudocounts()` to avoid zero-probability values.
        - This version is more stable for motif detection than the zero-pseudocount version.
        - In case of ties in most probable k-mer selection, the first occurrence is returned.

    Example:
        >>> Dna = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"]
        >>> GreedyMotifSearchWithPseudocounts(Dna, 3, 5)
        ['TTC', 'ATC', 'TTC', 'ATC', 'TTC']
    """
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
        
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
                BestMotifs = Motifs
            
    return BestMotifs

def Motifs(Profile: dict[str, list[float]], Dna: list[str]) -> list[str]:
    """
    Identifies the profile-most probable motif (k-mer) in each DNA string from a given profile matrix.

    For each string in the input list `Dna`, this function finds the k-mer that is most 
    likely to have been generated by the given profile matrix. The result is a list of 
    motifs—one from each sequence—that best match the provided profile.

    Args:
        Profile (dict[str, list[float]]): A profile matrix represented as a dictionary 
            mapping nucleotides ('A', 'C', 'G', 'T') to lists of positional probabilities.
        Dna (list[str]): A list of `t` DNA strings (assumed to be of equal or similar length).

    Returns:
        list[str]: A list of k-mers (motifs), one from each input string, representing the 
        most probable subsequences under the profile model.

    Example:
        >>> profile = {
        ...     'A': [0.8, 0.0, 0.0, 0.2],
        ...     'C': [0.0, 0.6, 0.2, 0.0],
        ...     'G': [0.2, 0.2, 0.8, 0.0],
        ...     'T': [0.0, 0.2, 0.0, 0.8]
        ... }
        >>> Dna = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]
        >>> Motifs(profile, Dna)
        ['ACCT', 'ATGT', 'GCGT', 'ACGA', 'AGGT']
    """
    n = len(Dna[0])
    k= len(Profile["A"])
    P = Profile
    Motifs = []
    for j in range(0, len(Dna)):
        Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
    return Motifs

def RandomMotifs(Dna: list[str], k: int, t: int) -> list[str]:
    """
    Randomly selects one k-mer motif from each DNA string in the input list.

    This function is typically used as an initialization step in randomized 
    motif search algorithms such as Gibbs sampling or Randomized Motif Search.
    It selects a random starting index in each DNA string and extracts a k-mer 
    from that position.

    Args:
        Dna (list[str]): A list of `t` DNA strings (assumed to be of equal or similar length).
        k (int): Length of the motif to select.
        t (int): Number of DNA strings to process (usually len(Dna)).

    Returns:
        list[str]: A list of `t` randomly chosen k-mers (one from each DNA string).

    Example:
        >>> Dna = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]
        >>> RandomMotifs(Dna, 3, 5)
        ['ACC', 'GAT', 'TAG', 'TAA', 'AGA']
    """
    Motifs = []
    for j in range(0, t):
        r=random.randint(0, len(Dna[j])-k)
        Motifs.append(Dna[j][r:r+k])
    
    return Motifs

def RandomizedMotifSearch(Dna: list[str], k: int, t: int) -> list[str]:
    """
    Performs the Randomized Motif Search algorithm to identify conserved k-mers across DNA sequences.

    This stochastic algorithm begins with a random selection of k-mers from each string in `Dna` 
    (using `RandomMotifs()`), then iteratively refines them based on a profile matrix with pseudocounts. 
    At each step, it constructs a profile matrix from the current motifs, selects the most probable 
    k-mers in all sequences, and updates the best motifs if the score improves. The algorithm stops 
    when no improvement is made.

    This method is particularly useful for discovering weak signals (subtle motifs) in genomic sequences 
    and often outperforms deterministic approaches like greedy motif search, especially when repeated 
    many times from different random initializations.

    Args:
        Dna (list[str]): A list of `t` DNA strings.
        k (int): Length of the motifs to find.
        t (int): Number of DNA strings to process.

    Returns:
        list[str]: A list of `t` k-mers representing the best-scoring motifs found.

    Example:
        >>> Dna = [
        ...     "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
        ...     "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
        ...     "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
        ...     "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
        ...     "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
        ... ]
        >>> RandomizedMotifSearch(Dna, 8, 5)
        ['TCTCGGGG', 'CCAAGGTG', 'TACAGGCG', 'TTCAGGTG', 'TCCACGTG']

    Notes:
        - The algorithm may return different results on each run due to its randomized nature.
        - For more reliable results, run the function multiple times and retain the best output.
        - Uses pseudocounts in profile construction to avoid zero probabilities.
    """
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs
        
def Normalize(Probabilities: dict[str, float]) -> dict[str, float]:
    """
    Normalizes a dictionary of probabilities so that the values sum to 1.

    This function takes a dictionary of raw scores or unnormalized probabilities
    and scales them proportionally so that their total equals 1. This is a common 
    preprocessing step in probabilistic models, such as those used in Gibbs sampling 
    or probabilistic motif selection.

    Args:
        Probabilities (dict[str, float]): A dictionary mapping nucleotide symbols 
            ('A', 'C', 'G', 'T') to non-negative float values.

    Returns:
        dict[str, float]: A new dictionary where the values are normalized to sum to 1.

    Example:
        >>> Normalize({'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1})
        {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}
    """
    sum_of_values = sum(Probabilities.values())
    for symbol in Probabilities:
        Probabilities[symbol]=Probabilities[symbol]/sum_of_values
    return Probabilities

def WeightedDie(Probabilities: dict[str, float]) -> str:
    """
    Randomly selects a k-mer based on weighted probabilities.

    This function performs weighted random sampling from a probability distribution 
    represented as a dictionary. Each key (e.g., a k-mer or nucleotide) is associated 
    with a probability value, and the function returns one key randomly, 
    proportionally to its assigned probability.

    Args:
        Probabilities (dict[str, float]): A dictionary where keys represent k-mers or nucleotides, 
            and values are probabilities that sum to 1 (use `Normalize()` if needed).

    Returns:
        str: A randomly selected key based on the weights.

    Example:
        >>> WeightedDie({'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25})
        'A'
    """

    kmer = ''
    p = random.uniform(0,1)
    sum=0
    for kmer in Probabilities:
        sum=sum+Probabilities[kmer]
        if p < sum:
            return kmer
        
def ProfileGeneratedString(Text: str, profile: dict[str, list[float]], k: int) -> str:
    """
    Selects a k-mer from the input string according to its probability based on a given profile.

    This function computes the probability of each k-mer of length `k` in `Text` based on 
    a nucleotide position-specific profile matrix. It then normalizes these probabilities 
    and randomly selects one k-mer using a weighted die (probabilistic sampling).

    Args:
        Text (str): The DNA string from which to extract the k-mer.
        profile (dict[str, list[float]]): Profile matrix as a dictionary mapping nucleotides to lists of position-specific probabilities.
        k (int): Length of the k-mers to evaluate.

    Returns:
        str: A k-mer selected probabilistically based on the profile matrix.

    Example:
        >>> profile = {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
        >>> ProfileGeneratedString("AAACCCAAACCC", profile, 2)
        'AA'
    """
    n = len(Text)
    probabilities = {}
    
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
        
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

def GibbsSampler(Dna: list[str], k: int, t: int, N: int) -> list[str]:
    """
    Implements the Gibbs Sampling algorithm for motif discovery in a set of DNA sequences.

    Gibbs sampling is a stochastic optimization technique that iteratively updates one motif 
    at a time by probabilistically sampling from a profile built on the remaining motifs. 
    This allows the algorithm to escape local optima and potentially find better solutions 
    than greedy or deterministic methods.

    Args:
        Dna (list[str]): A list of DNA strings.
        k (int): The length of the motif to search for.
        t (int): The number of DNA strings (should be equal to len(Dna)).
        N (int): Number of iterations for the Gibbs sampling process.

    Returns:
        list[str]: A list of `t` k-mers (one from each DNA string) representing the best motif set found.

    Example:
        >>> Dna = [
        ...     "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
        ...     "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
        ...     "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
        ...     "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
        ...     "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
        ... ]
        >>> GibbsSampler(Dna, 8, 5, 100)
        ['TCTCGGGG', 'CCAAGGTG', 'TACAGGCG', 'TTCAGGTG', 'TCCACGTG']
    """
    BestMotifs = []
    Motifs = RandomMotifs(Dna, k, t)
    BestMotifs = Motifs
    for j in range(N):
        i = random.randint(1,t)
        text=Motifs.pop(i-1)
        profile=ProfileWithPseudocounts(Motifs)
        kmer=ProfileMostProbableKmer(text, k, profile)
        Motifs.insert(i-1, kmer)
        if(Score(Motifs) < Score(BestMotifs)):
            BestMotifs = Motifs
    return BestMotifs