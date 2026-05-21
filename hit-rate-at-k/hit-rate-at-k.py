def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    counter = 0
    for rec, gt in zip(recommendations, ground_truth):
        hit = len([x for x in gt if x in rec[:k]])
        if hit: counter += 1

    return counter/len(recommendations)