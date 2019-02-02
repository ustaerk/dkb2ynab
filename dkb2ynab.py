#!/usr/bin/env python3
import argparse
import csv
import itertools
import sys

# config per statement type
config = {
    'account': {
        # number of rows to skip from the source csv
        'skip_rows': 7,
        # header columns we will have in the output
        'header': ['Date', 'Payee', 'Memo', 'Inflow'],
        # indices of source columns to keep
        'keep': [0, 3, 4, 7],
        # index of the inflow column
        'inflow_column': 3
    },
    'credit_card': {
        'skip_rows': 7,
        'header': ['Date', 'Memo', 'Inflow'],
        'keep': [2, 3, 4],
        'inflow_column': 2
    }
}

parser = argparse.ArgumentParser(description='Convert DKB account statements into a format usable by YNAB 4. Reads the'
                                             'specified file and prints to stdout')

group = parser.add_mutually_exclusive_group()
group.add_argument('-a', action='store_const', dest='statement_type', const='account',
                   help='parse an account statement file (default)', default='account')
group.add_argument('-c', action='store_const', dest='statement_type', const='credit_card',
                   help='parse a credit card statement file')

parser.add_argument('file', type=argparse.FileType(mode='r', encoding='cp1252'),
                    help='name of the statement file to convert')

args = parser.parse_args()

statement_reader = csv.reader(itertools.islice(args.file, config[args.statement_type]['skip_rows'], None),
                              delimiter=';', quotechar='"')

ynab_writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
ynab_writer.writerow(config[args.statement_type]['header'])

for row in statement_reader:
    extracted = list(row[i] for i in config[args.statement_type]['keep'])

    # in the inflow column, convert to us-english number formatting
    inflow_column = config[args.statement_type]['inflow_column']
    extracted[inflow_column] = extracted[inflow_column].replace('.', '')
    extracted[inflow_column] = extracted[inflow_column].replace(',', '.')

    ynab_writer.writerow(extracted)
