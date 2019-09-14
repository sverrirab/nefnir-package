======
nefnir
======

This is a package wrapping https://github.com/jonfd/nefnir 

All credits to the author of that excellent project. 

.. image:: https://img.shields.io/pypi/v/nefnir.svg
        :target: https://pypi.python.org/pypi/nefnir

.. image:: https://img.shields.io/travis/sverrirab/nefnir.svg
        :target: https://travis-ci.org/sverrirab/nefnir

.. image:: https://readthedocs.org/projects/nefnir/badge/?version=latest
        :target: https://nefnir.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




A lemmatizer for Icelandic text See e.g _IceNLP_bridge for help creating tokenized and tagged text.


* Free software: Apache Software License 2.0
* Documentation: https://nefnir.readthedocs.io.


Features
--------

* See Nefnir_ for full description.
* Simple lemmatizer for Icelandic.

Example
-------

    import nefnir
    
    nefnir.lemmatize('Hvað', 'fshen')

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Nefnir: https://github.com/jonfd/nefnir
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
