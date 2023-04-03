import argparse
import os
import sys
from pathlib import Path
from po2x import po2x
from x2po import x2po

def get_output_filename(input_path, ext):
    input_stem = input_path.stem
    output_dir = input_path.parent
    prefix = "jd"
    index = 0

    if input_stem.startswith("jd") and input_stem[2:4].isdigit():
        index = int(input_stem[2:4])
        input_stem = input_stem[5:]

    while True:
        output_filename = f"{prefix}{index:02}_{input_stem}.{ext}"
        output_path = output_dir / output_filename
        if not output_path.exists():
            break
        index += 1

    return output_path

def main():
    parser = argparse.ArgumentParser(description="Convert .PO to .XLSX or .XLSX to .PO")
    parser.add_argument("input", help="Input file (.PO or .XLSX)")
    parser.add_argument("-o", "--output", help="Output file (.PO or .XLSX)")

    args = parser.parse_args()

    input_path = Path(args.input)

    if input_path.suffix.lower() == ".po":
        if args.output:
            output_path = Path(args.output)
        else:
            output_path = get_output_filename(input_path, "xlsx")
        
        print(f"Converting {input_path.name} to {output_path.name}")
        po2x(input_path, output_path)
        print(f"Conversion completed. Output saved as {output_path.name}")

    elif input_path.suffix.lower() == ".xlsx":
        if args.output:
            output_path = Path(args.output)
        else:
            output_path = get_output_filename(input_path, "po")
        
        print(f"Converting {input_path.name} to {output_path.name}")
        x2po(input_path, output_path)
        print(f"Conversion completed. Output saved as {output_path.name}")

    else:
        raise ValueError("Unsupported input file format. Please provide a .PO or .XLSX file.")

if __name__ == "__main__":
    main()