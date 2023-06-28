import argparse
import glob
import os

import pandas as pd

# Create the parser to determine root directory from argument in the command line
parser = argparse.ArgumentParser(description="Process .txt files in a directory")
parser.add_argument(
    "--txt-dir",
    type=str,
    required=True,
    help="The directory containing .txt files that we want to process after CellProlifer feature extracion.",
)
args = parser.parse_args()
txt_dir = args.txt_dir

# Get all .txt files in the specified directory
txt_files = glob.glob(os.path.join(txt_dir, "*.txt"))

# Get the directory of the script and search for meta_table.txt
script_dir = os.path.dirname(os.path.realpath(__file__))
df_meta = pd.read_csv(os.path.join(script_dir, "meta_table.txt"), sep="\t", dtype=str)

# Exclude "meta_table.txt" and read it to data frame
txt_files = [file for file in txt_files if os.path.basename(file) != "meta_table.txt"]


# To determine correct data type for selected columns
def convert_df(df_raw_ID, df_meta):
    for index, row in df_meta.iterrows():
        row_name = row["Row_name"]
        aggregation_type = row["aggregation_type"]

        if (
            aggregation_type.lower() in ["sum", "mean"]
            and row_name in df_raw_ID.columns
        ):
            df_raw_ID[row_name] = pd.to_numeric(df_raw_ID[row_name], errors="coerce")
    return df_raw_ID


# To aggregate (pool) according to "meta_table.txt"
def aggregate_df(df_raw_ID, df_meta):
    # create a mapping of column names and their aggregation types
    original_mapping = dict(zip(df_meta.Row_name, df_meta.aggregation_type))

    # create a new dictionary for storing updated mappings
    aggregation_mapping = {}

    # change the 'sum' or 'mean' to the correct function names
    for column, agg_type in original_mapping.items():
        if agg_type.lower() == "sum":
            aggregation_mapping[column] = "sum"
        elif agg_type.lower() == "mean":
            aggregation_mapping[column] = "mean"
        else:
            del aggregation_mapping[column]
    df_agg = df_raw_ID.groupby("Unique_ID").agg(aggregation_mapping)
    df_agg = df_agg.reset_index()

    return df_agg


for file in txt_files:
    # Load the data
    df_raw = pd.read_csv(file, sep="\t", dtype=str)
    # Pipeline to process the raw files
    df_raw[
        [
            "FileName_Mito_1",
            "FileName_Mito_2",
            "FileName_Mito_3",
            "FileName_Mito_4",
            "FileName_Mito_5",
            "FileName_Mito_6",
            "FileName_Mito_7",
            "FileName_Mito_8",
            "Unique_ID",
            "FileName_Mito_10",
            "FileName_Mito_11",
        ]
    ] = df_raw["FileName_Mito"].str.split("_", expand=True)
    df_raw_ID = df_raw.drop(
        [
            "FileName_Mito_1",
            "FileName_Mito_2",
            "FileName_Mito_3",
            "FileName_Mito_4",
            "FileName_Mito_5",
            "FileName_Mito_6",
            "FileName_Mito_7",
            "FileName_Mito_8",
            "FileName_Mito_10",
            "FileName_Mito_11",
        ],
        axis=1,
        errors="ignore",
    )
    df_raw_ID = convert_df(df_raw_ID, df_meta)
    df_agg = aggregate_df(df_raw_ID, df_meta)
    df_unique = df_raw_ID.drop_duplicates(subset="Unique_ID")
    df_unique = df_unique[["FileName_Mito", "Unique_ID"]]
    df_merged = pd.merge(df_agg, df_unique, how="left", on="Unique_ID")
    os.makedirs(os.path.join(txt_dir, "processed"), exist_ok=True)
    processed_filename = os.path.splitext(os.path.basename(file))[0] + "_processed.txt"
    df_merged.to_csv(
        os.path.join(txt_dir, "processed", processed_filename), sep="\t", index=False
    )

print("Done!")
