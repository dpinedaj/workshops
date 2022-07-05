from faker import Faker
import pandas as pd


def fake_dataframe(size: int) -> pd.DataFrame:
    faker = Faker()
    return pd.DataFrame(
        [{'lat': faker.coordinate(center=74.0, radius=0.10),
          'lon': faker.coordinate(center=40.8, radius=0.10),
          'text': faker.sentence(),
          'name': faker.name(),
          'address': faker.address(),
          'job': faker.job(),
          "email": faker.email(),
          } for _ in range(size)]
    )
