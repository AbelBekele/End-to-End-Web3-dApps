import os
import pytest
from dynamic_image_generator.utils import write_name

def test_write_name():
    name = "Test"
    file_name = write_name(name)
    assert isinstance(file_name, str)
    assert os.path.exists(file_name)
    os.remove(file_name)  # Clean up after test