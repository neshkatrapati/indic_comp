# `parse_wmt.py`

## Description

This script reads one-sentence-per-line text from an input file, parses each sentence using the specified parser (currently Benepar), and writes the corresponding Penn-style constituency trees to an output file.

## Dependencies

- `argparse`
- `sys`
- `pathlib`
- `spacy`
- `benepar`

## Functions

### `load_benepar()`

Loads the SpaCy pipeline with the Benepar component.

- **Returns:**
    - A SpaCy pipeline that can be used to parse sentences.

### `parse_file(in_path: Path, out_path: Path, nlp)`

Reads sentences from the input file, parses them using the provided NLP pipeline, and writes the parse trees to the output file.

- **Args:**
    - `in_path` (Path): The path to the input file.
    - `out_path` (Path): The path to the output file.
    - `nlp`: The NLP pipeline to use for parsing.

### `main()`

The main function of the script. It parses command-line arguments, loads the specified parser, and calls `parse_file` to perform the parsing.

## Command-line Arguments

- `--input` or `-i`: (Required) The path to the plain-text input file, with one sentence per line.
- `--output` or `-o`: (Required) The path to the destination file for the bracketed parses.
- `--parser` or `-p`: (Optional) The parsing backend to use. Currently, only "benepar" is supported. Defaults to "benepar".

## Usage

```bash
python parse_wmt.py \
    --input ./wmt14-ende-raw/train.en \
    --output ./wmt14-ende-parsed/train.en.parse \
    --parser benepar
```

```