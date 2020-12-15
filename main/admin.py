from django.contrib import admin

# Register your models here.
from .models import GrpStatDown, TechType, WorkArea, TechRole, Vinechikle, StateDown, DownTimeJornal, UpTimeJornal

admin.site.register(GrpStatDown)
admin.site.register(TechType)
admin.site.register(WorkArea)
admin.site.register(TechRole)
admin.site.register(Vinechikle)
admin.site.register(StateDown)
admin.site.register(DownTimeJornal)
admin.site.register(UpTimeJornal)

