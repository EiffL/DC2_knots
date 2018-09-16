import os
import numpy as np
import argparse
import contextlib
import gzip

@contextlib.contextmanager
def fopen(filename, **kwds):
    """
    Return a file descriptor-like object that closes the underlying
    file descriptor when used with the with-statement.
    Parameters
    ----------
    filename: str
        Filename of the instance catalog.
    **kwds: dict
        Keyword arguments to pass to the gzip.open or open functions.
    Returns
    -------
    generator: file descriptor-like generator object that can be iterated
        over to return the lines in a file.
    """
    abspath = os.path.split(os.path.abspath(filename))[0]
    try:
        if filename.endswith('.gz'):
            fd = gzip.open(filename, **kwds)
        else:
            fd = open(filename, **kwds)
        yield fopen_generator(fd, abspath, **kwds)
    finally:
        fd.close()

def fopen_generator(fd, abspath, **kwds):
    """
    Return a generator for the provided file descriptor that knows how
    to recursively read in instance catalogs specified by the
    includeobj directive.
    """
    with fd as input_:
        for line in input_:
            if not line.startswith('includeobj'):
                yield line
            else:
                filename = os.path.join(abspath, line.strip().split()[-1])
                with fopen(filename, **kwds) as my_input:
                    for line in my_input:
                        yield line

def main(in_instcat_disk, in_instcat_knots,
             out_instcat_disk, out_instcat_knots):
    # Use .fopen to read in the command and object lines from the
    # instance catalog.
    with fopen(in_instcat_disk, mode='rt') as input_disk:
        with fopen(in_instcat_knots, mode='rt') as input_knots:
            with open(out_instcat_disk, 'w') as output_disk:
                with open(out_instcat_knots, 'w') as output_knots:
                    for line_disk, line_knots in zip(input_disk,input_knots):
                        if not line_disk.startswith('#'):
                            tokens_disk = line_disk.strip().split()
                            tokens_knots = line_knots.strip().split()

                            # Check the object ids are the same
                            id_disk = int(tokens_disk[1]) >> 10
                            id_knots = int(tokens_knots[1]) >> 10

                            if id_disk != id_knots:
                                print("ERROR: object ids do not match between input catalogs")
                                exit(-1)

                            # Get total flux
                            magnorm_disk = np.float(tokens_disk[4])
                            magnorm_knots = np.float(tokens_knots[4])
                            total_flux = 10.**(-magnorm_disk/2.5) + 10.**(-magnorm_knots/2.5)
                            knots_flux_ratio = 10.**(-magnorm_knots/2.5) / total_flux

                            # Apply flux cap for large galaxies
                            size = np.float(tokens_disk[13])

                            magnorm_disk = -2.5*np.log10((1-knots_flux_ratio)*total_flux)
                            magnorm_knots = -2.5*np.log10(knots_flux_ratio*total_flux)

                            # Update the entry
                            tokens_disk[4] = str(magnorm_disk)
                            tokens_knots[4] = str(magnorm_knots)
                            line_disk = ' '.join(tokens_disk)
                            line_knots = ' '.join(tokens_knots)

                        # Write
                        output_disk.write(line_disk)
                        output_knots.write(line_knots)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Knots cancelling script')
    parser.add_argument('input_disk', type=str)
    parser.add_argument('input_knots', type=str)
    parser.add_argument('output_disk', type=str)
    parser.add_argument('output_knots', type=str)
    args = parser.parse_args()
    main(args.input_disk, args.input_knots, args.output_disk, args.output_knots)
