# Summary of Introductory Training

All of these videos are short and sharpish, Depending on your previous experience, choose the ones that are most helpful to get you up to speed.

Keep a list of questions and please ask for clarification on anything that doesn't make sense. We suggest using the Slack `#interns` channel as others
probably have the same question(s).

The tech-stack that we have chosen is quite intentional and based on (a lot of) research. However the world, particularly in our space, changes quickly so we are always happy to hear about other alternatives. At this point in time you'll need to learn the following (although our choices are informed by what are re-usable skills to take away).

## Operating the "right" way 

DataBooth has values which are central to the way we operate and do business. These values are evolving:
* Integrity -- our yes is yes and our no is no. People can take us at our word. We say what me mean, and we mean what we say.
* Joy -- while we recognise that we live in a very flawed world, we aim to en-joy our work, value our colleagues and clients and not take ourselves too seriously,
* Quality matters - see more on reproducibility below.
* Collaboration - working together is more fun and leads to better solutions. Look for opportunities to pair-program. Our simple rule is that it is fine to "struggle" alone for a short while, but not a long time. So if you're stuck for more than 60 minutes on a task - ping someone on Slack and ask! :)
* IN PROGRESS

### The Turing Way - A great resource/reference

The [Turing Way](https://the-turing-way.netlify.app) is a handbook to reproducible, ethical and collaborative data science. Any time spent exploring this wonderful resource is a great use of your time. Feel welcome to ask questions, make comments, raise objections.

By the way, I assume it gets its name from [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing), a quite amazing human. His life is portrayed in the film - [The Imitation Game](https://en.wikipedia.org/wiki/The_Imitation_Game) which I'm happy to recommend.
### Putting it into practice

This area of ethical (explainable and sustainable) AI has grown rapidly of late, as the GDPR, CDR, APP legislation has filtered through the data science ecosystem. Here are just a couple of examples of the resources available.

* Deon - [https://deon.drivendata.org](https://deon.drivendata.org) - while we are not interested in
a compliance approach to things, i.e. we want our hearts and minds into it, this ethics checklist for data science is a useful resource.
* The Institute for Ethical AI & Machine Learning - https://ethical.institute

We will use the Deon library in the first instance to guide us.
## GitHub - versioning, issue management and lots more

This is probably the place to start. We need to add you to the DataBooth team and give you appropriate permissions.

## Tara.AI - Collaboratively developing software (Project Management)

Tara AI is a simple yet powerful project management software for teams. It helps us:
* define requirements, 
* assign tasks, 
* plan sprints (blocks of work), and 
* track progress/plan.

There are some initial Tara training resources here:

https://help.tara.ai/en/

Again please choose what is helpful/relevant (and ask if you're not sure). We have a great relationship with the team at Tara - so we can get help from them when/if needed.

## Gitpod.io - where we do our development work (mostly in Python)

Gitpod is the (browser-delivered) platform that we use for our development work. 
It allows us to define our (disposable) environments in code and have a known starting point and the freedom to experiment without "fear", which is essential for learning to code and writing good quality, reproducible code.

There are some initial Gitpod training resources here:

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

We mostly do development work in Python - although we're open-minded about this. Certainly Python (and its ecosystem) are the *lingua franca* of data scientists at this point in time. It is a very transferrable skill.
Although, we want you to think critically about how to solve problems and potential algorithms to do this. Python is just a (convenient) language to assist in implementing our ideas.
### Conda

We use `conda` as a cross-platform package manager. We install conda and then Python and a list of default packages in an enviroment called `condadb`.

`conda` is an open-source package manager very popular in the Python ecosystem that can be used as an alternative to `pip` (and in combination with `pip`). It is especially helpful when distributing packages that rely on compiled libraries (e.g. when you need to use some `C` code to achieve performance improvements). It can use Anaconda as its standard repository (a `PyPI` equivalent in the `conda` world), however we are using the more open conda-forge (and `mamba`) ecosystem at this point in time - not Anaconda.

The main advantage of `conda` compared to virtual-environment (`venv`) based tools is that it unifies several different tools and has a deeper isolation than the `pip` package manager. For instance `conda` allows you to create isolated environments by specifying also the Python version and even system libraries (e.g. `glibc`). In the `pip` ecosystem, one needs a tool like `pyenv` to choose the Python version and the installation of system libraries besides the current ones is not possible at all.

Again, like a lot of things in this space, there are other options. Michael has tried many/most of them. e.g. I do not recommend `pipenv`. Poetry is an interesting possibility. `conda` highly recommended for now.

### JupyterLab and Jupyter notebook

There is lots of general information here - https://jupyter.org

https://youtu.be/Ozq24uAshXo?t=40 (first 10 mins - 1.25 speed recommended)

ASIDE: Read Michael's article on the Titanic data set. https://www.databooth.com.au/posts/titanic-data-quality/


## References

* The Turing Way Community, Becky Arnold, Louise Bowler, Sarah Gibson, Patricia Herterich, Rosie Higman, … Kirstie Whitaker. (2019, March 25). The Turing Way: A Handbook for Reproducible Data Science (Version v0.0.4). Zenodo. http://doi.org/10.5281/zenodo.3233986.

