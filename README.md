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

# Installation

Use pip to install it or copy this directory in a relevant place
if you know what you are doing.

`pip install ShortDiff`

# Usage

## CLI

Create a patch

```
python -m ShortDiff diff FILA_A [FILE_B]
```

Create the patch to go from A to B. If FILE_B is ommited, its content
is expected from the standard input.
Output the patch to standard output.

Apply a patch

```
python -m ShortDiff patch PATCH [FILE]
```
Apply PATCH to FILE. If FILE is ommited, apply patch to standard input.
Result is printed to standard output.

## API

Functions can be imported from the module to be used in other apps.
Useful functions include:

- `differ(old, new)`: (low level) take to arbitrary sequences and return the Levenstein distance and
  the path from one to another as a sequence of pairs (position in old, position in new).
  If the position in old is the same in two consecutive pair, it correspond to an insertion.
  If the position in new is the same in two consecutive pair, it correspond to a deletion.
  Else it correspond to an unmodified chunk.
  Path is made so to consecutive operations cannot be of the same kind (a deletion cannot be
  immediatly followed by another deletion).

- `get_chunks(old_txt, new_txt)`: (high level) generator taking two strings and compute the live diff.
  It yields 4 elements tuples `(kind, start, stop, content)`. `kind` is one of `'d'` (deletion) `'i'` (insertion)
  and `'k'` (keep/unmodified). `start` and `stop` are the line number boundaries of the chunk concerned by the 
  operations in `old_txt` for deletion and keep and in `new_txt` for insertion. `content` is the list of lines of
  the chunk.

- `create_patch(old_txt, new_txt)`: (high level) return the patch as printed by the CLI
- `apply_patch(old_txt, patch)`: (high level) return the result of applying `patch` to `old_txt`
  
  
