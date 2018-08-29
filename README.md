# ShortDiff

This is a Python implementation of a diff algorithm. It's purpose is to
produce one way and as short as possible patch to go from a file to another.
This is useful for keeping history of modifications of a text file without
keeping a copy of each state (this is the easy part of version control).
This produce shorter patch than any output from the GNU diff tool.
By the way it is one way witch means the patch to go from A to B is not
usable to go from B to A.

# Disclaimer

Since it is a pure python script and it is a O(N\*M) (where N and M are the
number of line of each file) in time complexity it is not very performant.
You should not use it in any serious project. As for me I wrote it for
educational purpose and I use it in a really small scale project.

Still for educational project there are more naive version in the archive
directory. The final module is a refinment of these.
