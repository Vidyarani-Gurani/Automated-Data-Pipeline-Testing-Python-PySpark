def validate_record_count(source_df, target_df):
    return source_df.count() == target_df.count()

def check_nulls(df, column_name):
    return df.filter(df[column_name].isNull()).count()
