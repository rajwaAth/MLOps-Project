import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_desc = f.read()

__version__ = "0.0.1"

REPO_NAME = "end_to_end_project"
AUTHOR_NAME = "mrath"
SRC_REPO = "end_to_end_project"
AUTHOR_EMAIL = "rath@me.com" # just an example

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for end to end project (excercise) setup",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
)