# JupyterLite directive

`jupyterlite-sphinx` provides a `jupyterlite` directive that allows you to embed JupyterLab in your docs.

```rst
.. jupyterlite::
   :width: 100%
   :height: 600px
   :prompt: Try JupyterLite!
   :prompt_color: #00aa42
```

```{eval-rst}
.. jupyterlite::
   :width: 100%
   :height: 600px
   :prompt: Try JupyterLite!
   :prompt_color: #00aa42
```

You can also pass a Notebook file to open automatically:

```rst
.. jupyterlite:: my_notebook.ipynb
   :width: 100%
   :height: 600px
   :prompt: Try JupyterLite!
   :prompt_color: #00aa42
```

```{eval-rst}
.. jupyterlite:: my_notebook.ipynb
   :width: 100%
   :height: 600px
   :prompt: Try JupyterLite!
   :prompt_color: #00aa42
```

## Opening the notebook in a new tab

If you use the `:new_tab:` option in the directive, the Notebook will be opened in a new browser tab.

```rst
.. jupyterlite:: my_notebook.ipynb
   :new_tab: True
```

```{eval-rst}
.. jupyterlite:: my_notebook.ipynb
   :new_tab: True
```

## Standalone mode

If you use the `:standalone:` option in the directive, the Notebook will be opened in standalone
mode without the JupyterLite UI and the rest of the elements of the page. This option is compatible
with the `:new_tab:` option noted above.

Without `:new_tab:`, and `:standalone:` enabled:

```rst
.. jupyterlite:: my_notebook.ipynb
   :standalone: True
```

```{eval-rst}
.. jupyterlite:: my_notebook.ipynb
   :standalone: True
```

With `:new_tab:`, and `:standalone:` enabled:

```rst
.. jupyterlite:: my_notebook.ipynb
   :new_tab: True
   :standalone: True
```

```{eval-rst}
.. jupyterlite:: my_notebook.ipynb
   :new_tab: True
   :standalone: True
```

The standalone mode can also be set to `False` if the global configuration is set to `True`.

## Search parameters

The directive `search_params` allows to transfer some search parameters from the documentation URL to the Jupyterlite URL.\
Jupyterlite will then be able to fetch these parameters from its own URL.\
For example `:search_params: ["param1", "param2"]` will transfer the parameters *param1* and *param2*.
Use a boolean value to transfer all or none of the parameters (default to none): `:search_params: True`
