# home/blocks.py

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroCarouselImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True, help_text="Select the image for this carousel slide.")
    heading = blocks.CharBlock(required=True, help_text="Main heading text")
    subheading = blocks.CharBlock(required=False, help_text="Optional subheading text")
    button_text = blocks.CharBlock(required=False, help_text="Text on the button")
    button_link = blocks.URLBlock(required=False, help_text="URL the button will link to")

    class Meta:
        template = "home/blocks/hero_carousel_image.html"
        icon = "image"
        label = "Hero Carousel Image"


class SolutionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Title for the solution item")
    image = ImageChooserBlock(required=True, help_text="Background image")
    link = blocks.URLBlock(required=False, help_text="Optional link for the solution")

    class Meta:
        template = "home/blocks/solution_block.html"
        icon = "image"
        label = "Solution"


class FixedSolutionsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text="Main heading above the solutions section")
    subheading = blocks.TextBlock(required=False, help_text="Optional subheading text")
    solutions = blocks.ListBlock(SolutionBlock(), help_text="Add 5 items: 2 top, 3 bottom.")

    class Meta:
        template = "home/blocks/fixed_solutions_block.html"
        icon = "placeholder"
        label = "Fixed Solutions Section"


class StyleSwitcherBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text="Main heading")
    highlight = blocks.CharBlock(required=True, help_text="Highlighted word in heading")
    description = blocks.TextBlock(required=True, help_text="Main paragraph text")
    extra_text = blocks.TextBlock(required=False, help_text="Optional extra paragraph")
    image = ImageChooserBlock(required=True, help_text="Associated image")

    class Meta:
        template = "home/blocks/style_switcher_block.html"
        icon = "image"
        label = "Style Switcher Section"


class FooterBlock(blocks.StructBlock):
    logo = ImageChooserBlock(required=False)
    description = blocks.TextBlock(required=False)
    view_more_link = blocks.URLBlock(required=False)

    address = blocks.CharBlock(required=False)
    phone = blocks.CharBlock(required=False)
    email = blocks.CharBlock(required=False)

    link_1 = blocks.StructBlock([
        ("label", blocks.CharBlock()),
        ("url", blocks.URLBlock())
    ])
    link_2 = blocks.StructBlock([
        ("label", blocks.CharBlock()),
        ("url", blocks.URLBlock())
    ])
    link_3 = blocks.StructBlock([
        ("label", blocks.CharBlock()),
        ("url", blocks.URLBlock())
    ])

    copyright = blocks.CharBlock()

    class Meta:
        template = "home/blocks/footer_block.html"
        icon = "site"
        label = "Footer"
