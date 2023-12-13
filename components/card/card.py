from django_components import component


@component.register("card")
class Card(component.Component):
    template_name = "card/card.html"

    def get_context_data(self, recipe_link, recipe_name, recipe_button):
        return {
            "recipe_link": recipe_link,
            "recipe_name": recipe_name,
            "recipe_button": recipe_button,
        }
