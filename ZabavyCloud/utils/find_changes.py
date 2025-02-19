"""
Find changes utilities.
"""


def find_changes(old_data: dict, new_data: dict) -> list:
    """
    ? Finds the changes between two dictionaries.
    params:
        ! old_data: dict
            The old data saved on database.
        ! new_data: dict
            The new data to compare.
    """
    def add_changes(field: str, old_data: any, new_data: any):
        """
        ? Adds the fields and data to the changes list.
        params:
            ! field: str
                The field name.
            ! old_data: any
                The old data of field.
            ! new_data: any
                The new data of field.
        """
        changes.append({
            'field': field,
            'old_data': old_data,
            'new_data': new_data
        })
    changes: list = []
    old_keys: list = list(old_data.keys())
    new_keys: list = list(new_data.keys())
    for field in new_keys:
        if field in old_data:
            if new_data[field] is not None and new_data[field] != old_data[field]:
                add_changes(
                    field=field, old_data=old_data[field], new_data=new_data[field])
        else:
            add_changes(field=field, old_data=None, new_data=new_data[field])
    return changes
