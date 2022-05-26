from dataclasses import dataclass


@dataclass
class PDFRenderer():
    def render_form(self, form_name, *args, **kwargs):
        """Render an Anvil form to PDF. Pass the name of the form you want to render, plus any arguments you want to
        pass to its constructor.Returns a PDF as an Anvil Media object. """
        pass

    pass


def render_form(form_name, *args, **kwargs):
    """Render an Anvil form to PDF. Pass the name of the form you want to render, plus any arguments you want to pass
    to its constructor.Returns a PDF as an Anvil Media object. """
    pass
