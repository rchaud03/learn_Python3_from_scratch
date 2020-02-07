#creating nested dictionaries
cars = {"bmw": {"model": "550i", "year": 2016}, "benz": {"model": "550i", "year": 2015}}

#We can access a value by using the dictionary and both keys to get the value in the 2nd key
benz_year = cars["benz"]["year"]
print(benz_year)