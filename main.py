from collections import Counter
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, dna_sequence: str) -> List[str]:
        # Initialize a counter to keep track of the DNA sequence occurrences
        sequence_count = Counter()
        # Initialize an empty list to store the repeated sequences
        repeated_sequences = []
        # Calculate the number of possible substrings of length 10
        num_substrings = len(dna_sequence) - 10
        # Iterate over all the substrings of length 10 in the DNA sequence
        for i in range(num_substrings + 1):
            # Extract a substring of length 10
            subsequence = dna_sequence[i: i + 10]
            # Increment the count for this particular substring
            sequence_count[subsequence] += 1
            # If the count reaches 2, it means we've found a repeated sequence
            if sequence_count[subsequence] == 2:
                # Add it to the list of repeated sequences
                repeated_sequences.append(subsequence)
        # Return the list of repeated sequences
        return repeated_sequences
