
DEFAULT_FONT_SIZE = "font-size-estandar"
DEFAULT_FONT_FAMILY = "font-family-roboto"
DEFAULT_NAME = "Anónimo"


def manageNameLogin(request):
    username = request.session.get('username')
    # Para ver que puede ser un valor, vacio o None,
    # en caso de estos dos ultimos valores, se asigna el valor por defecto
    # print(f"Name: {username}")
    if username == "" or username is None:
        username = DEFAULT_NAME
    # Para comprobar que se ha guardado el nombre en la consola
    # print(f"Name: {username}")
    return username


def manageSize(request):
    size = request.session.get('font_size')
    if size == "small":
        font_size = "font-size-pequena"
    elif size == "large":
        font_size = "font-size-grande"
    else:
        font_size = DEFAULT_FONT_SIZE
    # print(f"Size: {font_size}")
    return font_size


def manageFamily(request):
    family = request.session.get('font_family')
    if family == "Courier New":
        font_family = "font-family-courier"
    elif family == "Verdana":
        font_family = "font-family-verdana"
    elif family == "Times New Roman":
        font_family = "font-family-times"
    elif family == "Helvetica":
        font_family = "font-family-helvetica"
    elif family == "Arial":
        font_family = "font-family-arial"
    elif family == "C4 Type":
        font_family = "font-family-c4type"
    else:
        font_family = DEFAULT_FONT_FAMILY
    return font_family


def get_user_config(request):
    name = manageNameLogin(request)
    font_size = manageSize(request)
    font_family = manageFamily(request)
    return name, font_size, font_family
