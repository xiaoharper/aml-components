import argparse
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A sample component which shows the input data.")
    parser.add_argument('--input_data')
    parser.add_argument('--output_data')
    parser.add_argument('--str_param', type=str)
    parser.add_argument('--int_param', type=int, default=0)
    parser.add_argument('--enum_param', choices=['val1', 'val2'])

    args, _ = parser.parse_known_args()
    print("Input data:", args.input_data)
    print("Output data:", args.output_data)
    print("Str param:", args.str_param)
    print("Int param:", args.int_param)
    print("Enum param:", args.enum_param)
    with open(Path(args.output_data) / 'result.txt', 'w') as fout:
        fout.write(str(args))
