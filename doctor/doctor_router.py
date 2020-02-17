from rest_framework.routers import SimpleRouter
from doctor.views import DoctorOperations

router = SimpleRouter()

router.register('doctor', DoctorOperations)
urlpatterns = router.urls
