import matplotlib.pyplot as plt

def plot_symbol_array(symbol_array: dict, symbol: str, genome_label: str = "genome") -> None:
    """
    Plots the symbol frequency array across the genome.

    This function visualizes the number of occurrences of a specified nucleotide 
    in a sliding window (typically of size genome_length/2), showing variation 
    in composition across the genome.

    Args:
        symbol_array (dict[int, int]): Dictionary mapping genome positions to the count of a symbol in the sliding window.
        symbol (str): The nucleotide symbol ('A', 'C', 'G', or 'T') used for counting.
        genome_label (str, optional): Label for the genome, used in the figure title. Default is "genome".

    Returns:
        None: The function displays the plot using matplotlib.

    Example:
        >>> arr = FasterSymbolArray(genome, 'C')
        >>> plot_symbol_array(arr, 'C', genome_label="E. coli")
    """
    positions = list(symbol_array.keys())
    counts = list(symbol_array.values())

    plt.figure(figsize=(10, 5))
    plt.plot(positions, counts, color="blue")
    plt.xlabel("genome position")
    plt.ylabel(f"count of {symbol} in half-genome starting at given position")
    plt.title(f"Symbol array for {genome_label} (symbol = '{symbol}')")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

