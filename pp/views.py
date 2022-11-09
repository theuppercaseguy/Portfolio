
from django.shortcuts import render,redirect
from django.http import FileResponse
from django.db import connection
from django.core.mail import send_mail,BadHeaderError

# Create your views here.
def index(request):

    context = {}
    cursor = connection.cursor()
    cursor.execute("select * from pp_reviewsss where turnonn = 'true' order by priority desc;")
    context = {"data":cursor.fetchall(),}
    cursor.close()

    if request.POST.get('review-post',False) == "review-post":# == 'review-post':
        print("review request posted")
        name = (request.POST['name'])
        linkid = (request.POST['ldp'])
        title = (request.POST['title'])
        review = (request.POST['review'])
        if linkid=='':
            linkid = 'NULL'

        cursor = connection.cursor()    
        try:
            cursor.execute("insert into pp_reviewsss(name,linkedin,title,review) values(%s,%s,%s,%s);",(name,linkid,title,review,))
            
            connection.commit()
        
        except Exception as e:
            cursor.close()
            
        return redirect("/")

    elif request.POST.get('letstalk-post',False) == "letstalk-post":
        name = request.POST['Full-Name']
        companyName = request.POST['Company-Name']
        email = request.POST['email']
        message = request.POST['Message']
        

        print("lets talk request posted")
        cursor = connection.cursor()
        try:        
            cursor.execute('insert into pp_letstalk(name,company_name,company_email,message) values(%s,%s,%s,%s)',(name,companyName,email,message))
        except Exception as e:
            cursor.close()

        cursor.close()
        return redirect('/')

    else:
        print("none posted")

    print(cursor)
    cursor.close()
    print(cursor)
   
    return render(request, "pp/index.html",context)


def pdf_download(request):
    
    return FileResponse(open('Resume-Saad-Khan.pdf','rb'),as_attachment=True,content_type='application/pdf')





