def get_root_property(d, value):
    def find_property(d, value, current_path):
        for key, value in d.items():
            if isinstance(value, list) and value in value:
                return current_path
            elif isinstance(value, dict):
                result = find_property(value, value, current_path + [key])
                if result:
                    return result
        return None

    result = find_property(d, value, [])
    return result[0] if result else None