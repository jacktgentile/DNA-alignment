# DNA-alignment

This program randomly generates a base-pair sequence of given length, creates mutations of that sequence, then uses dynamic programming to find the optimal alignment using given values for matches, mismatches, and gap penalty. 

Implemented in Python 3.7.2.

The files containing the genetic information must be in FASTA format.

The following command generates a random base-pair sequence of length `L`, produces 2 sequences with `L`/10 mutations each, then calculates optimal alignment between the 2 sequences.
```
python create_data_and_align.py <L>
```
