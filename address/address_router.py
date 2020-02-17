from rest_framework.routers import SimpleRouter
from address.views import *

router = SimpleRouter()

router.register('address', AddressOperations)
urlpatterns = router.urls
