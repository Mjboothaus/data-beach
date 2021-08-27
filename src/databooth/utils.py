from IPython.display import Markdown, display
from pathlib import Path

def in_notebook() -> bool:
    """
    Returns ``True`` if the module is running in IPython kernel,
    ``False`` if in IPython shell or other Python shell.
    """
    #return "ipykernel" in sys.modules
    try:
        __IPYTHON__
        return True
    except NameError:
        return False


def get_project_root() -> Path:
    if not in_notebook():
        print("NOT in Jupyter notebook")
        return Path(__file__).parent.parent
    else:
        print("In Jupyter notebook")
        return Path.cwd().parent

# def get_notebook_name():


def load_display_markdown(dotmd_file):
    dotmd_file_ext = Path(dotmd_file).suffix
    if dotmd_file_ext == ".md":
        if Path(dotmd_file).exists() == True:
            display(Markdown(Path(dotmd_file)))
        else:
            print('File not found: ' + dotmd_file)
    else:
        print('Invalid file extension: ' + dotmd_file_ext + ' - should be .md')
