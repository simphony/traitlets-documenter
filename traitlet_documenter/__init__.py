from __future__ import absolute_import

__all__ = ['__version__', 'setup']

try:  # pragma: no cover
    from traitlet_documenter._version import full_version as __version__
except ImportError:  # pragma: no cover
    __version__ = "not-built"


def setup(app):
    """ Add the TraitletDocumenter in the current sphinx autodoc instance.

    """
    from traitlet_documenter.class_traitlet_documenter import (
        ClassTraitletDocumenter)

    app.add_autodocumenter(ClassTraitletDocumenter)
