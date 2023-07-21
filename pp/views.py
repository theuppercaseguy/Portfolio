
from django.shortcuts import render,redirect
from django.http import FileResponse
from django.db import connection, close_old_connections,connections
from django.core.mail import send_mail,BadHeaderError

# Create your views here.

def index(request):

    context = {}
    with connection.cursor() as cursor:
    # cursor = connection.cursor()
        cursor.execute("select * from   pp_reviewsss where turnonn = 'true' order by priority desc  ;  ")
        context = {"data":cursor.fetchall(),}
    

        if request.method == "POST":
            if "review-post" in request.POST:
                name = request.POST.get("name")
                linkid = request.POST.get("ldp")
                print("/n/n Hello word: ",linkid)
                title = request.POST.get("title")
                review = request.POST.get("review")
                if linkid in ('', 'NULL', 'null', 'Null'):
                    linkid = None

                try:
                    cursor.execute("INSERT INTO pp_reviewsss (name, linkedin, title, review) VALUES (%s, %s, %s, %s);", (name, linkid, title, review))
                    connection.commit()
                except Exception as e:
                    pass

                return redirect("/")

            elif "letstalk-post" in request.POST:
                name = request.POST.get("Full-Name")
                companyName = request.POST.get("Company-Name")
                email = request.POST.get("email")
                message = request.POST.get("Message")

                try:
                    cursor.execute('INSERT INTO pp_letstalk (name, company_name, company_email, message) VALUES (%s, %s, %s, %s)', (name, companyName, email, message))
                except Exception as e:
                    pass

                return redirect('/')

    return render(request, "pp/index.html", context)


def pdf_download(request):
    return FileResponse(open('Resume-Saad-Khan.pdf','rb'),as_attachment=True,content_type='application/pdf')





