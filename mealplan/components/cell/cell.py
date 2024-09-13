from django_components import component


@component.register("cell")
class Cell(component.Component):
    template_name = "cell/cell.html"

    def get_context_data(self, text):
        return {
            "text": text,
        }
