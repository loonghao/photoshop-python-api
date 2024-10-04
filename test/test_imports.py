"""Import Test."""
# Import future modules
# Import built-in modules
import importlib
import pkgutil

import photoshop
# Import local modules


def test_imports():
    """Test import modules."""
    prefix = f"{photoshop.__name__}."
    iter_packages = pkgutil.walk_packages(
        photoshop.__path__,  # noqa: WPS609
        prefix,
    )
    for _, name, _ in iter_packages:
        module_name = name if name.startswith(prefix) else prefix + name
        importlib.import_module(module_name)
