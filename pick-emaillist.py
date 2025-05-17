import pandas as pd
import os

def extract_emails(file_path, column_name, output_file):
    try:
        # Excelファイルの読み込み
        df = pd.read_excel(file_path, engine='openpyxl')
    except FileNotFoundError:
        print(f"エラー: ファイル '{file_path}' が見つかりません。")
        return
    except Exception as e:
        print(f"エラー: ファイルの読み込み中に問題が発生しました。詳細: {e}")
        return

    if column_name not in df.columns:
        print(f"エラー: 指定した列名 '{column_name}' が見つかりません。")
        return

    try:
        # メールアドレスの抽出
        email_addresses = df[column_name].dropna().tolist()
        email_string = '; '.join(email_addresses)
        email_count = len(email_addresses)

        # テキストファイルに保存
        with open(output_file, 'w') as f:
            f.write(f"Total email addresses: {email_count}\n")
            f.write(email_string)
            f.write('\n') # ファイルの最後に改行を追加

        print(f"メールアドレスが '{output_file}' に保存されました。")
    except Exception as e:
        print(f"エラー: メールアドレスの抽出または保存中に問題が発生しました。詳細: {e}")

# 使用例
file_path = 'your_excel_file.xlsx'
column_name = 'メールアドレス'
output_file = 'email_addresses.txt'

extract_emails(file_path, column_name, output_file)
