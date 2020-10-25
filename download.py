from db_models.mongo_setup import global_init
from db_models.models.cache_model import Cache
global_init()
db_key="5f95812daf87666477c97cf7"
db_object = Cache.objects.get(pk=db_key)
file_name = db_object.file_name

with open(file_name, 'wb') as file_to_save:
    file_to_save.write(db_object.file.read())