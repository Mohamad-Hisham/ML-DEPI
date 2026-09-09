import pandas as pd

def replace_outliers_with_fences(df, num_cols):
    for col in num_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        IQR = q3 - q1
        lower_fence = q1 - 1.5 * IQR
        upper_fence = q3 + 1.5 * IQR
        df[col] = df[col].clip(lower_fence, upper_fence)
    return df