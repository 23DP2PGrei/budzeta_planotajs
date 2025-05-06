import csv

STANDARD_COLUMNS = ["Food", "Healthcare", "Rent", "Loans"] # Noklusētās kategorijas
BASE_COLUMNS = ["User ID", "Month", "Monthly Income"] + STANDARD_COLUMNS + ["Balance"] # Pamata kolonnas

def save_data_to_csv(file_path, user_id, month, income, spending_data, balance):
    row = {
        "User ID": user_id,
        "Month": month,
        "Monthly Income": income
    } # Izveido sākotnējo rindu ar pamata informāciju
    
    # Pievieno noklusētās kategorijas ar vērtībām (vai 0, ja nav)
    for key in STANDARD_COLUMNS:
        row[key] = spending_data.get(key, 0)

    # Pievieno lietotāja pievienotās papildu kategorijas
    for key, value in spending_data.items():
        if key not in STANDARD_COLUMNS:
            row[key] = value

    row["Balance"] = balance # Pievieno atlikumu

    # Raksta CSV failā
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        headers = list(row.keys()) # Dinamiski veido kolonnu sarakstu
        writer = csv.DictWriter(f, fieldnames=headers)

        writer.writeheader() # Pieraksta kolonnas (katru reizi, kas nav ideāli — to var uzlabot)
        writer.writerow(row) # Pieraksta vienu rindu
