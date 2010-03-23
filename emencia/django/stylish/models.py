"""Models for emencia.django.stylish"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class MarkupStyle(models.Model):
    MARKUP_CHOICES = (('a', 'A'),
                      ('p', 'P'),
                      ('em', 'EM'),
                      ('img', 'IMG'),
                      ('h1', 'H1'),
                      ('h2', 'H2'),
                      ('h3', 'H3'),)

                      
    markup = models.CharField(_('markup'), max_length=10,
                              choices=MARKUP_CHOICES)
    style = models.TextField(_('style'), blank=True,
                             help_text=_('key1: value1; key2: value2;'))

    def __unicode__(self):
        return '<%s style="%s">' % (self.markup, self.style)

    class Meta:
        verbose_name = _('markup style')
        verbose_name_plural = _('markup styles')

class StyleCollection(models.Model):
    """Collection of styles to apply"""
    name = models.CharField(_('name'), max_length=255)

    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    styles = models.ManyToManyField(MarkupStyle, verbose_name=_('styles'),
                                    blank=True, null=True)

    def __unicode__(self):
        return 'Collection %s (%i styles)' % (self.name, self.styles.count())

    class Meta:
        verbose_name = _('style collection')
        verbose_name_plural = _('style collections')
