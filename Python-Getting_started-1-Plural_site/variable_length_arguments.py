def test_var_args(name, **kwargs):
	print(name)
	print(kwargs)


test_var_args("Mark", "Loves Python", None,"Hello world", True)