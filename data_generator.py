import random


first_name = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Ava', 'Elijah', 'Charlotte', 'William', 'Sophia', 'James', 'Amelia', 'Benjamin', 'Isabella', 'Lucas', 'Mia', 'Henry', 'Evelyn', 'Alexander', 'Harper']

last_name = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin']

street_name = ['Main Street', 'Oak Avenue', 'Pine Road', 'Maple Drive', 'Cedar Lane', 'Elm Street', 'Washington Boulevard', 'Lakeview Drive', 'Park Place', 'Hilltop Court', 'Sunset Lane', 'Willow Way', 'River Road', 'Ridge Avenue', 'Meadow Lane', 'Broadway', 'Cherry Street', 'Highland Drive', 'Forest Avenue', 'Hickory Road']

cities = ['Springfield', 'Franklin', 'Clinton', 'Greenville', 'Salem', 'Fairview', 'Madison', 'Georgetown', 'Arlington', 'Washington', 'Ashland', 'Burlington', 'Manchester', 'Winchester', 'Milton', 'Newport', 'Cleveland', 'Centerville', 'Oakland', 'Riverdale']

states = ['CA', 'TX', 'NY', 'FL', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI', 'NJ', 'VA', 'WA', 'AZ', 'MA', 'TN', 'IN', 'MD', 'MO', 'WI']


for num in range(100):
	
	first = random.choice(first_name)
	last = random.choice(last_name)

	phone = f'{random.randint(100,999)}-555-{random.randint(1000,9999)}'

	street_num = random.randint(100,999)

	street = random.choice(street_name)

	city = random.choice(cities)

	state = random.choice(states)

	zip_code = random.randint(10000, 99999)

	address = f'{street_num} {street} St., {city} {state} {zip_code}'

	email = first.lower() + last.lower() + '@irockmail.com'

	#print(f'{first} {last}\n{phone}\n{address}\n{email}\n')
	#print(f'{first},{last},{email}')

