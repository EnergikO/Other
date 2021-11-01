def add_items(_dict: dict, *args) -> None:
	for arg in args:
		try:
			_dict[arg]

		except KeyError:
			_dict[arg] = None


def delete_items(_dict: dict, *keys) -> dict:
	new_dict = dict()

	for key in _dict.keys():
		if key in keys:
			continue

		new_dict[key] = _dict[key]

	return new_dict


def sort_by_keys(_dict: dict, reverse=False) -> list:
	return sorted(list(_dict.items()), key=lambda x: x[0], reverse=reverse)


def sort_by_values(_dict: dict, reverse=False) -> list:
	return sorted(list(_dict.items()), key=lambda x: x[1], reverse=reverse)


def fill_dict_randomly(n, _range):
	from random import randint

	_dict = dict()
	for i in range(n):
		_dict[i] = randint(*_range)

	return _dict


def print_dict(_dict: dict):
	for elem in _dict:
		try:
			print(elem.__repr__())

		except AttributeError:
			print(elem)

