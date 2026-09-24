#!/usr/bin/env bash
set -euo pipefail

REPO_NAME="fractional-d-stability-networks"
VISIBILITY="--public"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required for automatic repository creation."
  echo "Alternatively create an empty public repository named ${REPO_NAME} on GitHub and push this directory."
  exit 1
fi

gh auth status
gh repo create "$REPO_NAME" "$VISIBILITY" --source=. --remote=origin --push
