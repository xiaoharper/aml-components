import sys
import runpy
from enum import Enum
from azureml.pipeline.wrapper import dsl
from azureml.pipeline.wrapper.dsl.component import componentExecutor, InputDirectory, OutputDirectory


class EnumEnumParam(Enum):
    val1 = 'val1'
    val2 = 'val2'


@dsl.component(
    description='A sample component which shows the input data.',
    name='Prepare data',
)
def prepare_data(
    output_data: OutputDirectory(),
    input_data: InputDirectory() = None,
    str_param: str = None,
    int_param: int = 0,
    enum_param: EnumEnumParam = None,
):
    sys.argv = [
        'prepare_data.py',
        '--input_data', str(input_data),
        '--output_data', str(output_data),
        '--int_param', str(int_param),
    ]
    if str_param is not None:
        sys.argv += ['--str_param', str(str_param)]
    if enum_param is not None:
        sys.argv += ['--enum_param', enum_param.value]
    print(' '.join(sys.argv))
    runpy.run_path('prepare_data.py', run_name='__main__')


if __name__ == '__main__':
    componentExecutor(prepare_data).execute(sys.argv)
