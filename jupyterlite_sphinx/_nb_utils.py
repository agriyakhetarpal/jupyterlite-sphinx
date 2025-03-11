from importlib import import_module
import os
import nbformat


from typing import Callable, List, Optional


def _strip_notebook_cells(nb: nbformat.NotebookNode) -> List[nbformat.NotebookNode]:
    """Strip cells based on the presence of the "jupyterlite_sphinx_strip" tag
    in the metadata. The content meant to be stripped must be inside its own cell
    cell so that the cell itself gets removed from the notebooks. This is so that
    we don't end up removing useful data or directives that are not meant to be
    removed.

    Parameters
    ----------
    nb : nbformat.NotebookNode
        The notebook object to be stripped.

    Returns
    -------
    List[nbformat.NotebookNode]
        A list of cells that are not meant to be stripped.
    """
    return [
        cell
        for cell in nb.cells
        if "jupyterlite_sphinx_strip" not in cell.metadata.get("tags", [])
    ]


def _apply_notebook_modification_function(
    nb: nbformat.NotebookNode | os.PathLike, function: Callable
) -> None:
    """Apply a notebook modification function to a notebook.

    Parameters
    ----------
    nb : nbformat.NotebookNode
        The notebook to modify, can also be a path to the notebook file
    function : callable
        The function to apply to the notebook

    Returns
    -------
    None
        Modifies the notebook in place
    """
    if not callable(function):
        msg = f"{function} is not a callable object"
        raise ValueError(msg)

    try:
        function(nb)
    except Exception as e:
        from sphinx.util import logging

        logger = logging.getLogger("jupyterlite-sphinx")
        msg = f"Error applying notebook modification function to {nb}: {str(e)}, notebook will be left unmodified"
        logger.warning(
            msg, type="jupyterlite-sphinx", location=nb
        )  # TODO: think about this


# TODO: use this
def _get_callable(conf, name: str) -> Optional[Callable]:
    """Load a callable object from a string specification.

    Parameters
    ----------
    conf : dict
        Configuration dictionary
    name : str
        Name of the configuration option

    Returns
    -------
    callable or None
        Returns the callable object or None if not specified

    Raises
    ------
    ConfigError
        If the specified path doesn't lead to a callable object
    """
    function_path = conf.get(name)
    if not function_path:
        return None

    try:
        module_path, function_name = function_path.rsplit(".", 1)
        module = import_module(module_path)
        function = getattr(module, function_name)

        if not callable(function):
            raise ValueError(f"'{function_path}' is not a callable object")

        return function
    except (ValueError, ImportError, AttributeError) as e:
        raise ValueError(
            f"Failed to import '{function_path}' for {name}: {str(e)}"
        ) from e


# Public API functions that were taken from Sphinx-Gallery


def add_code_cell(nb: nbformat.NotebookNode, code: str):
    """Add a code cell to the notebook.

    Parameters
    ----------
    code : str
        Cell content
    """
    nb.cells.append(
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": code.splitlines(),
        }
    )


def add_markdown_cell(nb: nbformat.NotebookNode, markdown: str):
    """Add a markdown cell to the notebook.

    Parameters
    ----------
    markdown : str
        Markdown cell content.
    """
    nb.cells.append(
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": markdown,
        }
    )
