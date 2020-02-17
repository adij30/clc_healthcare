from rest_framework.routers import SimpleRouter
from patient.views import PatientOperations

router = SimpleRouter()

router.register('patient', PatientOperations)
urlpatterns = router.urls
