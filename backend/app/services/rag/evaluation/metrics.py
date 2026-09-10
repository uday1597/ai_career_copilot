def calculate_precision(
    retrieved_sources: list[str],
    expected_sources: list[str],
) -> float:

    if not retrieved_sources:
        return 0.0

    retrieved = set(retrieved_sources)
    expected = set(expected_sources)

    relevant_retrieved = (
        retrieved.intersection(expected)
    )

    return (
        len(relevant_retrieved)
        / len(retrieved)
    )


def calculate_recall(
    retrieved_sources: list[str],
    expected_sources: list[str],
) -> float:

    if not expected_sources:
        return 0.0

    retrieved = set(retrieved_sources)
    expected = set(expected_sources)

    relevant_retrieved = (
        retrieved.intersection(expected)
    )

    return (
        len(relevant_retrieved)
        / len(expected)
    )

def calculate_f1(
    precision: float,
    recall: float,
) -> float:

    if precision + recall == 0:
        return 0.0

    return (
        2
        * precision
        * recall
        / (precision + recall)
    )