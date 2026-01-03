import pytest
from pyrobosim.core import WorldYamlLoader
import pathlib
from pyrobosim.utils.general import get_data_folder


@pytest.fixture(autouse=False, scope="module")
def world():
    """Create a reusable test world factory for sensors tests.

    Usage:
        w = world()  # loads default test_world.yaml
        w = world("other_world.yaml")  # loads another YAML in data folder
    """

    def _factory(filename: str = "test_world.yaml"):
        """Create a World from a YAML file in the data folder.
        
        :param filename: Name of YAML file in data folder.
        :return: World object.
        """
        return WorldYamlLoader().from_file(
            pathlib.Path(get_data_folder()) / filename,
        )

    return _factory