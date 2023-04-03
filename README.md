# jdxonv.py
The converter between .PO (Portable Object) and .XLSX/XLS (Microsoft Excel)

```
This script converts files between .PO and .XLSX formats using po2x and x2po functions.

Command-line arguments:
- input: the input file (.PO or .XLSX)
- output (optional): the output file (.PO or .XLSX). If not provided, the output filename will be generated using get_output_filename.

Supported input file formats: .PO and .XLSX.

Example usage:
    - To convert a .PO file to .XLSX: python jdxonv.py input.po
    - To convert a .XLSX file to .PO: python jdxonv.py input.xlsx
    - To specify the output file path: python jdxonv.py input.po -o output.xlsx

Note: If the output file path is not specified, the script generates a filename using the 'jd' prefix and a two-digit index.

```
