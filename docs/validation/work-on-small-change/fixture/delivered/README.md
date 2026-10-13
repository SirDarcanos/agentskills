# Markdown filename filter

`is_markdown(name)` recognizes the final `.md` suffix regardless of extension case.
`markdown_files(names)` returns matching names unchanged, in their original
order, including duplicates. Inputs are strings; this module does not inspect
the filesystem or file contents.

Run the existing checks from this directory:

```sh
python3 -B -m unittest -v
```
