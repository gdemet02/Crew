# home/models.py

from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from wagtail.snippets.models import register_snippet
from wagtail.fields import RichTextField
from home.blocks import FooterBlock

from .blocks import (
    HeroCarouselImageBlock,
    FixedSolutionsBlock,
    StyleSwitcherBlock,
    FooterBlock
)
class HeaderNavItemBlock(blocks.StructBlock):
    label = blocks.CharBlock()
    url = blocks.URLBlock()

class HeaderDropdownBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    # Later we override this dropdown with dynamic MarketingPages
    items = blocks.ListBlock(HeaderNavItemBlock())

class HeaderBlock(blocks.StructBlock):
    logo = ImageChooserBlock(help_text="Upload logo image")
    nav_items = blocks.ListBlock(HeaderNavItemBlock())
    solutions_dropdown = HeaderDropdownBlock()

@register_snippet
class GlobalHeader(models.Model):
    title = models.CharField(max_length=255, default="Main Header")
    header = StreamField([
        ("header", HeaderBlock())
    ], use_json_field=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("header"),
    ]

    def __str__(self):
        return self.title

@register_snippet
class GlobalFooter(models.Model):
    title = models.CharField(max_length=255, default="Global Footer")

    footer = StreamField([
        ('footer', FooterBlock())
    ], use_json_field=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('footer'),
    ]

    def __str__(self):
        return self.title
    
@hooks.register('register_admin_menu_item')
def register_custom_page():
    homepage = Page.objects.filter(slug='home').first()
    if homepage:
        return MenuItem(
            'Add Marketing Page',
            reverse('wagtailadmin_pages:add', args=('home', 'marketingpage', homepage.id)),
            icon_name='plus'
        )
    

class LogoCarouselBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text="Main title")
    rotating_words = blocks.ListBlock(blocks.CharBlock(), help_text="Words to rotate")
    subtitle = blocks.CharBlock(required=True, help_text="Subtitle below the heading")
    logos = blocks.ListBlock(ImageChooserBlock(), help_text="Upload logos")

    class Meta:
        template = "home/blocks/logo_carousel_block.html"
        icon = "image"
        label = "Logo Carousel"


class HomePage(Page):
    body = StreamField(
        [
            ('hero_carousel', blocks.ListBlock(HeroCarouselImageBlock())),
            ('fixed_solutions', FixedSolutionsBlock()),
            ("logo_carousel", LogoCarouselBlock()),
            ("style_switcher", StyleSwitcherBlock()),
        ],
        use_json_field=True,
        blank=True,
    )
    footer = StreamField([
        ('footer', FooterBlock())
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('footer'),
    ]


class MarketingPage(Page):
    body = StreamField([
        ('hero_section', blocks.StructBlock([
            ('background_image', ImageChooserBlock()),
            ('heading', blocks.CharBlock(required=True)),
            ('subheading', blocks.CharBlock(required=False)),
        ])),
        ('tab_section', blocks.ListBlock(blocks.StructBlock([
            ('icon', blocks.CharBlock(help_text="Font Awesome class")),
            ('label', blocks.CharBlock()),
            ('heading', blocks.CharBlock()),
            ('description', blocks.TextBlock()),
            ('image', ImageChooserBlock(required=False)),
            ('icon_image', ImageChooserBlock(required=False)),
        ]))),
        ('cta_section', blocks.StructBlock([
            ('heading', blocks.CharBlock()),
            ('features', blocks.ListBlock(blocks.CharBlock())),
            ('button_text', blocks.CharBlock()),
            ('button_link', blocks.URLBlock()),
        ])),
    ], use_json_field=True)

    footer = StreamField([
        ('footer', FooterBlock())
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('footer'),
    ]

class TeamMemberBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    role = blocks.CharBlock()
    image = ImageChooserBlock()
    description = blocks.TextBlock()
    facebook = blocks.URLBlock(required=False)
    twitter = blocks.URLBlock(required=False)
    linkedin = blocks.URLBlock(required=False)


class AboutUsPage(Page):
    body = StreamField([
        ('page_header', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('breadcrumb', blocks.CharBlock(required=False)),
        ])),
        ('who_we_are', blocks.StructBlock([
            ('heading', blocks.CharBlock()),
            ('text', blocks.RichTextBlock()),
            ('carousel_images', blocks.ListBlock(ImageChooserBlock())),
        ])),
        ('toggle_section', blocks.ListBlock(blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('content', blocks.RichTextBlock())
        ]))),
        ('team_section', blocks.ListBlock(TeamMemberBlock())),
        ('logos_carousel', blocks.ListBlock(ImageChooserBlock())),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from django.core.mail import EmailMessage
from django.utils.html import escape
from django.shortcuts import render
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class ContactPage(Page):
    heading = models.CharField(max_length=255, default="Contact Us Advanced")
    subheading = models.CharField(max_length=255, default="Get in touch with us")
    background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    intro_text = RichTextField(blank=True)

    subject_choices = models.TextField(
        help_text="Enter comma-separated subject options", default="Option 1,Option 2,Option 3,Option 4"
    )
    checkbox_choices = models.TextField(
        help_text="Enter comma-separated checkbox options", default="1,2,3"
    )
    radio_choices = models.TextField(
        help_text="Enter comma-separated radio options", default="1,2,3"
    )

    office_address = models.CharField(max_length=255, blank=True)
    office_phone = models.CharField(max_length=50, blank=True)
    office_email = models.EmailField(blank=True)
    business_hours = RichTextField(blank=True)

    gallery_images = StreamField(
        [
            ('image', ImageChooserBlock())
        ],
        blank=True,
        use_json_field=True
    )

    map_api_key = models.CharField(max_length=255, blank=True)
    map_lat = models.FloatField(default=37.09024)
    map_lng = models.FloatField(default=-95.71289)
    map_zoom = models.IntegerField(default=5)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("heading"),
            FieldPanel("subheading"),
            FieldPanel("background_image"),
        ], heading="Header Section"),

        FieldPanel("intro_text"),
        MultiFieldPanel([
            FieldPanel("subject_choices"),
            FieldPanel("checkbox_choices"),
            FieldPanel("radio_choices"),
        ], heading="Form Options"),

        MultiFieldPanel([
            FieldPanel("office_address"),
            FieldPanel("office_phone"),
            FieldPanel("office_email"),
            FieldPanel("business_hours"),
        ], heading="Office Info"),

        FieldPanel("gallery_images"),
        MultiFieldPanel([
            FieldPanel("map_api_key"),
            FieldPanel("map_lat"),
            FieldPanel("map_lng"),
            FieldPanel("map_zoom"),
        ], heading="Google Map Settings"),
    ]
    def serve(self, request):
        arr_result = None

        if request.method == "POST" and request.POST.get("emailSent"):
            subject = request.POST.get("subject", "Contact form submission")
            message = ""

            for key, value in request.POST.items():
                if key != "emailSent":
                    label = key.capitalize()
                    safe_value = escape(value).replace("\n", "<br>")
                    message += f"{label}: {safe_value}<br>"

            try:
                email = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email="you@example.com",
                    to=["you@example.com"]
                )
                email.content_subtype = "html"
                if request.FILES.get("attachment"):
                    attachment = request.FILES["attachment"]
                    email.attach(attachment.name, attachment.read(), attachment.content_type)
                email.send()
                arr_result = {"response": "success"}
            except Exception as e:
                arr_result = {"response": "error", "errorMessage": str(e)}

        context = self.get_context(request)
        context["arrResult"] = arr_result
        return render(request, "contact/contact_page.html", context)
