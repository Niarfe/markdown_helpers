from setuptools import setup, find_packages

setup(
      name='markdown_helpers',
      version='0.0.2',
      description='Markdown formatting helpers',
      author='Efrain Olivares',
      author_email='efrain.olivares@gmail.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    )
