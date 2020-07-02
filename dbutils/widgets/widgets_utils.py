from typing import Dict

widgets_map: Dict[str, str] = dict()


def combobox(name: str, defaultValue: str, choices: list, label: str) -> None:
    """
    Creates a combobox input widget with a given name, default value and choices
    """
    widgets_map[name] = defaultValue


def dropdown(name: str, defaultValue: str, choices: list, label: str) -> None:
    """
    Creates a dropdown input widget a with given name, default value and choices
    """
    widgets_map[name] = defaultValue


def get(name: str) -> str:
    """
    Retrieves current value of an input widget
    """
    return widgets_map[name]


def getArgument(name: str, optional: str) -> str:
    """
    (DEPRECATED) Equivalent to get
    """
    return widgets_map[name]


def multiselect(name: str, defaultValue: str, choices: list, label: str) -> None:
    """
    Creates a multiselect input widget with a given name, default value and choices
    """
    widgets_map[name] = defaultValue


def remove(name: str) -> None:
    """
    Removes an input widget from the notebook
    """
    del widgets_map[name]


def removeAll() -> None:
    """
    Removes all widgets in the notebook
    """
    widgets_map.clear()


def text(name: str, defaultValue: str, label: str) -> None:
    """
    Creates a text input widget with a given name and default value
    """
    widgets_map[name] = defaultValue
