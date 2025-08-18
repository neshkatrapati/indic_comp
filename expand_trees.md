# `expand_trees.py`

## Description

This script generates trigrams from a bracketed constituency parse. The trigrams are of the form: `ParentLabel -> Child₁ Child₂ … Childₙ , CurrentLabel , CurrentChildrenExpansion`. The script reads a bracketed constituency parse from STDIN.

## Dependencies

- `nltk`
- `sys`

## Functions

### `child_repr(node: Tree) -> str`

Returns a leaf-stripped representation of a node suitable for the ‘children’ part of the trigram.

- **Args:**
    - `node` (Tree): The node to represent.
- **Returns:**
    - `str`: The string representation of the node.

**Example:**

- For a pre-terminal node, it returns the POS tag, e.g., `(DT)`.
- For an internal node, it returns its label plus its own children’s representations, e.g., `(NP (JJ) (NN))`.

### `expansion(node: Tree) -> str`

Returns space-separated representations of all immediate children of a node.

- **Args:**
    - `node` (Tree): The node whose children are to be represented.
- **Returns:**
    - `str`: A string of space-separated representations of the children.

### `generate_trigrams(tree: Tree)`

Yields trigram strings in the required format.

- **Args:**
    - `tree` (Tree): The input constituency parse tree.
- **Yields:**
    - `str`: A trigram string.

### `main()`

The main function of the script. It reads a parse tree from STDIN, generates the trigrams, and prints them to STDOUT.

## Usage

To use this script, pipe or redirect a bracketed constituency parse to its STDIN.

```bash
cat parse_tree.txt | python expand_trees.py
```
