# Name report fixture

normalize_name strips surrounding whitespace and lowercases strings. Run python3 -B -m unittest -v.
render_names joins normalized strings with comma-space, preserving order,
duplicates and empty values. An empty sequence yields an empty string.
The approved feature is defined in REQUEST.md.
