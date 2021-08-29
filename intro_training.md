# Summary of Introductory Training

All of these videos are short and sharpish, Depending on your previous experience, choose the ones that are most helpful to get you up to speed.

Keep a list of questions and please ask for clarification on anything that doesn't make sense. We suggest using the Slack `#interns` channel as others
probably have the same question(s).

The tech-stack that we have chosen is quite intentional and based on (a lot of) research. However the world, particularly in our space, changes quickly so we are always happy to hear about other alternatives. At this point in time you'll need to learn the following (although our choices are informed by what are re-usable skills to take away).

## Gitpod.io

Gitpod is the (browser-delivered) platform that we use for our development work. It allows us to define our (disposable) environments in code and have a known starting point and the freedom to experiment without "fear", which is essential for learning to code and writing good quality, reproducible code.

https://www.gitpod.io/screencasts

### Always ready to code

https://www.gitpod.io/screencasts/always-ready-to-code

### Navigating your (Gitpod) workspace

https://www.gitpod.io/screencasts/navigating-your-workspace

## Visual Studio Code (VS Code)

Visual Studio Code is a (free) integrated development environment (IDE) provided by Microsoft. Ultimately it is a text editor with lots of cool (community-contributed) extensions for being more productive and reducing errors. If you like using Vim, Emacs, Atom, JetBrains, nano etc and think you'll be more productive with one of these then let's have a chat.

There are lots of videos on various aspects of VS Code.

https://code.visualstudio.com/docs/getstarted/introvideos

Also there are some tutorials on Python and Data Science within VS Code. Some of this information may be out of date as there is a lot of active development in this part of the ecosystem currently.

https://code.visualstudio.com/docs/python/python-tutorial

Please note that Jupyter notebooks can now be run/edited from within the VS Code environment.

https://code.visualstudio.com/docs/datascience/overview



## Python

### Conda

We use `conda` as a cross-platform package manager. We install conda and then Python and a list of default packages in an enviroment called `condadb`.

`conda` is an open-source package manager very popular in the Python ecosystem that can be used as an alternative to `pip` (and in combination with `pip`). It is especially helpful when distributing packages that rely on compiled libraries (e.g. when you need to use some `C` code to achieve performance improvements). It can use Anaconda as its standard repository (a `PyPI` equivalent in the `conda` world), however we are using the more open conda-forge (and `mamba`) ecosystem at this point in time - not Anaconda.

The main advantage of `conda` compared to virtual-environment (`venv`) based tools is that it unifies several different tools and has a deeper isolation than the `pip` package manager. For instance `conda` allows you to create isolated environments by specifying also the Python version and even system libraries (e.g. `glibc`). In the `pip` ecosystem, one needs a tool like `pyenv` to choose the Python version and the installation of system libraries besides the current ones is not possible at all.

Again, like a lot of things in this space, there are other options. Michael has tried many/most of them. e.g. I do not recommend `pipenv`. Poetry is an interesting possibility. `conda` highly recommended for now.

### JupyterLab and Jupyter notebook

There is lots of general information here - https://jupyter.org

https://youtu.be/Ozq24uAshXo?t=40 (first 10 mins - 1.25 speed recommended)

ASIDE: Read Michael's article on the Titanic data set. https://www.databooth.com.au/posts/titanic-data-quality/

