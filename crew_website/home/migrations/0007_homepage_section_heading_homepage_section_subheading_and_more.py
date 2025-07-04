# Generated by Django 5.2.2 on 2025-06-25 11:28

import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_remove_homepage_section_heading_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="section_heading",
            field=models.CharField(
                default="Explore All Possibilities",
                help_text="Main heading above the solutions section",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="section_subheading",
            field=models.TextField(blank=True, help_text="Optional subheading text"),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [("fixed_solutions", 5), ("logo_carousel", 12)],
                blank=True,
                block_lookup={
                    0: (
                        "wagtail.images.blocks.ImageChooserBlock",
                        (),
                        {"required": False},
                    ),
                    1: ("wagtail.blocks.CharBlock", (), {"required": True}),
                    2: ("wagtail.blocks.URLBlock", (), {"required": True}),
                    3: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("image", 0),
                                ("title", 1),
                                ("button_text", 1),
                                ("button_link", 2),
                            ]
                        ],
                        {},
                    ),
                    4: ("wagtail.blocks.ListBlock", (3,), {}),
                    5: ("wagtail.blocks.StructBlock", [[("solutions", 4)]], {}),
                    6: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"help_text": "Main title", "required": True},
                    ),
                    7: ("wagtail.blocks.CharBlock", (), {}),
                    8: (
                        "wagtail.blocks.ListBlock",
                        (7,),
                        {"help_text": "Words to rotate"},
                    ),
                    9: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"help_text": "Subtitle below the heading", "required": True},
                    ),
                    10: ("wagtail.images.blocks.ImageChooserBlock", (), {}),
                    11: (
                        "wagtail.blocks.ListBlock",
                        (10,),
                        {"help_text": "Upload logos"},
                    ),
                    12: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("heading", 6),
                                ("rotating_words", 8),
                                ("subtitle", 9),
                                ("logos", 11),
                            ]
                        ],
                        {},
                    ),
                },
            ),
        ),
    ]
