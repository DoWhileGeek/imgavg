import contextlib
import json
import os
import re
import subprocess

from setuptools import setup

VERSION_FILE = os.path.join(os.path.dirname(__file__), "version.json")


def _get_git_description():
    try:
        return subprocess.check_output(["git", "describe"]).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        return None


def _create_version_from_description(git_description):
    match = re.match(r"(?P<tag>[\d\.]+)-(?P<offset>[\d]+)-(?P<sha>\w{8})", git_description)
    if not match:
        version = git_description
    else:
        version = "{tag}.post{offset}".format(**match.groupdict())
    return version


def get_version():
    with open(VERSION_FILE) as version_file:
        return json.loads(version_file.read())["version"]


@contextlib.contextmanager
def write_version():
    git_description = _get_git_description()

    version = _create_version_from_description(git_description) if git_description else None

    if version:
        with open(VERSION_FILE, "w") as version_file:
            version_file.write(json.dumps({"version": version}))
    yield


def main():
    with write_version():
        setup(
            name="imgavg",
            url="https://github.com/DoWhileGeek/imgavg",
            description="A command line utility that outputs the average of a number of pictures.",
            author="Joeseph Rodrigues",
            author_email="dowhilegeek@gmail.com",
            version=get_version(),
            install_requires=[
                "numpy==1.10.2",
                "Pillow==3.0.0"
            ],
            extras_require={
                "develop": [
                    "pytest==2.8.5",
                    "twine==1.5.0",
                ]},
            packages=[
                "imgavg"
            ],
            package_data={
                "imgavg": ["imgavg/*"],
            },
            scripts=["bin/imgavg"]
        )


if __name__ == "__main__":
    main()
