# ShortDiff

This is a Python implementation of a diff algorithm.
It aims at producing one-way as-short-as-possible patch 
to go from a file to another.
This is useful to keep track of modifications in a text file without
keeping a copy of each state (this is the easy part of version control).
This produce shorter patch than any output from the GNU diff tool.
Since it is one-way only, the patch to go from A to B does not permit to
to go from B to A.

# Disclaimer

This algorithm have a time complexity of O(N\*M) (where N and M are the
number of line of each file) and is implemented in pure python.
There performances are not great.
You should probably not use it in any serious project.
I wrote it for educational purpose and I use it in a really small
scale project.

Still for educational project there are more naive version in the archive
directory. The final module is a refinment of these.
