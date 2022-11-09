
from django.shortcuts import render,redirect
from django.http import FileResponse
from django.db import connection
from django.core.mail import send_mail,BadHeaderError
from . import models

# Create your views here.
# def index(request):

#     context = {}
#     cursor = connection.cursor()
#     cursor.execute("select * from pp_reviewsss where turnonn = 'true' order by priority desc;")
#     context = {"data":cursor.fetchall(),}
#     cursor.close()

#     if request.POST.get('review-post',False) == "review-post":# == 'review-post':
#         print("review request posted")
#         name = (request.POST['name'])
#         linkid = (request.POST['ldp'])
#         title = (request.POST['title'])
#         review = (request.POST['review'])
        
#         cursor = connection.cursor()    
#         try:
#             cursor.execute("insert into reviews(name,linkedin_url,title,review,turnonn) values(%s,%s,%s,%s,%s);",(name,linkid,title,review,'false',))
            
#             connection.commit()
#             # print(f"context is: {context}")
            
#         except Exception as e:
#            cursor.close()

#         return redirect("/")

#     elif request.POST.get('letstalk-post',False) == "letstalk-post":
#         subject = "portfolio review submitted"
#         body = {
#             "Name":request.POST['Full-Name'],
#             "companyName":request.POST['Company-Name'],
#             "company_email":request.POST['email'],
#             "message":request.POST['Message'],
#         }
#         message = "\n".join(body.values())
        
#         try:
#             success = send_mail(
#                 subject,
#                 message,
#                 'saadan060@gmail.com',
#                 ['saadan060@gmail.com',],
#                 fail_silently=False,
#                 auth_password='lucifermorningstar',
#             )
#             print(f"success value is: {success}")
#             print("sending message")
#         except BadHeaderError as e:
#             print(f"email not send,error:{e}")
            
        
        
#         print("lets talk request posted")

#         return redirect('/')

#     else:
#         print("none posted")


#     return render(request, "pp/index.html",context)

def index(request):

    context = {}
    cursor = connection.cursor()
    cursor.execute("select * from pp_reviewsss where turnonn = 'true' order by priority desc;")
    context = {"data":cursor.fetchall(),}
    print(context)

    cursor.close()

    if request.POST.get('review-post',False) == "review-post":# == 'review-post':
        print("review request posted")
        name = (request.POST['name'])
        linkid = (request.POST['ldp'])
        title = (request.POST['title'])
        review = (request.POST['review'])
        
        cursor = connection.cursor()    
        try:
            cursor.execute("insert into pp_reviewsss(name,linkedin,title,review) values(%s,%s,%s,%s);",(name,linkid,title,review,))
            
            connection.commit()
        
        except Exception as e:
            cursor.close()
            
        return redirect("/")

    elif request.POST.get('letstalk-post',False) == "letstalk-post":
        subject = "portfolio review submitted"
        body = {
            "Name":request.POST['Full-Name'],
            "companyName":request.POST['Company-Name'],
            "company_email":request.POST['email'],
            "message":request.POST['Message'],
        }
        message = "\n".join(body.values())
        
        try:
            success = send_mail(
                subject,
                message,
                'saadan060@gmail.com',
                ['saadan060@gmail.com',],
                fail_silently=False,
                auth_password='lucifermorningstar',
            )
            print(f"success value is: {success}")
            print("sending message")
        except BadHeaderError as e:
            print(f"email not send,error:{e}")
            
        
        
        print("lets talk request posted")

        return redirect('/')

    else:
        print("none posted")


    return render(request, "pp/index.html",context)


def pdf_download(request):
    
    return FileResponse(open('Resume-Saad-Khan.pdf','rb'),as_attachment=True,content_type='application/pdf')





