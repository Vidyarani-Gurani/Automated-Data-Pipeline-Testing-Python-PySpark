import pandas as pd

source = pd.read_csv("../datasets/source_data.csv")
target = pd.read_csv("../datasets/target_data.csv")

def validate_row_count():
    assert len(source) == len(target)

def validate_nulls():
    assert source.isnull().sum().sum() == 0
    assert target.isnull().sum().sum() == 0

validate_row_count()
validate_nulls()

print("Data validation completed successfully")
