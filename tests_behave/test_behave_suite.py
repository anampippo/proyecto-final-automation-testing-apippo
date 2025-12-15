import subprocess
import os

def run_behave(tags=None):
    os.makedirs("reports", exist_ok=True)

    command = [
    "python3",
    "-m",
    "behave",
    "-f", "json",
    "-o", "reports/behave.json",
    "-f", "pretty"
]


    if tags:
        command.extend(["-t", tags])

    result = subprocess.run(command)
    assert result.returncode == 0


def test_behave_smoke():
    run_behave("@smoke")


def test_behave_regression():
    run_behave("@regression")