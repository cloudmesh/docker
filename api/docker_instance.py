from cloudmesh.config.cm_config import get_mongo_db, DBConnFactory
from mongoengine import *

class Cloudmeshdocker(Document):
    dockerserver = StringField(required=True)
    meta = {'allow_inheritance': True}
    get_mongo_db("cloudmesh", DBConnFactory.TYPE_MONGOENGINE)


class Container(Document):
    containerId = StringField(required=True)
    containerImage = StringField(required=True)
    containerName = StringField(required=True)
    containerStatus = StringField(required=True)
    meta = {'allow_inheritance': True}
    get_mongo_db("cloudmesh", DBConnFactory.TYPE_MONGOENGINE)

class Images(Document):
    imageName = StringField(required=True)
    imageId = StringField(required=True)
    imageSize = StringField(required=True)
    meta = {'allow_inheritance': True}
    get_mongo_db("cloudmesh", DBConnFactory.TYPE_MONGOENGINE)
