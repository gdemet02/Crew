from home.models import GlobalFooter, GlobalHeader, MarketingPage

def global_components(request):
    header_instance = GlobalHeader.objects.first()
    footer_instance = GlobalFooter.objects.first()

    return {
        'global_header': header_instance.header if header_instance else None,
        'global_footer': footer_instance.footer if footer_instance else None,
        'marketing_pages': MarketingPage.objects.live().public(),
    }