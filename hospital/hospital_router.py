from rest_framework.routers import SimpleRouter
from hospital.views import HospitalOperations

router = SimpleRouter()

router.register('hospital', HospitalOperations)
urlpatterns = router.urls
