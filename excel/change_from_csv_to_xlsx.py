import os
import pandas as pd

def convert_csvs_in_subfolders(base_folder):
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith('.csv'):
                csv_path = os.path.join(root, file)
                xlsx_path = os.path.splitext(csv_path)[0] + '.xlsx'

                try:
                    df = pd.read_csv(csv_path)
                    df.to_excel(xlsx_path, index=False)
                    print(f"✅ Converted: {csv_path} -> {xlsx_path}")
                except Exception as e:
                    print(f"❌ Failed: {csv_path} - {e}")

# Change this to your actual path
if __name__ == "__main__":
    base_dir = os.path.expanduser("~/data-brach/excel")
    convert_csvs_in_subfolders(base_dir)

