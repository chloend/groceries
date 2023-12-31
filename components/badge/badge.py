from django_components import component


@component.register("badge")
class Badge(component.Component):
    template_name = "badge/badge.html"

    def get_context_data(self, text):
        return {
            "text": text,
        }