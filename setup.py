from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_args = dict(
    name="apiclient-gonzalo123",
    version="1.0.2",
    author="Gonzalo Ayuso",
    author_email="gonzalo123@gmail.com",
    description="apiclient",
    long_description=long_description,
    license='MIT',
    long_description_content_type="text/markdown",
    keywords=['apiclient'],
    url="https://github.com/gonzalo123/apiclient",
    packages=['apiclient'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5'
)

install_requires = [
    'requests>=2.3.0'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)