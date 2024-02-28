def deep_merge_dict(dict1, dict2):
    """深度合并字典"""
    result = dict1.copy()

    for key, value in dict2.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = deep_merge_dict(result[key], value)
        else:
            result[key] = value

    return result