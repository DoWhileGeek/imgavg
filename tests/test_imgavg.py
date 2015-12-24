import os
import tempfile
import shutil

import numpy as np
import pytest
from PIL import Image

from imgavg import imgavg


def test_happy_path(args):
    with tempfile.TemporaryDirectory() as temp_dir:
        args["output"] = os.path.join(temp_dir, "out.png")
        result = imgavg.average(args)

    im = Image.open("tests/assets/happy_path/1.png")
    expected = np.array(im).astype(np.uint8)

    assert np.array_equal(result, expected)

@pytest.mark.xfail(raises=imgavg.InconsistentImageError)
def test_inconsistent_image_sizes(args):
    """you cant mix and match array shapes"""
    args["folder"] = "tests/assets/inconsistent_images/"

    imgavg.average(args)


@pytest.mark.xfail(raises=imgavg.InsufficientImagesError)
def test_no_images_in_folder(args):
    """you cant average images if there are no images"""
    with tempfile.TemporaryDirectory() as temp_dir:
        args["folder"] = temp_dir
        imgavg.average(args)


@pytest.mark.xfail(raises=imgavg.InsufficientImagesError)
def test_not_enough_images(args):
    """one picture isnt enough to average"""
    with tempfile.TemporaryDirectory() as temp_dir:
        shutil.copy("tests/assets/happy_path/1.png", os.path.join(temp_dir, "1.png"))
        args["folder"] = temp_dir
        imgavg.average(args)

