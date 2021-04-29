from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = fh.read().strip().split('\n')

setup(
    name="swifind",
    version="0.1",
    author="Leonardi Fabianto",
    author_email="av.leonardif@gmail.com",

    description="Web scraping scripting language and toolset.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avidito/swifind",

    packages=find_packages(),
    install_requires=install_requires,
    python_requires=">=3.6",
)
