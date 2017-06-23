# pyblish-nukestudio

This page will walk you through integrating Pyblish with Foundry NukeStudio.

## Prerequisities

Make sure you have installed Pyblish before continuing.

- See [Installing Pyblish](https://github.com/pyblish/pyblish/wiki/Installation)

## Introduction

With this integration you can publish from two places in NukeStudio;

- Menu-item called *"Publish"*, located directly under the right-click menu on the timeline.
- Submission called *"Pyblish"*, located in the export dialog in the dropdown menu *"Render with:"*.

This will display a Pyblish graphical user interface.

## Installation

Ensure Pyblish for NukeStudio is on your `PYTHONPATH` and run this within NukeStudio.

```python
import pyblish_nukestudio
pyblish_nukestudio.setup()
```

You can then show the Pyblish graphical user interface by calling `show()`.

```python
pyblish_nukestudio.show()
```

## Persistence

It is recommended that you allow Pyblish to load upon launching NukeStudio.
For this to work, add the `pyblish_nukestudio/hiero_plugin_path` directory to your `HIERO_PLUGIN_PATH`

(2) You can find your `pythonpath` directory here:

```bash
pyblish-nukestudio/pyblish_nukestudio/hiero_plugin_path
```

As you will find, this directory contains sub-directories leading to two python files; `pyblish_startup.py` and `selection_tracker.py`.

**pyblish_startup.py**

This sets up Pyblish similar to `pyblish_nukestudio.setup()`

**selection_tracker.py**

This ensures that you can access the active selection outside of NukeStudio, via `nukestudio.selection` which is added to the ```nukestudio``` module by this tracker. This is also injected into the context, so you can easily access the active selection with `context.data('selection')`

## Plugins

This integration comes with some built-in plugins that provide basic data collection from NukeStudio. Apart of the usual host information; ```context.data["currentFile"]```, ```context.data["hostVersion"]``` and ```context.data["host"]```, you are also provided with:

### ```context.data["selection"]```

This is the current selection on the timeline.

### ```context.data["activeProject"]```

This is the project being published from.

### ```context.data["submission"]```

This is the submission object from the export dialog. This is TaskGroup which you can read more about here;

https://www.thefoundry.co.uk/products/hiero/developers/10.5/hieropythondevguide/export.html
https://www.thefoundry.co.uk/products/hiero/developers/10.5/hieropythondevguide/api/api_core.html#hiero.core.TaskGroup
