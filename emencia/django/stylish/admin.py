"""Admin for emencia.django.stylish"""
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from emencia.django.stylish.models import MarkupStyle
from emencia.django.stylish.models import StyleCollection

class MarkupStyleAdmin(admin.ModelAdmin):
    list_filter = ('markup',)
    list_display = ('markup', 'style', '__unicode__', 'applied')
    actions_on_top = False
    actions_on_bottom = True

    def applied(self, markupstyle):
        return '<div style="%s">Preview</div>' % markupstyle.style
    applied.short_description = _('preview')
    applied.allow_tags = True

class StyleCollectionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'styles_count', 'related_object_admin')
    filter_horizontal = ('styles',)
    fieldsets = ((None, {'fields': ('name',)}),
                 (None, {'fields': ('object_id', 'content_type'),}),
                 (_('Styles'), {'fields': ('styles',),}))

    actions_on_top = False
    actions_on_bottom = True

    def styles_count(self, stylecollection):
        return stylecollection.styles.count()

    def related_object_admin(self, stylecollection):
        """Display link to related object's admin"""
        if stylecollection.content_type and stylecollection.object_id:
            admin_url = reverse('admin:%s_%s_change' % (stylecollection.content_type.app_label,
                                                        stylecollection.content_type.model),
                                args=(stylecollection.object_id,))
            return '%s: <a href="%s">%s</a>' % (stylecollection.content_type.model.capitalize(),
                                                admin_url,
                                                stylecollection.content_object.__unicode__())
        return _('No relative object')
    related_object_admin.allow_tags = True
    related_object_admin.short_description = _('Related object')


admin.site.register(MarkupStyle, MarkupStyleAdmin)
admin.site.register(StyleCollection, StyleCollectionAdmin)



