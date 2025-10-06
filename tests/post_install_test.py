import subprocess
import sys

def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def test_hello():
    out = run("python tasks/hello_world.py")
    assert "hello from agent task" in out.stdout

def test_health():
    out = run("python tasks/healthcheck.py")
    assert "HEALTH=OK" in out.stdout or "MISSING_ENV=" in out.stdout
