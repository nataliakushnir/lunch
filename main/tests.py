from django_seed import Seed
from main.models import Category

test_string = "test_string"
seeder = Seed.seeder()
seeder.add_entity(Category, 5, dict(title=lambda x: test_string))
seeder.execute()
