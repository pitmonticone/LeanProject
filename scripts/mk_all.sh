#!/usr/bin/env bash
# Usage: mk_all.sh [directory]
#
# Examples:
#   ./scripts/mk_all.sh
#   ./scripts/mk_all.sh data/real
#   ./scripts/mk_all.sh ../archive
#
# Description:
# This script generates a Project.lean file that imports all Lean files
# within the specified directory (default is the current directory). It ensures
# that all Lean files are included in the generated file, excluding Project.lean
# itself.
#
# The script processes the filenames to:
# - Remove an initial `./` if present.
# - Replace an initial `../<dir>/` (e.g., `../test/`) with `Project.`.
# - Convert all directory separators (`/`) to Lean module separators (`.`).
# - Remove the `.lean` suffix.
# - Prepend `import Project.` to each line to create a valid Lean import statement.
#
# The processed import statements are then sorted and written to Project.lean.

# Navigate to the Project directory relative to the script's location
cd "$(dirname "${BASH_SOURCE[0]}")"/../Project

# Determine the target directory
if [[ $# -eq 1 ]]; then
  dir="${1%/}"  # Remove trailing slash if present
else
  dir="."  # Default to the current directory
fi

# Find all .lean files in the target directory, excluding Project.lean
# Process the filenames as described in the script header and sort them
find "$dir" -name \*.lean -not -name Project.lean \
  | sed 's,^\./,,;s,^\.\./[^/]*,,;s,/,.,g;s,\.lean$,,;s,^,import Project.,' \
  | sort >"$dir"/../Project.lean