from setuptools import setup

# Parse README.md as long_description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Parse requirements.txt as install_requires
with open("requirements.txt", "r", encoding="utf-8") as f:
    require = f.read().splitlines()

# !TODO: Change these settings
setup(
    name="example_package", # Name of the package
    version="0.0",
    description="An example package",
    author="Kristóf Müller, You",
    author_email="muller.kristof@itk.ppke.hu, you@email.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://your-git.com",
    project_urls={"Bug Tracker": "http://your-git.com/issues",},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    packages=["example_package"], # Name of the package directory
    install_requires=[require],
    python_requires=">=3.10"
)