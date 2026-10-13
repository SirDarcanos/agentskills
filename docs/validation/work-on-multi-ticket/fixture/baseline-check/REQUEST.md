# Approved name-report feature

Parent 100 coordinates work 101 and 102; parent is not an implementation unit.
101 owns names.py, test_names.py and normalization documentation. N1:
normalize_name(string) strips surrounding whitespace and lowercases; empty stays
empty. 102 owns report.py, test_report.py and report documentation; blocked by 101.
R1: render_names(strings) joins normalized names with comma-space, preserving
order, duplicates and empty values; empty sequence yields empty string.
P1: protected staged/unstaged/untracked/mode/symlink work remains unchanged.
G1: closed/ready prerequisite is insufficient; current accepted integration and
checks/review unlock the dependent. E1: retain failed/stale evidence and repair
budget through checkpoint resume; refresh affected checks and both review axes.
Exclude input coercion, locale/Unicode normalization, production tracker fixtures,
parallel writers, deployment and releases. Python standard library checks:
python3 -B -m unittest -v. Strings are the supported input domain.
