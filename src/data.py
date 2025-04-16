import csv
import os

STANDARD_COLUMNS = ["Food", "Healthcare", "Rent", "Loans"]
BASE_COLUMNS = ["User ID", "Month", "Monthly Income"] + STANDARD_COLUMNS

def get_current_headers(file_path):
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, newline='', encoding='utf-8') as f:
            return next(csv.reader(f))
    return BASE_COLUMNS + ["Balance"]

def save_data_to_csv(file_path, user_id, month, income, spending_data, balance):
    current_headers = get_current_headers(file_path)
    extra_keys = [k for k in spending_data if k not in STANDARD_COLUMNS]
    new_headers = BASE_COLUMNS + extra_keys + ["Balance"]

    all_headers = list(dict.fromkeys(current_headers + new_headers))

    row = {
        "User ID": user_id,
        "Month": month,
        "Monthly Income": income,
        "Balance": balance
    }
    row.update(spending_data)

    rows = []
    if os.path.exists(file_path):
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for existing_row in reader:
                rows.append(existing_row)

    rows.append(row)

    with open(file_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=all_headers)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
