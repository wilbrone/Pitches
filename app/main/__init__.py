from flask import BluePrint

main = BluePrint('main',__name__)
from . import views
