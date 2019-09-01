from city import City
from zoo import Zoo


vienna = City("vienna")

assert vienna.zoo
assert isinstance(vienna.zoo, Zoo)
assert vienna.zoo.size == 130
assert vienna.zoo._owner_name == "Mrs Zoo Keeper"

print(
    f"City: {vienna.name}\n"
    f"Zoo owner: {vienna.zoo._owner_name}\n"
    f"Zoo's size: {vienna.zoo.size}\n"
    f"Zoo's animals: {', '.join([animal.name for animal in vienna.zoo.animals])}"
)
