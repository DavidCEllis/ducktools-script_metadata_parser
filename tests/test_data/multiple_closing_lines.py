# /// pyproject
# [run]
# dependencies = ["requests"]
# ///
# Additional comment
# ///

import textwrap

output = {
    "pyproject": textwrap.dedent(
        """
        [run]
        dependencies = ["requests"]
        ///
        Additional comment
        """
    ).lstrip()
}

is_error = False

# Internals
exact_error = None
