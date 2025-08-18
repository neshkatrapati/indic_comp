#!/usr/bin/env python3
"""
parse_wmt.py
------------
Read one-sentence-per-line text, parse each sentence with Benepar,
and write the corresponding Penn-style constituency trees.

Example
-------
python parse_wmt.py \
       --input  ./wmt14-ende-raw/train.en \
       --output ./wmt14-ende-parsed/train.en.parse \
       --parser benepar
"""

import argparse, sys
from pathlib import Path

# ---- choose a parser implementation ----------------------------------------
# Here we use SpaCy + Benepar.  Feel free to swap in CoreNLP, Berkeley, etc.
import spacy, benepar

def load_benepar():
    """Return a SpaCy pipeline that yields `token._.parse_string`."""
    nlp = spacy.load("en_core_web_sm", disable=["ner", "lemmatizer"])
    # if not benepar.is_downloaded("benepar_en3"):
    #     benepar.download("benepar_en3")
    nlp.add_pipe("benepar", config={"model": "benepar_en3"})
    return nlp

def parse_file(in_path: Path, out_path: Path, nlp):
    with in_path.open(encoding="utf8") as fin, out_path.open("w", encoding="utf8") as fout:
        for line_no, sent in enumerate(fin, 1):
            sent = sent.strip()
            if not sent:
                fout.write("\n")
                continue
            doc = nlp(sent)
            # Benepar attaches the parse to the *first* sentence in the Doc
            tree = doc.sents.__iter__().__next__()._.parse_string
            fout.write(tree + "\n")
            if line_no % 10000 == 0:
                print(f"{line_no:,} sentences parsed", file=sys.stderr)

# ---- CLI -------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", "-i",  required=True, type=Path,
                    help="plain-text file, one sentence per line")
    ap.add_argument("--output", "-o", required=True, type=Path,
                    help="destination file for bracketed parses")
    ap.add_argument("--parser", "-p", default="benepar",
                    choices=["benepar"],  # extendable
                    help="which backend to use")
    args = ap.parse_args()

    if args.parser == "benepar":
        nlp = load_benepar()
    else:
        raise NotImplementedError(f"Parser {args.parser} not supported yet.")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    parse_file(args.input, args.output, nlp)

if __name__ == "__main__":
    main()
