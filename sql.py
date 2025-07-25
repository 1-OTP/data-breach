import os
import pandas as pd

input_dir = "/home/kali/.local/share/sqlmap/output/www.ptt.co.th/dump"
output_sql_file = "dump_all.sql"

with open(output_sql_file, "w", encoding="utf-8") as out_sql:
    for db_name in os.listdir(input_dir):
        db_path = os.path.join(input_dir, db_name)
        if not os.path.isdir(db_path):
            continue

        for table_file in os.listdir(db_path):
            if table_file.endswith(".csv") or table_file.endswith(".txt"):
                table_name = table_file.rsplit('.', 1)[0]
                file_path = os.path.join(db_path, table_file)
                try:
                    df = pd.read_csv(file_path, engine='python')
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
                    continue

                columns = df.columns.tolist()
                for _, row in df.iterrows():
                    values = [f"'{str(val).replace('\'', '\\\'')}'" for val in row.tolist()]
                    insert_stmt = f"INSERT INTO `{table_name}` ({', '.join(columns)}) VALUES ({', '.join(values)});\n"
                    out_sql.write(insert_stmt)

print(f"[✔] SQL dump saved to {output_sql_file}")

