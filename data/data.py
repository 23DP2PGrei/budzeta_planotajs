import csv

STANDARD_COLUMNS = ["Food", "Healthcare", "Rent", "Loans"]
BASE_COLUMNS = ["User ID", "Month", "Monthly Income"] + STANDARD_COLUMNS + ["Balance"]

def save_data_to_csv(file_path, user_id, month, income, spending_data, balance):
    row = {
        "User ID": user_id,
        "Month": month,
        "Monthly Income": income
    }

    for key in STANDARD_COLUMNS:
        row[key] = spending_data.get(key, 0)

    for key, value in spending_data.items():
        if key not in STANDARD_COLUMNS:
            row[key] = value

    row["Balance"] = balance

    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        headers = list(row.keys())
        writer = csv.DictWriter(f, fieldnames=headers)

        writer.writeheader()
        writer.writerow(row)
