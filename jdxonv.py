import argparse
import os
import sys
from pathlib import Path
from po2x import po2x
from x2po import x2po

# Define a function to generate an output file name based on the input file name and path
def get_output_filename(input_path, ext):
    """
    # This function takes an input path and an extension as arguments
    # It extracts the input filename stem, output directory and prefix
    # Then it checks if the input filename stem starts with 'jd' and has a 2-digit number after it
    # If yes, it extracts the index from the filename stem and removes it from the stem
    # Then it generates a new output filename with prefix, index, input stem and extension
    # If the generated output filename already exists, it increments the index and tries again
    # It keeps incrementing the index until it finds a non-existing output filename
    # Finally, it returns the output path
    # :param input_path: The path of the input file
    # :param ext: The extension of the output file
    # :return: A Path object representing the output file path
    """
    input_stem = input_path.stem
    output_dir = input_path.parent
    prefix = "jd"
    index = 0

    # If the input file name starts with "jd" followed by two digits, use the digits as an index
    if input_stem.startswith("jd") and input_stem[2:4].isdigit():
        index = int(input_stem[2:4])
        input_stem = input_stem[5:]

    # Generate an output file name that does not conflict with any existing file in the output directory
    while True:
        output_filename = f"{prefix}{index:02}_{input_stem}.{ext}"
        output_path = output_dir / output_filename
        if not output_path.exists():
            break
        index += 1

    return output_path

# Define the main function
def main():
    """
    # Parse command-line arguments, convert the input file to the output format, and save the output file
    # If output file is not provided, it calls get_output_filename function to generate a new output filename
    # It then checks the input file extension and calls the corresponding conversion function
    # If the input file extension is neither .PO nor .XLSX, it raises a ValueError
    """
    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description="Convert .PO to .XLSX or .XLSX to .PO")

    # Define two positional arguments: the input file and an optional output file
    parser.add_argument("input", help="Input file (.PO or .XLSX)")
    parser.add_argument("-o", "--output", help="Output file (.PO or .XLSX)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Convert the input path string to a Path object
    input_path = Path(args.input)

    # Check the extension of the input file and convert it to the corresponding output format
    if input_path.suffix.lower() == ".po":
        # If the output file is specified, use it as the output file path; otherwise, generate an output file name
        if args.output:
            output_path = Path(args.output)
        else:
            output_path = get_output_filename(input_path, "xlsx")
        
        # Convert the input file to the output format and display a message when the conversion is completed
        print(f"Converting {input_path.name} to {output_path.name}")
        po2x(input_path, output_path)
        print(f"Conversion completed. Output saved as {output_path.name}")

    elif input_path.suffix.lower() == ".xlsx":
        # If the output file is specified, use it as the output file path; otherwise, generate an output file name
        if args.output:
            output_path = Path(args.output)
        else:
            output_path = get_output_filename(input_path, "po")
        
        # Convert the input file to the output format and display a message when the conversion is completed
        print(f"Converting {input_path.name} to {output_path.name}")
        x2po(input_path, output_path)
        print(f"Conversion completed. Output saved as {output_path.name}")

    else:
        # Raise an error
        raise ValueError("Unsupported input file format. Please provide a .PO or .XLSX file.")

if __name__ == "__main__":
    main()
