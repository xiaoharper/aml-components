import sys
from pathlib import Path
import pandas as pd
import rtree
import gdal

from azureml.pipeline.wrapper.dsl.component import componentExecutor, InputDirectory, OutputDirectory
from azureml.studio.core.io.data_frame_directory import load_data_frame_from_directory
from azureml.pipeline.wrapper import dsl



gdal_version_num = int(gdal.VersionInfo('VERSION_NUM'))
print(f'gdal version number is {gdal_version_num}.')


@dsl.component(
    name="gdal_sample"
)
def gdal_sample(
    ##define interface(input, output, paratmers) of the component here 
        output_dir1: OutputDirectory(),
        output_dir2: OutputDirectory(),
        input_dir1: InputDirectory(),
        input_dir2: InputDirectory()
):
    print('I am in component definition')
    print(f'input_dir1: {Path(input_dir1).resolve()}')
    print(f'input_dir2: {Path(input_dir2).resolve()}')
   
   ## add custom logic here
    
    dfd1 = load_data_frame_from_directory(input_dir1)
    data_frame1 = dfd1.data
    print(data_frame1.head(10))


if __name__ == '__main__':
    componentExecutor(gdal_sample).execute(sys.argv)
