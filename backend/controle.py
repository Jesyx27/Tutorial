from backend.magic import make_checker_magic, display, HTML, md

class CustomException(Exception):
    def __init__(self, message):
        self.message = message


class CustomWarning(Exception):
    def __init__(self, message):
        self.message = message


def _display(title, message="", error=False, warning=False):
    """Display a message with a title and optional error indication."""
    if error:
        color = "red"
    elif warning:
        color = "orange"
    else:
        color = "green"

    display(HTML(f"""
        <div style="border:2px solid {color}; background:#222222; padding:10px; border-radius:10px;">
            <strong>{title}</strong><br>
            {message}
        </div>
    """))


@make_checker_magic('check_1_1')
def check_1_1(e):
    if isinstance(e, Exception):
        title = "Opdracht 1 is helaas niet goed"
        iserror = True
        iswarning = False

        if isinstance(e, CustomException):
            message = str(e)
        elif isinstance(e, CustomWarning):
            title = "Opdracht 1 is nog niet helemaal juist"
            message = str(e)
            iswarning = True
            iserror = False
        elif isinstance(e, NameError):
            message = "Het lijkt erop dat je een NameError hebt gemaakt. Controleer of je de variabel <code>favnum</code> goed hebt aangemaakt."
        elif isinstance(e, TypeError):
            message = "Het lijkt erop dat je een TypeError hebt gemaakt. Controleer of je de juiste types gebruikt."
        else:
            message = "Er is een onbekende fout opgetreden (<code>{}</code>).<br>Controleer je code en probeer het opnieuw.".format(e)

        _display(title, message, error=iserror, warning=iswarning)
    else:
        globals_, cell_ = e
        if 'favnum' in globals_:
            pass
        else:
            raise CustomException('Het variabel <code>favnum</code> is niet gedefinieerd. Zorg ervoor dat je deze variabele aanmaakt met een waarde van jouw favoriete getal; bijvoorbeeld: `favnum = 1`')
        
        if not isinstance(globals_['favnum'], int):
            raise CustomWarning('Het variabel <code>favnum</code> is geen (heel) nummer. Zorg ervoor dat je deze variabele aanmaakt met een waarde van jouw favoriete getal; bijvoorbeeld: `favnum = 1`')

        _display("Opdracht 1 is goed!", "Je hebt de opdracht goed uitgevoerd en jouw favoriete nummer {} is. Ga verder met de volgende opdracht.".format(
            globals_['favnum']
        ))


@make_checker_magic('check_1_2')
def check_1_2(e):
    if isinstance(e, Exception):
        title = "Opdracht 2 is helaas niet goed"
        if isinstance(e, CustomException):
            message = str(e)
        elif isinstance(e, NameError):
            message = 'Er is nog geen datatype ingevuld. Voer een van de volgende datatypen in: <code>bool</code>, <code>int</code>, <code>float</code> of <code>str</code>'
        else:
            message = "Er is een onbekende fout opgetreden (<code>{}</code>).<br>Controleer je code en probeer het opnieuw.".format(e)

        _display(title, message, error=True)
    else:
        globals_, cell_ = e
        cell = cell_.strip().split('\n')
        is_int = any([line.strip().lower() == 'int' for line in cell])
        tpes = ['bool', 'float', 'str', 'list', 'tuple', 'dict', 'set', 'frozenset', 'complex']
        is_other_type = any([any([line.strip().lower() == tpe for tpe in tpes]) for line in cell])

        if not is_int:
            if is_other_type:
                raise CustomException('Dit is helaas nog niet het juiste datatype. Probeer het opnieuw')
            else:
                raise NameError()
        
        _display("Opdracht 2 is goed!", "Je hebt de opdracht goed uitgevoerd. Ga verder met de volgende opdracht.")