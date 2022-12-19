import subprocess
import sys
from time import sleep

import pytest


@pytest.mark.parametrize("module", "src.main_dummy")
def test_main(module: str):
    process = subprocess.Popen([sys.executable, "-m", module])
    sleep(5)  # wait for the app to load
    process.kill()
