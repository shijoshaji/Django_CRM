from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent, User
from .forms import LeadModelForm
import logging

# Get an instance of a logger
logger = logging.getLogger('django')

# Create your views here.
LEAD_URL = "leads/"


def lead_list(request):
    template = f"{LEAD_URL}leads_list.html"
    list_of_leads = Lead.objects.all()
    context = {
        "leads": list_of_leads
    }
    return render(request, template, context)


def lead_detail(request, pk):
    lead_data = Lead.objects.get(id=pk)
    context = {
        "lead": lead_data
    }
    template = f"{LEAD_URL}leads_detail.html"
    return render(request, template, context)


def _create(information):
    logger.info(f" inside _create {information}")
    Lead.objects.create(
        first_name=information['first_name'],
        last_name=information['last_name'],
        age=information['age'],
        agent=information['agent'],
    )


def lead_create(request):
    template = f"{LEAD_URL}leads_create.html"
    form = LeadModelForm()
    if request.method == "POST":
        logger.info(f'Retriving data from forms')
        data = request.POST
        logger.info(f'{data}')
        form = LeadModelForm(data)
        if form.is_valid():
            logger.info(f'cleaner {form.cleaned_data}')
            # _create(form.cleaned_data) NOTE: we can use form.save() isntead on this
            form.save()
            logger.info(f'Lead is created')
            return redirect("/leads")

    context = {
        "form": form
    }
    return render(request, template, context)
