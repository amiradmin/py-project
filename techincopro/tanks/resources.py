from import_export import resources
from .models import GeneralWelding,Rt

class GeneralWeldingResource(resources.ModelResource):
    class Meta:
        model = GeneralWelding


class RtResource(resources.ModelResource):
    class Meta:
        model = Rt
