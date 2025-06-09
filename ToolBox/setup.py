from setuptools import setup

# Parse README.md as long_description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Parse requirements.txt as install_requires
with open("requirements.txt", "r", encoding="utf-8") as f:
    require = f.read().splitlines()

# !TODO: Change these settings
setup(
    name="GenomeVisualizer", # Name of the package
    version="0.0.1",
    description="Toolbox for Detecting DNA Replication Origins and Regulatory Motifs in Genomic Sequences",
    author="Varga Henrietta",
    author_email="varga.henrietta.julianna@hallgato.ppke.hu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vargaheni05/GenomeVisualizer",
    project_urls={"Bug Tracker": "https://github.com/vargaheni05/GenomeVisualizer/issues",},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    packages=["GenomeVisualizer"], # Name of the package directory
    install_requires=[require],
    python_requires=">=3.10"
)