def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    numerator = len([x for x in relevant if x in recommended[:k]])
    precision = numerator/k
    recall = numerator/len(relevant)

    return [precision, recall]
    