# funciones de ayuda
def create_alert(type,message):
    return {"type": type, "message": message}


def create_moneda(request):
    try:
        moneda = request.session["moneda"]
    except KeyError:
        request.session["moneda"] = "clp"
        moneda = request.session["moneda"]
    
    return moneda