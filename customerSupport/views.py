from django.views.generic import TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from .forms import SupportRequestForm
from django.contrib.auth.decorators import login_required
from .models import SupportRequest


@login_required
def SupportPageView(request):
    openRequestFound = False
    closedRequestFound = False
    openRequests = []
    closedRequests = []
    requests = SupportRequest.objects.filter(
        user=request.user)
    if len(requests) > 0:
        for supportRequest in requests:
            if supportRequest.req_status == "resolved" or supportRequest.req_status == "closed_not_resolved":
                closedRequests.append(supportRequest)
                closedRequestFound = True
            else:
                openRequests.append(supportRequest)
                openRequestFound = True

    print(openRequestFound,
          closedRequestFound,
          openRequests,
          closedRequests)
    return render(request, "supportPage.html", {"OpenRequests": openRequests, "OpenRequestFound": openRequestFound, "ClosedRequests": closedRequests, "ClosedRequestFound": closedRequestFound})


@login_required
def SubmitSupportRequest(request):
    context = {}
    context['form'] = SupportRequestForm()
    if request.method == 'POST':
        print("##########################", request.user)
        form = SupportRequestForm(request.POST)
        if form.is_valid():
            print("Vaild")
            print(request.POST)
            newRequest = SupportRequest.objects.create(user=request.user)
            newRequest.req_subject = request.POST["req_subject"]
            newRequest.req_category = request.POST["req_category"]
            newRequest.req_description = request.POST["req_description"]
            newRequest.save()
            print(newRequest)
            return redirect(SupportPageView)
    return render(request, 'submitRequest.html', context)

@login_required
def ViewSupportRequest(request,request_id):
    item = SupportRequest.objects.get(id=request_id)
    return render(request, 'viewRequest.html', {"Request":item})
