from django.shortcuts import render

def display(request):
    return render(request, "index.html")

def show(request):
    res = request.POST.getlist("mv")
    if len(res) == 0:
        global data
        data = {"key": 0}
        return render(request, "show.html", data)

    elif len(res) == 1:
        if res[0] == "uri":
            data = {"key": "uri"}
            return render(request, "show.html", data)

        elif res[0] == "border":
            data = {"key": "border"}
            return render(request, "show.html", data)

        else:
            data = {"key": "kgf"}
            return render(request, "show.html", data)

    elif len(res) == 2:
        if "uri" in res and "border" in res:
            data = {"key": "uri and border"}
            return render(request, "show.html", data)

        elif "uri" in res and "kgf" in res:
            data = {"key": "uri and kgf"}
            return render(request, "show.html", data)

        else:
            data = {"key": "border and kgf"}
            return render(request, "show.html", data)

    else:
        data = {"key": 3}
        return render(request, "show.html", data)
