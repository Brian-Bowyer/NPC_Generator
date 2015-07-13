from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'NPC_Gen.views.index'),
    url(r'^list$', "NPC_Gen.views.list"),
    url(r'^single$', "NPC_Gen.views.list"),
]
