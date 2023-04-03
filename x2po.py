import openpyxl
import polib

def x2po(xlsx_file, po_file):
    wb = openpyxl.load_workbook(xlsx_file)
    ws = wb.active

    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': '',
        'POT-Creation-Date': '',
        'PO-Revision-Date': '',
        'Last-Translator': 'JohnDu <johndu@usun-ap.com>',
        'Language-Team': 'U-SUN Asia',
        'Language': 'zh_TW',
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Content-Transfer-Encoding': '8bit',
        'X-Source-Language': 'en',
        'X-Generator': 'Poedit 3.2.2',
        'X-Poedit-SourceCharset': 'UTF-8',
    }

    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[2] is not None:
            entry = polib.POEntry(
                msgid=row[2],
                msgstr=row[3] if row[3] is not None else '',
                msgctxt=row[1],
                occurrences=[(row[0], '')] if row[0] else []
            )
            po.append(entry)

    # def format_multiline_entry(text):
    #     lines = text.split('\n')
    #     if len(lines) > 1:
    #         return '""\n' + '\n'.join('"{}\\n"'.format(line.rstrip().replace('"', '\\"').replace('\t', '\\t')) for line in lines[:-1]) + '\n"{}"'.format(lines[-1].rstrip().replace('"', '\\"').replace('\t', '\\t'))
    #     else:
    #         return '"{}"'.format(text.rstrip('\n').replace('"', '\\"').replace('\t', '\\t'))

    def format_multiline_entry(text):
        lines = text.split('\n')
        if len(lines) > 1:
            return '""\n' + '\n'.join('"{}\\n"'.format(line.replace('\\', '\\\\').replace('"', '\\"').replace('\t', '\\t')) for line in lines[:-1]) + '\n"{}"'.format(lines[-1].replace('\\', '\\\\').replace('"', '\\"').replace('\t', '\\t'))
        else:
            return '"{}"'.format(text.replace('\\', '\\\\').replace('"', '\\"').replace('\t', '\\t'))



    with open(po_file, 'w', encoding='utf-8') as f:
        # Write metadata
        f.write('msgid ""\n')
        f.write('msgstr ""\n')
        for key, value in po.metadata.items():
            f.write(f'"{key}: {value}\\n"\n')
        f.write('\n')

        # Write entries
        for entry in po:
            if entry.occurrences:
                f.write('#: {}\n'.format(entry.occurrences[0][0]))

            if entry.msgctxt:
                f.write('msgctxt {0}\n'.format(format_multiline_entry(entry.msgctxt)))
            f.write('msgid {0}\n'.format(format_multiline_entry(entry.msgid)))
            f.write('msgstr {0}\n'.format(format_multiline_entry(entry.msgstr)))
            f.write('\n')
