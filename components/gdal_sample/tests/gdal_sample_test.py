import sys
import unittest
from pathlib import Path

from azureml.core import Workspace
from azureml.pipeline.wrapper import component

# The following line adds source directory to path.
sys.path.insert(0, str(Path(__file__).parent.parent))
from gdal_sample import gdal_sample


class TestGdalSample(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.workspace = Workspace.from_config(str(Path(__file__).parent.parent / 'config.json'))
        cls.base_path = Path(__file__).parent.parent / 'data'

    def prepare_inputs(self) -> dict:
        # Change to your own inputs
        return {'input_dir': str(self.base_path / 'gdal_sample' / 'inputs' / 'input_dir')}

    def prepare_outputs(self) -> dict:
        # Change to your own outputs
        return {'output_dir': str(self.base_path / 'gdal_sample' / 'outputs' / 'output_dir')}

    def prepare_parameters(self) -> dict:
        # Change to your own parameters
        return {'str_param': 'some_string'}

    def prepare_arguments(self) -> dict:
        # If your input's type is not Path, change this function to your own type.
        result = {}
        result.update(self.prepare_inputs())
        result.update(self.prepare_outputs())
        result.update(self.prepare_parameters())
        return result

    def test_component_from_func(self):
        # This test calls gdal_sample from cmd line arguments.
        local_component = component.from_func(self.workspace, gdal_sample)
        component = local_component()
        component.set_inputs(**self.prepare_inputs())
        component.set_parameters(**self.prepare_parameters())
        status = component.run(use_docker=True)
        self.assertEqual(status, 'Completed', 'component run failed.')

    def test_component_func(self):
        # This test calls gdal_sample from parameters directly.
        gdal_sample(**self.prepare_arguments())
