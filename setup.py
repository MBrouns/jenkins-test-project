from setuptools import setup, find_packages

base_dependencies = [
]

dev_dependencies = [
    "pytest",
    "flake8",
    "mypy",
]

all = dev_dependencies

setup(
    name="testproject",
    version="0.1",
    author="Matthijs Brouns",
    description="...",
    install_requires=base_dependencies,
    extras_require={
        "all": all,
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
