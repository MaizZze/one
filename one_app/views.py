# Create your views here.
from django.contrib import messages
from django.db.models import F
from django.shortcuts import render_to_response
from django.template import RequestContext
from one_app.models import Group, Property, Statistic


def init(request):
    # messages.info(request, 'Test')
    # messages.error(request, 'Test')
    # messages.warning(request, 'Test')
    props = Property.objects.all()
    n = 0
    for prop in props:
        stat = Statistic.objects.create_statistic(prop)
        n += 1
        for pr in props:
            if pr != prop:
                Statistic.objects.create_child_statistic(pr, stat)
                n += 1
    context = {}
    messages.info(request, u"Asdf {n}".format(n=n))
    return render_to_response('base.html', context, context_instance=RequestContext(request))


def home(request):
    context = {}
    context['groups'] = Group.objects.all()
    return render_to_response('home.html', context, context_instance=RequestContext(request))


def test(request):
    context = {}
    listPropPk = map(lambda w: int(w[0].replace('cb', '')),
                     filter(lambda x: x[0].__contains__("cb"), request.POST.items()))

    query_parent_isnull_prop_in = Statistic.objects.filter(parent__isnull=True, property__pk__in=listPropPk)

    query_parent_isnull_prop_in.update(trueCount=F('trueCount') + 1)

    Statistic.objects.filter(parent__isnull=True).exclude(property__pk__in=listPropPk) \
        .update(falseCount=F('falseCount') + 1)

    Statistic.objects.filter(parent__in=query_parent_isnull_prop_in).filter(property__pk__in=listPropPk) \
        .update(trueCount=F('trueCount') + 1)

    Statistic.objects.filter(parent__in=query_parent_isnull_prop_in).exclude(property__pk__in=listPropPk) \
        .update(falseCount=F('falseCount') + 1)






    commonPropBall = 100.0 / Property.objects.count()
    propBall = commonPropBall / 5.0
    childPropBall = (commonPropBall - propBall) / (Property.objects.count() - 1.0)

# git://github.com/openshift/django-example.git
    result = 0.0

    false_parent_isnull = Statistic.objects.filter(parent__isnull=True, falseCount__gt=F('trueCount'))
    for stat in false_parent_isnull:
        if stat.property.pk not in listPropPk:
            result += commonPropBall

    true_parent_isnull = Statistic.objects.filter(parent__isnull=True, trueCount__gt=F('falseCount'))
    for stat in true_parent_isnull:
        if stat.property.pk in listPropPk:
            result += propBall
            true_parent_stat = Statistic.objects.filter(parent=stat, trueCount__gt=F('falseCount'))
            for childStat in true_parent_stat:
                if childStat.property.pk in listPropPk:
                    result += childPropBall

            false_parent_stat = Statistic.objects.filter(parent=stat, falseCount__gt=F('trueCount'))
            for childStat in false_parent_stat:
                if childStat.property.pk not in listPropPk:
                    result += childPropBall




    context['result'] = result
    return render_to_response('result.html', context, context_instance=RequestContext(request))