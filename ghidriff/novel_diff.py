import hashlib

from typing import List, Tuple, TYPE_CHECKING

from .ghidra_diff_engine import GhidraDiffEngine

if TYPE_CHECKING:
    import ghidra
    from ghidra_builtins import *


class SimpleDiff(GhidraDiffEngine):
    """
    An Ghidra Diff implementation using simple comparison mechanisms
    """

    def find_matches(
        self,
        p1: "ghidra.program.model.listing.Program",
        p2: "ghidra.program.model.listing.Program",
        ignore_FUN: bool = False,
    ) -> dict:
        """
        Find matching and unmatched functions between p1 and p2
        """
        from ghidra.program.util import DiffUtility

        matched = []
        unmatched = []
        matches = []

        self.logger.info("\nMatching functions...")

        return [unmatched, matches, []]
