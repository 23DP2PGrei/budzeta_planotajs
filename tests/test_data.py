import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import csv
from data.data import save_data_to_csv

def test_save_data_to_csv(tmp_path):
    # Izveido pagaidu failu
    file_path = tmp_path / "test_output.csv"

    # Ievaddati
    spending_data = {"Food": 100, "Healthcare": 50, "Rent": 300, "Custom": 25}
    user_id = "user123"
    month = "May"
    income = "1000"
    balance = 525

    # Izsauc funkciju
    save_data_to_csv(file_path, user_id, month, income, spending_data, balance)

    # Nolasa failu
    with open(file_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Pārbaude
    assert len(rows) == 1
    row = rows[0]
    assert row["User ID"] == "user123"
    assert row["Month"] == "May"
    assert row["Monthly Income"] == "1000"
    assert row["Food"] == "100"
    assert row["Healthcare"] == "50"
    assert row["Rent"] == "300"
    assert row["Custom"] == "25"
    assert row["Balance"] == "525"