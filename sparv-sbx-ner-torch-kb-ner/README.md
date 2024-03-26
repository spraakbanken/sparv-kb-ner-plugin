# sparv-sbx-ner-torch-kb-ner

[![PyPI version](https://badge.fury.io/py/sparv-sbx-ner-torch-kb-ner.svg)](https://pypi.org/project/sparv-sbx-ner-torch-kb-ner)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sparv-sbx-ner-torch-kb-ner)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/json-arrays)](https://pypi.org/project/sparv-sbx-ner-torch-kb-ner/)

[![Maturity badge - level 2](https://img.shields.io/badge/Maturity-Level%202%20--%20First%20Release-yellowgreen.svg)](https://github.com/spraakbanken/getting-started/blob/main/scorecard.md)
[![Stage](https://img.shields.io/pypi/status/sparv-sbx-ner-torch-kb-ner)](https://pypi.org/project/sparv-sbx-ner-torch-kb-ner/)

[![CI(release)](https://github.com/spraakbanken/sparv-sbx-ner/actions/workflows/release-torch-kb-ner.yml/badge.svg)](https://github.com/spraakbanken/sparv-sbx-ner/actions/workflows/release-torch-kb-ner.yml)

Plugin for applying bert masking as a [Sparv](https://github.com/spraakbanken/sparv-pipeline) annotation.

## Install

First, install Sparv, as suggested:

```bash
pipx install sparv-pipeline
```

Then install install `sparv-sbx-ner-torch-kb-ner` with

```bash
pipx inject sparv-pipeline sparv-sbx-ner-torch-kb-ner
```

## Usage

Depending on how many explicit exports of annotations you have you can decide to use this
annotation exclusively by adding it as the only annotation to export under `xml_export`:

```yaml
xml_export:
    annotations:
        - <token>:sbx_word_prediction_kb_bert.ner--torch-kb-ner
```

To use it together with other annotations you might add it under `export`:

```yaml
export:
    annotations:
        - <token>:sbx_word_prediction_kb_bert.ner--torch-kb-ner
        ...
```

### Configuration

You can configure this plugin by the number of neighbours to generate.

#### Number of Neighbours

The number of neighbours defaults to `5` but can be configured in `config.yaml`:

```yaml
sbx_word_prediction_kb_bert:
    num_neighbours: 5
```

#### Number of Decimals

The number of decimals defaults to `3` but can be configured in `config.yaml`:

```yaml
sbx_word_prediction_kb_bert:
    num_decimals: 3
```

> [!NOTE] This also controls the cut-off, so all values where the score round to 0.000 (or the number of decimals) is discarded.

### Metadata

#### Model

Type | HuggingFace Model | Revision
--- | --- | ---
Model | [`KBLab/bert-base-swedish-cased`](https://huggingface.co/KBLab/bert-base-swedish-cased) | c710fb8dff81abb11d704cd46a8a1e010b2b022c
Tokenizer | same as Model  | same as Model

## Changelog

This project keeps a [changelog](./CHANGELOG.md).
