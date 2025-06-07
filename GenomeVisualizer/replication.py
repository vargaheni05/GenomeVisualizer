def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

def Reverse(Pattern):
    rev = ""
    for char in Pattern:
        rev = char + rev
    return rev

def Complement(Pattern):
    comp = ""
    for char in Pattern:
        if(char == 'T'):
            comp = comp + 'A'
        if(char == 'A'):
            comp = comp + 'T'
        if(char == 'C'):
            comp = comp + 'G'
        if(char == 'G'):
            comp = comp + 'C'
    return comp

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

def SkewArray(Genome):
    skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == "C":
            skew.append(skew[-1] - 1)
        elif Genome[i] == "G":
            skew.append(skew[-1] + 1)
        else:
            skew.append(skew[-1])
    return skew

def MinimumSkew(Genome):
    positions = []
    skew = SkewArray(Genome)
    mn = min(skew)
    for i in range (len(skew)):
        if skew[i] == mn:
            positions.append(i)
    return positions

def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if(p[i] != q[i]):
            count+=1
    return count

def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    for i in range(len(Text)-len(Pattern)+1):
        distance = HammingDistance(Text[i:i+len(Pattern)], Pattern)
        if distance <= d:
            positions.append(i)
    return positions

def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        distance = HammingDistance(Text[i:i+len(Pattern)], Pattern)
        if distance <= d:
            count = count+1
    return count

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] += 1
    return freq

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        # add each key to words whose corresponding frequency value is equal to m
        if(freq.get(key) == m):
            words.append(key)
    return words