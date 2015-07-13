from django.shortcuts import render_to_response
from NPC_Gen.models import NPC

# Create your views here.
def index(request):
    return render_to_response("NPC_Gen/index.html")

#TODO: View that shows list of NPCs
def list(request):
    context = NPC.objects.all()
    return render_to_response("NPC_Gen/list.html", context)

#TODO: View that shows a single NPC
def single(request, NPC_id=1):
    context = NPC.objects.get(pk=NPC_id)
    return render_to_response("NPC_Gen/single.html", context)