from pathlib import Path

import pytest

from ducktools.pep723parser import EmbeddedMetadata
import compliance_data


def parse_data(path, parse_type):
    path = Path(path)
    if parse_type == "string":
        return EmbeddedMetadata.from_string(path.read_text())
    elif parse_type == "path":
        return EmbeddedMetadata.from_path(path)


@pytest.mark.parametrize("parser_type", ["string", "path"])
@pytest.mark.parametrize("module_name", dir(compliance_data))
def test_compliance(parser_type, module_name):
    module = getattr(compliance_data, module_name)
    try:
        metadata = parse_data(module.__file__, parser_type)
    except Exception as e:
        assert module.is_error
        assert type(e) is type(module.exact_error) and e.args == module.exact_error.args
    else:
        assert metadata.blocks == module.output
