#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf 'Usage: %s SOURCE DESTINATION\n' "$0"
}

if [[ ${1:-} == "--help" || $# -ne 2 ]]; then
  usage
  exit $(( $# == 2 ? 0 : 2 ))
fi

src=$1
dest=$2

[[ -d "$src" ]] || { printf 'Source is not a directory: %s\n' "$src" >&2; exit 1; }
[[ -n "$dest" && "$dest" != / ]] || { printf 'Destination must be a non-root path\n' >&2; exit 1; }

archive="$dest/$(basename -- "$src")-$(date +%F).tar.gz"
tar -C "$src" -czf "$archive" -- .
printf 'Backed up %s to %s\n' "$src" "$archive"
