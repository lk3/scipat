# scipat

## About

This module generates a dataset from USPTO patent records. Its data retrieval component is based on the [pypatent](https://github.com/daneads/pypatent) module by @daneads and @danhydro.

Work in progress.


## Development environment

```
conda env create -f ~/scipat/scipat.yml
conda activate scipat
pip install -U pytest
```

## Development install

```
pip install -e .
```

## Test

```
pytest -s tests
```

## To do

* patent references count (US and foreign)
* NLP references count