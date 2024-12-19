from __future__ import annotations

import subprocess
import time
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from typing import Generator


@pytest.fixture
def runserver_ngrok() -> Generator[None, None, None]:
    process = subprocess.Popen(
        ["python", "manage.py", "runserver_ngrok"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    time.sleep(2)
    yield
    process.terminate()
