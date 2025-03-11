import nbformat


from typing import List


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
