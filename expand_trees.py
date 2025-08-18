#!/usr/bin/env python
"""
Generate trigrams of the form:
ParentLabel -> Child₁ Child₂ … Childₙ , CurrentLabel , CurrentChildrenExpansion
from a bracketed constituency parse read from STDIN.
"""

from nltk import Tree
import sys


def child_repr(node: Tree) -> str:
    """
    Return a leaf-stripped representation of a node suitable for
    the ‘children’ part of the trigram, e.g.  (DT)  or  (NP (JJ) (NN)).
    """
    # Pre-terminal: POS tag with a single word child
    if len(node) == 1 and isinstance(node[0], str):
        if isinstance(node, str):
            return ""
        return f"({node.label()})"
    # Internal node: show its label plus its own children’s representations
    inner = " ".join(child_repr(c) for c in node)
    if isinstance(node, str):
        return ""
    return f"({node.label()} {inner})"


def expansion(node: Tree) -> str:
    """Return space-separated representations of *all* immediate children."""
    return " ".join(child_repr(c) for c in node)


def generate_trigrams(tree: Tree):
    """Yield trigram strings in the required format."""
    for parent in tree.subtrees():
        # List of this parent’s immediate children labels
        child_labels = " ".join(c.label() for c in parent if isinstance(c, Tree))
        for child in parent:
            if isinstance(child, Tree):  # ignore pre-terminals when they are 'Current'
                exp = expansion(child)
                if exp:
                    yield f"{parent.label()} -> {child_labels}, {child.label()}, {exp}"


def main():
    parse_str = "(S (NP (NP (DT the) (NN boy)) (PP (IN in) (NP (JJ red) (NN shirt)))) (VP (VBZ is) (VP (VBG playing) (PP (IN with) (NP (PRP$ his) (NN ball))) (PP (IN in) (NP (DT the) (NN garden))))))"
    if not parse_str:
        sys.exit("Please pipe or redirect a parse tree to STDIN.")
    tree = Tree.fromstring(parse_str)
    for line in generate_trigrams(tree):
        print(line)


if __name__ == "__main__":
    main()
