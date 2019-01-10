# update, Deleted
# Attomic => id
import mlab
from models.character import Charater

mlab.connect()

Character = Charater.objects().with_id("5c34acfc0b58220448dc96bd")
print(Character)
print(Character.to_mongo())

# 1. Update
# 1.1 read document
#1.2 update document

# Character.update(set__rate=2,set__name="super man") # set__inc__
# Character.reload()
# print(Character.rate)


#2 delete
#2.1 read document
#2.2 delete document
Character.delete()