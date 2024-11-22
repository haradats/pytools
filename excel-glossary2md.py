import pandas as pd
import openpyxl
import os

site_name = 'my site'

input_file = 'yougo_20241030.xlsx'
input_cols = 'B,C,D,E'
input_names = ['term','def','comment','reference']
sheet_names = {
        'sheet_a',
        'sheet_b',
        'sheet_c' }

out_dir = './docs-20241030'

if (len(input_cols.split(',')) != len(input_names)):
    print("error: wrong input parameter")
    exit()
if not out_dir.endswith('/'):
    out_dir = f"{out_dir}/"
if not os.path.isdir(out_dir):
    print(f"error: directory does not exist - {out_dir}")
    exit()

print(f"site_name: {site_name}")
print("theme:")
print("    name: 'material'")
print("    language: 'ja'")
print("extra:")
print("    search:")
print("      language: 'ja'")
print("plugins:")
print("  - search")
print("#  - pdf-export")
print("nav:")
print("  - About:")
print("    - index.md")

try:
    with open(input_file, 'rb') as f_in:
        for sheet in sheet_names:
            df = pd.read_excel(f_in,
                sheet_name = sheet,
                header = 0,
                usecols = input_cols,
                names = input_names)
            df = df.sort_values('term')

            print(f"  - {sheet}:")

            for index, row in df.iterrows():
                if pd.isna(row['term']):
                    break
                item_name = row['term']
                definition = row['def']
                comment = row['comment']
                ref = row['reference']

                file_name = f"{item_name}.md"
                file_path = f"{out_dir}/{file_name}.md"
                print(f"    - {file_name}")

                try:
                    with open(file_path, "w", encoding = 'utf-8') as f_out:
                        f_out.write(f"# {item_name}\n")
                        f_out.write(f"{definition}\n")
                        if not pd.isna(comment):
                            f_out.write(f"## 備考\n{comment}\n")
                        if not pd.isna(ref):
                            f_out.write(f"## リファレンス\n{ref}\n")
                except:
                    print(f"error: file write failed: {file_name} - {e}")

except Exception as e:
    print(f"error: {e}")
