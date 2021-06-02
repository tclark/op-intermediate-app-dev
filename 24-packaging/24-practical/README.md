
# Practical  24: Python Packaging 

In today's practical we're going to build an installable Python package and 
upload to https://test.pypi.org. Then it will be possible to install the packageusing `pip`. There is not one standard way to create an installable Python package and it's actually more complicated that it probably should be for complex packages. We will set up our packages using [`setuptools`](https://setuptools.readthedocs.io/en/latest/index.html), which is probably the most widely used version.

This directory contains a Python project set up with a structure that works reasonably well for general projects. Again, there are other ways to do it. This directory already contains

  - this README
  - a LICENSE file. If you're going to distribute code you need to provide a license that gives permissions for its use. This licence file specifies the GPLv3, but there are many options (perhaps too many).
  - a `src` directory that contains the actual Python source for our project
  - a `tests` directory for tests that are part of the project but won't be included in the installable package. Our `tests` directory is empty, because YOLO.

All of the commands that we will use enter should be entered in the same working directory that contains this README.

## Steps

1. Create a `pyproject.toml` file. Since there are multiple build systems for Python packages, the `pyproject.toml` file is intended to provide a generally compatible configuration file than can be used by them. Since we are using setuptools, our project need to include the following

    [build-system]
    requires = [
    "setuptools>=42",
    "wheel"
    ]
    build-backend = "setuptools.build_meta"
```

There are many [other options](https://martin-thoma.com/pyproject-toml/), but this is sufficient for our project.

2. Next, create a `setup.cfg` file that provides information for setuptools. Alternatively, you can  provide a `setup.py` file that determines package informatin dynamically, but a typical project should not need this. Your `setup.cfg` should be similar to this

```
    [metadata]
    name = example-pkg-YOUR-USERNAME-HERE
    version = 0.0.1
    author = Your Name
    author_email = your_email@example.com
    description = Practical Lab 24 
    long_description = file: README.md
    long_description_content_type = text/markdown
    url = https://github.com/your/projectrepo
    project_urls =
        Bug Tracker = https://github.com/your/projectrepo/issues
    classifiers =
        Programming Language :: Python :: 3
        License :: OSI Approved :: GNU General Public License v3 (GPLv3)
        Operating System :: OS Independent

    [options]
    package_dir =
        = src
    packages = find:
    python_requires = >=3.7

    [options.packages.find]
    where = src
```

Most of these options are pretty self-explanatory. Note that you don't actually need to create a GitHub repo for this lab. Take note of the `options` sections that specify the minimum Python version required for our package, and the location (`src`) of the files that should be installed by the package. Another option is `install_requires` with which you can list any other packages required by this one.

3. Now we are ready to build the package. First, make sure you have the `build` module installed.


    pip3 install --user --upgrade build

And now build your package (working from the same directory where this README is saved).

    python3 -m build

On Windows you may need to use 

    py -m build

This command will create a `dist` directory with two package files: a `tar.gz` file that contains the source distribution used by some old versions of `pip` and a `.whl` file used by newer versions.

4. Finally we need to upload our package to the Python index. We will use the test version of the index in this case. First you'll need to go to https://test.pypi.org and create an account.

Once your account is ready, create an API token from https://test.pypi.org/manage/account/#api-tokens. Set the scope to the entire account.  Copy and save thetoken, although you can create a new one if necessary.

To upload your packages, you'll need to install `twine`.

    pip3 install --user --upgrade twine

And then upload your package with the command

    python3 -m twine upload --repository testpypi dist/*

You'll be prompted for a username and password. For the username, enter `__token__`. For the password, paste the token you obtained earlier.

5. Now you can install your package with the command

    pip3 install --index-url https://test.pypi.org/simple/ your-package-name

## Next steps
From here, you can adapt this process easily to use the live PyPi index instead. It's also possible to host your own packaging index if needed for your own in-house projects.

