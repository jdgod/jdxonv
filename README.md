# jdxonv
The converter between .PO (Portable Object) and .XLSX/XLS (Microsoft Excel)

```
This script converts files between .PO and .XLSX formats using po2x and x2po functions.

Functions:
    - get_output_filename: Generates an output filename with the prefix 'jd' and a two-digit index.
    - main: Converts the input file to the specified output format.

Arguments:
    - input: Path to the input file (.PO or .XLSX).
    - output: Path to the output file (.PO or .XLSX).

Example usage:
    - To convert a .PO file to .XLSX: python jdxonv.py input.po
    - To convert a .XLSX file to .PO: python jdxonv.py input.xlsx
    - To specify the output file path: python jdxonv.py input.po -o output.xlsx

Note: If the output file path is not specified, the script generates a filename using the 'jd' prefix and a two-digit index.

```
