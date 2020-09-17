
import sys
import os
import subprocess
import pandas as pd
from azureml.pipeline.wrapper import dsl
from azureml.pipeline.wrapper.dsl.component import componentExecutor, InputDirectory, OutputDirectory, StringParameter

@dsl.component(
    description='merge two datasets',
    name='nyc taxi merge',
)
def merge(
    cleaned_yellow_data: InputDirectory(description="cleaned yellow data, needs to be read as pandas dataframe"),
    cleaned_green_data: InputDirectory(description="cleaned green data, needs to be read as pandas dataframe"),
    merged_output: OutputDirectory(description="output data after merge"),
):

    green_df = pd.read_csv(cleaned_green_data)
    yellow_df = pd.read_csv(cleaned_yellow_data)

    print("Argument (output merge taxi data path): %s" % merged_output)

    merge_df = green_df.append(yellow_df, ignore_index = True)
    merge_df.reset_index(inplace=True, drop = True)

    if not (merged_output is None):
        os.makedirs(merged_output, exist_ok=True)
        print("merge output folder %s created" % merged_output)
        path = merged_output + "/merged.csv"
        write_df = merge_df.to_csv(path)

if __name__ == '__main__':
    componentExecutor(merge).execute(sys.argv)