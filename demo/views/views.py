# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import time

# Create your views here.