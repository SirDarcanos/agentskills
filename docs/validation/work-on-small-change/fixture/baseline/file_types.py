"""Classify Markdown filenames without inspecting the filesystem."""


def is_markdown(name):
    return name.endswith(".md")


def markdown_files(names):
    return [name for name in names if is_markdown(name)]
