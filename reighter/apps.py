from django.apps import AppConfig
from keras.models import load_model
from django.conf import settings
import pickle
import os



class ReighterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reighter'
        # loading model
    model_path = os.path.join(settings.MODELS, 'digitdemo1.h5')
    digitmodel = load_model(model_path)

