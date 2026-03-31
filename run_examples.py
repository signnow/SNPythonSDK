#!/usr/bin/env python3
"""
Script to automatically run all example files in the examples directory.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple


def find_example_files(examples_dir: Path) -> List[Path]:
    """Find all example Python files."""
    example_files = []
    for file in examples_dir.glob("*_example.py"):
        if file.is_file() and file.name != "__init__.py":
            example_files.append(file)
    return sorted(example_files)


def run_example(example_file: Path) -> Tuple[bool, str]:
    """
    Run a single example file.
    Returns (success: bool, output: str)
    """
    try:
        # Run the example as a subprocess from project root so signnow and examples.preset_data are importable
        project_root = Path(__file__).parent
        env = os.environ.copy()
        env["PYTHONPATH"] = str(project_root) + os.pathsep + str(example_file.parent)
        result = subprocess.run(
            [sys.executable, str(example_file)],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minutes timeout per example
            cwd=str(project_root),
            env=env,
        )

        output = result.stdout + result.stderr
        success = result.returncode == 0

        return success, output
    except subprocess.TimeoutExpired:
        return False, "Example execution timed out after 5 minutes"
    except Exception as e:
        return False, f"Error running example: {str(e)}"


def resolve_single_example(examples_dir: Path, name: str) -> Path:
    """Resolve example name (with or without .py) to file path."""
    name = name.strip()
    if not name.endswith(".py"):
        name = name + ".py"
    path = examples_dir / name
    if path.is_file():
        return path
    # Try without _example suffix if user passed e.g. auth_check
    if not name.endswith("_example.py"):
        path = examples_dir / (name.replace(".py", "") + "_example.py")
        if path.is_file():
            return path
    return None


def main():
    """Main function to run all examples or a single one if name is passed."""
    examples_dir = Path(__file__).parent / "examples"

    if not examples_dir.exists():
        print(f"Error: Examples directory not found: {examples_dir}")
        sys.exit(1)

    # Single example: run_examples.py auth_check_example.py  OR  run_examples.py auth_check_example
    if len(sys.argv) >= 2:
        example_name = sys.argv[1]
        example_file = resolve_single_example(examples_dir, example_name)
        if not example_file:
            print(f"Error: Example not found: {example_name}")
            sys.exit(1)
        print(f"Running: {example_file.stem}")
        print("-" * 70)
        success, output = run_example(example_file)
        print(output)
        sys.exit(0 if success else 1)

    example_files = find_example_files(examples_dir)

    if not example_files:
        print("No example files found.")
        sys.exit(0)

    print("=" * 70)
    print(f"Running {len(example_files)} example(s)...")
    print("=" * 70)
    print()

    results = []
    for example_file in example_files:
        example_name = example_file.stem
        print(f"[{len(results) + 1}/{len(example_files)}] Running: {example_name}")
        print("-" * 70)

        success, output = run_example(example_file)
        results.append((example_name, success, output))

        if success:
            print(f"✓ {example_name} - SUCCESS")
            if output.strip():
                # Print last few lines of output if available
                lines = output.strip().split("\n")
                if len(lines) > 0:
                    print(f"  Output: {lines[-1][:100]}")
        else:
            print(f"✗ {example_name} - FAILED")
            if output.strip():
                # Print error output
                error_lines = output.strip().split("\n")
                for line in error_lines[-5:]:  # Last 5 lines
                    if line.strip():
                        print(f"  {line[:100]}")

        print()

    # Summary
    print("=" * 70)
    print("Summary:")
    print("=" * 70)

    successful = sum(1 for _, success, _ in results if success)
    failed = len(results) - successful

    for name, success, _ in results:
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"  {status}: {name}")

    print()
    print(f"Total: {len(results)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print("=" * 70)

    # Exit with error code if any examples failed
    if failed > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
