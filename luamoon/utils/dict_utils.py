def deep_update(d1, d2):
    for k, v in d2.items():
        if isinstance(v, dict) and isinstance(d1.get(k), dict):
            deep_update(d1[k], d2[k])
        else:
            d1[k] = d2[k]
