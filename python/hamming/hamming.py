def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strangs must have the same length")
    diffs = [strand_a[i] == strand_b[i] for i in range(len(strand_a))]

    return diffs.count(False)
