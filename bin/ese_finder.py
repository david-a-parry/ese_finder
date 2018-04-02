#!/usr/bin/env python
import sys
import argparse
import re
import logging
from ese_finder import *

def parse_args():
    parser = argparse.ArgumentParser(
                    description='Output BED regions of potential ESE sites')
    parser.add_argument('-g', '--genes', required=True, 
                        help='''Input gene GTF file''')
    parser.add_argument('-f', '--fasta', required=True, 
                        help='''Genome fasta file - must match the same genome
                                version as the GTF file given to --genes.''')
    parser.add_argument('-m', '--motifs_file', metavar='MOTIFS', 
                        default='ese_finder/data/ese_int3',
                        help='''File containing one motif per line to match.
                                Default is to read the contents of 
                                'ese_finder/data/ese_int3'.''')
    return parser

def main(genes, fasta, motifs_file):
    pass

if __name__ == '__main__':
    parser = parse_args()
    args = parser.parse_args()
    main(**vars(args))
 
