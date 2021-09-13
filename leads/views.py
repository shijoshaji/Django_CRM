from typing import ClassVar
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Lead, Agent, User
from .forms import LeadModelForm, CustomUserCreationForm
from django.core.mail import send_mail

import logging

# Get an instance of a logger
logger = logging.getLogger('django')

# Create your views here.
LEAD_URL = "leads/"

#  Class Based View - CBV
# NOTE: Remeber CBV as CRUD+List => CreateView,UpdateView,ListView,DeleteView,DetailView


# Signup view
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        # NOTE: on success it redirect to link we specify
        return reverse('login')


class LandingPageView(TemplateView):
    template_name = "landing.html"


class LeadListView(ListView):
    template_name = f"{LEAD_URL}leads_list.html"
    # NOTE: give this way or define a in buit function like get_queryset
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(DetailView):
    template_name = f"{LEAD_URL}leads_detail.html"
    # queryset = Lead.objects.all()
    context_object_name = "lead"

    def get_queryset(self):
        return Lead.objects.all()


class LeadCreateView(CreateView):
    template_name = f"{LEAD_URL}leads_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        # NOTE: on success it redirect to link we specify
        return reverse('leadList')

    def form_valid(self, form):
        # TODO: send email
        send_mail(
            subject="A Lead is created",
            message="Go to admin dashboard to see",
            from_email="test@test.com",
            recipient_list=["test@test.com"],
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(UpdateView):
    template_name = f"{LEAD_URL}leads_update.html"
    form_class = LeadModelForm

    def get_success_url(self):
        # NOTE: on success it redirect to link we specify
        return reverse('leadList')

    def get_queryset(self):
        return Lead.objects.all()


class LeadDeleteView(DeleteView):
    template_name = f"{LEAD_URL}leads_delete.html"

    def get_success_url(self):
        # NOTE: on success it redirect to link we specify
        return reverse('leadList')

    def get_queryset(self):
        return Lead.objects.all()


#  Function Based View - FBV
# NOTE: commenting FBV since we are using CBV


def landing_page(request):
    # template = "landing.html"
    # return render(request, template)
    pass


def lead_list(request):
    # template = f"{LEAD_URL}leads_list.html"
    # list_of_leads = Lead.objects.all()
    # context = {
    #     "leads": list_of_leads
    # }
    # return render(request, template, context)
    pass


def lead_detail(request, pk):
    # lead_data = Lead.objects.get(id=pk)
    # context = {
    #     "lead": lead_data
    # }
    # template = f"{LEAD_URL}leads_detail.html"
    # return render(request, template, context)
    pass


def _create(information):
    logger.info(f" inside _create {information}")
    Lead.objects.create(
        first_name=information['first_name'],
        last_name=information['last_name'],
        age=information['age'],
        agent=information['agent'],
    )


def lead_create(request):
    # template = f"{LEAD_URL}leads_create.html"
    # form = LeadModelForm()
    # if request.method == "POST":
    #     logger.info(f'Retriving data from forms')
    #     data = request.POST
    #     logger.info(f'{data}')
    #     form = LeadModelForm(data)
    #     if form.is_valid():
    #         logger.info(f'cleaner {form.cleaned_data}')
    #         # _create(form.cleaned_data) NOTE: we can use form.save() isntead on this
    #         form.save()
    #         logger.info(f'Lead is created')
    #         return redirect("/leads")

    # context = {
    #     "form": form
    # }
    # return render(request, template, context)
    pass


def lead_update(request, pk):
    # lead_data = Lead.objects.get(id=pk)
    # form = LeadModelForm(instance=lead_data)
    # if request.method == "POST":
    #     data = request.POST
    #     form = LeadModelForm(data, instance=lead_data)
    #     if form.is_valid():
    #         form.save()
    #         logger.info(f'Lead is Updated')
    #         return redirect("/leads")

    # context = {
    #     "lead": lead_data,
    #     "form": form,
    # }
    # template = f"{LEAD_URL}leads_update.html"
    # return render(request, template, context)
    pass


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
