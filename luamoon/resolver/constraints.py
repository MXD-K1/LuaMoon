import re
import operator

OPS_MAP = {
    '==': operator.eq,
    '>=': operator.ge,
    '<=': operator.le,
    '>': operator.gt,
    '<': operator.lt
}

PATTERN = re.compile(
    r'([A-Za-z_][A-Za-z0-9_-]*)' +              # package name
    rf'({"|".join(re.escape(op) for op in OPS_MAP.keys())})' +  # operator
    r'(\d+(?:\.\d+)*)$'                           # version (no trailing dot)
)

def parse_constraint(constraint_str) -> dict[str , str]:
    if _is_valid_constraint(constraint_str):
        match_ = re.match(PATTERN, constraint_str)
        return {
            'package_name': match_.group(1),
            'operator': match_.group(2),
            'version': match_.group(3)
        }
    else:
        # todo: raise an error
        return {}

def matches(version, constraint):
    _, op, c_ver = parse_constraint(constraint).values()
    norm_version = tuple(normalize_version(version).split('.'))
    norm_c_ver = tuple(normalize_version(c_ver).split('.'))
    return OPS_MAP[op](norm_version, norm_c_ver)

def _is_valid_constraint(constraint_str):
    match_ = re.match(PATTERN, constraint_str)
    return match_ is not None

def normalize_version(version):
    parts = version.split('.')

    for i, part in enumerate(parts):
        parts[i] = str(int(part))  # remove leading zeros

    if len(parts) > 3:
        return '.'.join(parts[:3])
    elif len(parts) == 3:
        return '.'.join(parts)
    else:
        parts.extend(['0'] * (3 - len(parts)))
        return '.'.join(parts)

__all__ = ['parse_constraint', 'matches', 'normalize_version', 'OPS_MAP']
