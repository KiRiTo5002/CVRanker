from src.schemas import Resume, MatchResult


def rank_candidates(
    candidates: list[tuple[Resume, MatchResult]],
) -> list[tuple[Resume, MatchResult]]:
    """
    Rank candidates from highest to lowest overall score.
    """

    return sorted(
        candidates,
        key=lambda candidate: candidate[1].overall_score,
        reverse=True,
    )
