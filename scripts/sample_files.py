#!/usr/bin/env python3


import argparse
import os
import random
import shutil
import sys


def walk(dirname):
    """Returns all the files in a directory tree."""
    for (root, _, files) in os.walk(dirname):
        for file in files:
            yield os.path.join(root, file)


def sample(n, input_dir, output_dir):
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    os.makedirs(output_dir)
    for file in random.sample(list(walk(input_dir)), n):
        dest = os.path.join(output_dir, os.path.basename(file))
        if os.path.exists(dest):
            sys.stderr.write('WARNING: {} exists. Clobbering.'.format(dest))
        shutil.copyfile(file, dest)


def parse_args(args):
    p = argparse.ArgumentParser()

    p.add_argument(
        '-n', '--n', dest='n', action='store', type=int, metavar='N',
        default=1000,
        help='The size of the sample (default=1000).',
        )
    p.add_argument(
        '-i', '--input', dest='input', action='store', type=str,
        metavar='INPUT_DIR', help='The input directory to sample.',
        )
    p.add_argument(
        '-o', '--output', dest='output', action='store', type=str,
        metavar='OUTPUT_DIR',
        help='The output directory to copy sample files into.',
        )

    opts = p.parse_args(args)

    if opts.input is None or opts.output is None:
        p.error('You must give the input and output directories.')

    return opts


def main():
    opts = parse_args(sys.argv[1:])
    sample(opts.n, opts.input, opts.output)


if __name__ == '__main__':
    main()
