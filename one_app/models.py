from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100, default='panel-primary')

    def __unicode__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=100)
    groups = models.ForeignKey(Group, related_name='properties')

    def __unicode__(self):
        return self.name


class StatisticManager(models.Manager):
    def create_statistic(self, property):
        statistic = self.create(property=property)
        return statistic

    def create_child_statistic(self, property, parent):
        statistic = self.create(property=property, parent = parent)
        return statistic

    def get_or_create_statistic(self, property):
        stats = Statistic.objects.filter(parent__isnull=True, property=property)
        if stats.__len__() == 1:
            stat = stats.first()
        elif stats.__len__() > 1:
            raise
        else:
            stat = Statistic.objects.create_statistic(property)
        return stat

    def get_statistic_by_property(self,property):
        return Statistic.objects.filter(parent__isnull=True, property=property).first()

    def get_statistic_by_property_with_parent(self,property, parent):
        return Statistic.objects.filter(parent=parent, property=property).first()


class Statistic(models.Model):
    property = models.ForeignKey(Property, related_name='statistics')
    trueCount = models.IntegerField(default=0)
    falseCount = models.IntegerField(default=0)
    parent = models.ForeignKey('self', related_name='statistics', blank=True, null=True)

    objects = StatisticManager()

    def __unicode__(self):
        return u"Statistic {name} id {id}".format(name=self.property.name, id=self.pk)