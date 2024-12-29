"""Import Test."""

# Import future modules

# Import built-in modules
from __future__ import annotations

import importlib
import pkgutil

# Import local modules
import photoshop


def test_imports():
    """Test import modules."""
    prefix = f"{photoshop.__name__}."
    iter_packages = pkgutil.walk_packages(
        photoshop.__path__,
        prefix,
    )
    for _, name, _ in iter_packages:
        module_name = name if name.startswith(prefix) else prefix + name
        importlib.import_module(module_name)
