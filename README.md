# DNA-alignment

This program randomly generates a base-pair sequence of given length, creates mutations of that sequence, then uses dynamic programming to find the optimal alignment using given values for matches, mismatches, and gap penalty. 

Implemented in Python 3.7.2.

Files containing the genetic information must be in FASTA format.

The following command generates a random base-pair sequence of length `L`, produces 2 sequences with `L`/10 mutations each, then calculates optimal alignment between the 2 sequences.
```
python create_data_and_align.py <L>
```
The substitution matrix is a 4x4 integer matrix that assigns a score value for when one base is substituted for another.

The following command calculates the optimal alignment--and corresponding score--between sequences stored in `seq1` and `seq2` using the substitution matrix stored in a text file `subs`, with an integer gap penalty of `G`. 
```
python optimal_align.py <seq1> <seq2> <subs> <G>
```
The results are stored in `results.txt`.
