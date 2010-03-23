"""Unit tests for emencia.django.stylish"""
from django.test import TestCase

from emencia.django.stylish.utils import apply_styles
from emencia.django.stylish.models import MarkupStyle
from emencia.django.stylish.models import StyleCollection


class StylishTestCase(TestCase):

    def setUp(self):
        self.styles = [MarkupStyle.objects.create(markup='a', style='color: #FF0000;'),
                       MarkupStyle.objects.create(markup='p', style='color: #00FF00;'),
                       MarkupStyle.objects.create(markup='p', style='background-color: #0000FF;'),]
        
        self.style_collection  = StyleCollection.objects.create(name='Test')
        self.style_collection.styles.add(*self.styles)

    def test_apply_styles(self):
        html = '<p><a href="example.com">Click here</a></p>'
        html_stylized = apply_styles(html, self.style_collection.styles.all())
        self.assertEquals(html_stylized, '<p style="background-color: #0000FF;">\n <a href="example.com" style="color: #FF0000;">\n  Click here\n </a>\n</p>')

