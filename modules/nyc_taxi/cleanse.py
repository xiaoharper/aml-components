# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

import sys
import os
import subprocess
import pandas as pd
from azureml.pipeline.wrapper import dsl
from azureml.pipeline.wrapper.dsl.module import ModuleExecutor, InputDirectory, OutputDirectory, StringParameter


def get_dict(dict_str):
    pairs = dict_str.strip("{}").split(";")
    print(pairs)
    new_dict = {}
    for pair in pairs:
        print(pair)
        key, value = pair.strip().split(":")
        new_dict[key.strip().strip("'")] = value.strip().strip("'")

    return new_dict


@dsl.module(
    description='pick useful columns and rename',
    name='nyc clean',
)
def clean(
    input_data: InputDirectory(description="input data, needs to be read as pandas dataframe"),
    output_data: OutputDirectory(description="output data after clean"),
    useful_columns: StringParameter(description="columns to keep, format example: ""'vendorID','fareAmount'"""),
    new_names: StringParameter("new names mapping, format example: " "'vendorID': 'vendor'; 'fareAmount': 'cost'" "")
):

    print("Argument 1(columns to keep): %s" % str(useful_columns.strip("[]").split("\;")))
    print("Argument 2(columns renaming mapping): %s" % str(new_names.strip("{}").split("\;")))
    print("Argument 3(output cleansed taxi data path): %s" % output_data)

    # These functions ensure that null data is removed from the dataset,
    # which will help increase machine learning model accuracy.
    raw_data = pd.read_csv(input_data)
    useful_columns_list = [s.strip().strip("'") for s in useful_columns.strip("[]").split(",")]
    new_names_dict = get_dict(new_names)

    new_df = raw_data.dropna(how='all')
    new_df = new_df.rename(columns=new_names_dict)
    new_df = new_df[useful_columns_list]
    new_df.reset_index(inplace=True, drop=True)

    if not (output_data is None):
        os.makedirs(output_data, exist_ok=True)
        print("output folder %s created" % output_data)
        path = output_data + "/processed.csv"
        write_df = new_df.to_csv(path)


if __name__ == '__main__':
    ModuleExecutor(clean).execute(sys.argv)

