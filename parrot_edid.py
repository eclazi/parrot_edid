from argparse import ArgumentParser
import xml.etree.ElementTree as ET
import binascii

def main():
    parser = ArgumentParser(description='Create a binary EDID from a .edid file created by Parrot Trainer')
    parser.add_argument('input_path',
                        type=str,
                        help='Path to .edid file')
    parser.add_argument('output_path',
                        type=str,
                        help='Path to binary EDID')
    args = parser.parse_args()

    tree = ET.parse(open(args.input_path, 'r'))

    data_block = tree.find('Edid/DataBlock')
    extension_block = tree.find('Edid/ExtensionBlock')

    out = open(args.output_path, 'w')
    for block in [data_block, extension_block]:
        for i in range(0 , len(block.text), 2):
            byte = binascii.a2b_hex(block.text[i:i+2])
            out.write(byte)

if __name__ == '__main__':
    main()