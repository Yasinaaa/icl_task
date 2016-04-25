#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from client.form import *
from StringIO import StringIO
from django.http import HttpResponse
from icl_task import settings
import os
from django.shortcuts import render_to_response
import StringIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from django.views.generic import *

class MyModel(FormView):
    template_name = 'main_page.html'
    form_class = ClientFileForm
    model = ClientFileModel

    def get_context_data(self, **kwargs):
        all_graphs = ClientFileModel.objects.all()
        context = super(MyModel, self).get_context_data(**kwargs)
        context["all_graphs"] = all_graphs
        context['graph'] = 'e'
        return context

    def form_valid(self, form):
         task = form.save()
         return task

    def post(self, request, *args, **kwargs):
        xlabel = u'X'
        ylabel = u'Y'
        print 'j'

        form = self.form_class(request.POST,request.FILES)

        all_graphs = ClientFileModel.objects.all()

        if form.is_valid():
            task =  self.form_valid(form)

            fig = Figure(facecolor = 'white', edgecolor = 'white')
            graph = fig.add_subplot(111)

            title = task.title
            graph.set_title(title)
            graph.set_xlabel(xlabel)
            graph.set_ylabel(ylabel)

            graph.grid()
            var_x, var_y = read_xls_file(task.path_to_file.path)

            xs = np.array(var_x)
            series1 = np.array(var_y)
            s1mask = np.isfinite(series1)

            graph.plot(xs[s1mask], series1[s1mask], linestyle='-', marker='o')

            output = StringIO.StringIO()
            canvas = FigureCanvas(fig)

            canvas.print_png(output)
            all_path = '/home/yasina/PycharmProjects/icl_task/static_files/media/graphs/%s.png' % (task.title)
            print all_path
            fig.savefig(all_path);

            path = '%s/all_graphs.json' % (settings.MEDIA_ROOT)

            with open(path, 'w') as f:
                results = [ob.json() for ob in all_graphs]
                json_str = json.dumps(results)
                f.write(json_str)

            context = self.get_context_data()
            context['graph'] = 'media/graphs/%s.png' % (task.title)
            context['form'] = form
            context['all_graphs'] = all_graphs
            return super(FormView, self).render_to_response(context)
        else:
            return render(request, self.template_name,{'graph': 'e',"form":form, "all_graphs": all_graphs})


def read_xls_file(excel_file_name):
    path = settings.MEDIA_ROOT
    rb = xlrd.open_workbook(excel_file_name)
    sheet = rb.sheet_by_index(0)

    var_x = []
    var_y = []
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        var_x.append(row[0])
        var_y.append(row[1])

    return (var_x,var_y)



