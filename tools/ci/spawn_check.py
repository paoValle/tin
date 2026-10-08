#!/usr/bin/env python3
"""Run the #576 spawn tests: natively on macOS, in a Linux container on Linux.

The tests start real processes, so they cannot run in the empty-root image; debian:bookworm-slim
provides the programs. On Linux the fixture is built for the host's architecture and run in that
architecture's container, so the check works on a Linux runner and on a Mac's Docker VM alike; on
macOS it is built for the host and run directly, exercising posix_spawn and the scheduler's wait. It
covers start and wait, exit codes, a missing program, PATH lookup, a working directory, signals,
a deadline that kills and reaps, a 1 MiB stdin pipe round trip, streaming reads, Run's separate
stdout and stderr, and the maxOutput cap.
"""
import os
import platform
import subprocess
import tempfile
from pathlib import Path

from suite import ROOT

EXPECTED = [
    'cat true 0 1048576 true',
    'deadline result -1',
    'deadline true',
    'dir 0 true',
    'echo 0',
    'hello',
    'killed -1',
    'limit true',
    'lookpath true',
    'loop fds equal true',
    'missing spawn: /no/such/tin-program: no such file or directory',
    'run 4 true true',
    'run deadline result false',
    'run deadline true',
    'sh exit 3',
    'stream true 0',
]


def host_target():
    machine = platform.machine()
    if machine in ('arm64', 'aarch64'):
        return 'linux-arm64', 'linux/arm64'
    if machine in ('x86_64', 'amd64'):
        return 'linux-amd64', 'linux/amd64'
    raise AssertionError(f'spawn_check: unknown host architecture {machine}')


def main():
    directory = ROOT / 'bin/ci/spawn'
    directory.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, TIN_ROOT=str(ROOT))
    with tempfile.TemporaryDirectory(prefix='spawn-', dir=directory) as tmp:
        work = Path(tmp)
        exe = work / 'spawn'
        if os.uname().sysname == 'Darwin':
            # macOS: the fixture runs directly, with posix_spawn and the kqueue wait.
            subprocess.run([str(ROOT / 'tin'), 'build', 'tools/ci/fixtures/spawn.tin', '-o', str(exe)],
                           check=True, cwd=ROOT, env=env, timeout=300)
            result = subprocess.run([str(exe)], capture_output=True, cwd=ROOT, timeout=300)
            where = 'macOS native (posix_spawn and the scheduler wait)'
        else:
            target, docker_platform = host_target()
            subprocess.run([str(ROOT / 'tin'), 'build', 'tools/ci/fixtures/spawn.tin', '-o', str(exe),
                            '--target', target], check=True, cwd=ROOT, env=env, timeout=300)
            result = subprocess.run(['docker', 'run', '--rm', '--platform', docker_platform,
                                     '-v', f'{exe}:/spawn', 'debian:bookworm-slim', '/spawn'],
                                    capture_output=True, cwd=ROOT, timeout=300)
            where = f'{target} in debian:bookworm-slim'
        (directory / 'spawn.stderr.log').write_bytes(result.stderr)
        assert result.returncode == 0, f'spawn: exit {result.returncode}: {result.stderr!r}'
        got = sorted(result.stdout.decode().splitlines())
        assert got == EXPECTED, f'spawn: got {got}, want {EXPECTED}'
        print(f'PASS spawn: {len(EXPECTED)} lines from {where}')


if __name__ == '__main__':
    main()
