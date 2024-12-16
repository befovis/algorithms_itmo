# Lab6/Task5/src/ElectionsProcessor.py

"""Module for processing election results."""

from typing import List, Tuple


class ElectionsProcessor:
    """
    A class to tally votes for candidates.
    Accepts a list of tuples (candidate, vote_count).
    Returns a list of result strings sorted by candidate names.
    """

    def process_elections(self, election_data: List[Tuple[str, str]]) -> List[str]:
        """
        Processes the election results.

        :param election_data: List of tuples (candidate_name, vote_count).
        :return: List of strings in the format "candidate vote_count\n", sorted by candidate name.
        """
        vote_tally: dict = {}
        for candidate_name, votes in election_data:
            vote_tally[candidate_name] = vote_tally.get(candidate_name, 0) + int(votes)

        sorted_candidates: List[Tuple[str, int]] = sorted(vote_tally.items())
        result_lines: List[str] = [f"{candidate} {count}\n" for candidate, count in sorted_candidates]
        return result_lines
