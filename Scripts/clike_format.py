import argparse

if __name__ in '__main__':
    try:
        parser = argparse.ArgumentParser( description = 'Prints C-like string from raw binary' );
        parser.add_argument( '-f', required = True, help = 'Path to the raw binary', type = str );
        option = parser.parse_args();

        hex_data = open(option.f, 'rb').read().hex()

        paired_hex_data = [i+k for i,k in zip(hex_data[0::2],hex_data[1::2])]

        print("C-like string: ")
        print("{ 0x", end='')
        print(*paired_hex_data, sep=', 0x', end=' };')

    except Exception as e:
        print( '[!] error: {}'.format( e ) );
