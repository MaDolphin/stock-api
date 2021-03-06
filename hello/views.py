import datetime

import simplejson
import tushare as ts
import time

from django.shortcuts import render

from django.http import HttpResponse

def hello(request):
    s = 'Hello World!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)

def getHistoryStock(request):
    id = request.GET.get('id')
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    df = ts.get_hist_data(id, start='2014-01-05', end=date)
    df = df[::-1]
    df = df.to_json(orient='index')
    return HttpResponse(simplejson.dumps(df, ensure_ascii=False))

def getRealStock(request):
    id = request.GET.get('id')
    df = ts.get_realtime_quotes(id)
    df = df.to_json(orient='index')
    return HttpResponse(simplejson.dumps(df, ensure_ascii=False))

def getTodayStock(request):
    id = request.GET.get('id')
    df = ts.get_today_ticks(id)
    df = df[::-1]
    df = df.to_json(orient='index')
    return HttpResponse(simplejson.dumps(df, ensure_ascii=False))

def getTodayDateStock(request):
    id = request.GET.get('id')
    date = request.GET.get('date')
    df = ts.get_tick_data(id,date=date)
    df = df[['time', 'price', 'volume', 'amount', 'type']]
    df = df[::-1]
    df = df.to_json(orient='index')
    return HttpResponse(simplejson.dumps(df, ensure_ascii=False))