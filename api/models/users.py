from api.models.base import Base
from api.mixins.int_id_pk import IntIdPkMixin
from api.mixins.dates import CreatedAtMixin, UpdateAtMixin

# from api.utils.password import hash_password


# Fields: 'gender', 'first_name', 'last_name', 'title', 'email', 'username', 'password', 'age', 'phone',

class User(IntIdPkMixin, CreatedAtMixin, UpdateAtMixin, Base):
    ...
    
# Fields: 'city', 'state', 'country', 'timezone', 'postcode', 'street_name', 'street_number'

class Location(IntIdPkMixin, CreatedAtMixin, UpdateAtMixin, Base):
    ...

