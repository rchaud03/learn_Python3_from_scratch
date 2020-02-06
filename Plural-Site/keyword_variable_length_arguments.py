def test_var_args(name, **kwargs):
	print(name)
	print(kwargs["description"], kwargs["feedback"])


test_var_args("Mark", description= "Loves Python", feedback=None, plural_sight_subscriber=True)