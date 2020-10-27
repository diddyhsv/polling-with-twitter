import re
citiesstring = "Florence (37778 people) | Myrtle Beach (32795 people) | Conway (23714 people) | Socastee (19952 people) | North Myrtle Beach (16310 people) | Red Hill (13223 people) | Garden City (9209 people) | Little River (8960 people) | Georgetown (8860 people) | Bennettsville (8038 people) | Hartsville (7626 people) | Murrells Inlet (7547 people) | Marion (6472 people) | Dillon (6444 people) | Darlington (5999 people) | Cheraw (5639 people) | Forestbrook (4612 people) | Surfside Beach (4422 people) | Mullins (4387 people) | North Hartsville (3251 people) | Andrews (2876 people) | Pageland (2683 people) | Loris (2680 people) | Timmonsville (2388 people) | McColl (2033 people) | Johnsonville (1492 people) | Chesterfield (1429 people) | Latta (1306 people) | Pamplico (1231 people) | "
result = re.sub(r"((\w+ )+)\(\d+ people\) \| ", r' or "\1" in tw["user"]["location"].lower() ', citiesstring)
result2 = re.sub(r'(\w\w\w) "', r'\1"', result)

print(result2.lower())