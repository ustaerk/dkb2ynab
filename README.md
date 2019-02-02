# dkb2ynab
A little python script to convert DKB account statements into a YNAB 4 compatible format

# Usage

```
usage: dkb2ynab.py [-h] [-a | -c] file

Convert DKB account statements into a format usable by YNAB 4. Reads
the specified file and prints to stdout

positional arguments:
  file        name of the statement file to convert

optional arguments:
  -h, --help  show this help message and exit
  -a          parse an account statement file (default)
  -c          parse a credit card statement file
```

## Examples
### Convert regular checking account statement
```bash
./dkb2ynab.py -a statement.csv > ynab.csv
```

The `-a` flag can also be omitted:

```bash
./dkb2ynab.py statement.csv > ynab.csv
```

### Convert credit card statement
```bash
./dkb2ynab.py -c statement.csv > ynab.csv
```