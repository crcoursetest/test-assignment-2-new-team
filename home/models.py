from django.db import models

from django.shortcuts import render
from wagtail.core.models import Page, Site
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from blog.models import BlogPage


class HomePage(Page):
    subtitle = models.CharField(max_length=255, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle')
    ]

    def serve(self, request):
        # Get blogs
        blogs = BlogPage.objects.filter(live=True)
        blogs = blogs.order_by('-date')

        tag = request.GET.get('tag')
        print(tag)
        if tag:
            blogs = blogs.filter(tags__name=tag)
        show_nav = True
        return render(request, self.template, {
            'self': self,
            'blogs': blogs,
            'show_nav': show_nav,
        })
