import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

version = "0.1.0"
REPO_NAME = "MLOps-E2E"
AUTHOR_USER_NAME = "mrunal-i"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "mrunalingale2001@gmail.com"

setuptools.setup(
    name="mlproject",
    version=version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for MLOps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)