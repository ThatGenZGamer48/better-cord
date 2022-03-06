from setuptools import setup

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()
    
setup(
    name="bettercord",
    packages=["discord.ext.bettercord"],
    version="0.0.1",
    license="MIT",
    description="A module made to make Pycord easier to code in.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="That GenZ Gamer",
    url="https://github.com/ThatGenZGamer48/better-cord",
    keywords="pycord, py-cord",
    install_requires=[],
    classifiers=classifiers,
    project_urls={"Source": "https://github.com/ThatGenZGamer48/better-cord"},
)
