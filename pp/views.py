
from django.shortcuts import render,redirect
from django.http import FileResponse
from django.db import connection, close_old_connections,connections
from django.core.mail import send_mail,BadHeaderError

# Create your views here.
# def index(request):

#     context = {}
#     cursor = connection.cursor()
#     cursor.execute("select * from   pp_reviewsss where turnonn = 'true' order by priority desc  ;  ")
#     context = {"data":cursor.fetchall(),}
#     # cursor.close()
    

#     if request.POST.get('review-post',False) == "review-post":# == 'review-post':
#         print("review request posted")
#         name = (request.POST['name'])
#         linkid = (request.POST['ldp'])
#         title = (request.POST['title'])
#         review = (request.POST['review'])
        
#         if linkid=='' or linkid=='NULL' or linkid=='null' or 'Null':
#             linkid = 'NULL'

#         # cursor = connection.cursor()    
#         try:
#             cursor.execute("insert into pp_reviewsss(name,linkedin,title,review) values(%s,%s,%s,%s);",(name,linkid,title,review,))
            
#             connection.commit()
        
#         except Exception as e:
#             # cursor.close()
#             pass
        
#         close_old_connections()
#         cursor.close()
#         return redirect("/")

#     elif request.POST.get('letstalk-post',False) == "letstalk-post":
#         name = request.POST['Full-Name']
#         companyName = request.POST['Company-Name']
#         email = request.POST['email']
#         message = request.POST['Message']
        

#         print("lets talk request posted")
#         # cursor = connection.cursor()
#         try:        
#             cursor.execute('insert into pp_letstalk(name,company_name,company_email,message) values(%s,%s,%s,%s)',(name,companyName,email,message))
#         except Exception as e:
#             # cursor.close()
#             pass

#         close_old_connections()
#         cursor.close()
#         return redirect('/')

#     else:
#         close_old_connections()
#         cursor.close()
#         print("none posted")


#     close_old_connections()
#     cursor.close()   
#     return render(request, "pp/index.html",context)

def index(request):

    context = {}
    with connection.cursor() as cursor:
    # cursor = connection.cursor()
        cursor.execute("select * from   pp_reviewsss where turnonn = 'true' order by priority desc  ;  ")
        context = {"data":cursor.fetchall(),}
    

        if request.POST.get('review-post',False) == "review-post":# == 'review-post':
            print("review request posted")
            name = (request.POST['name'])
            linkid = (request.POST['ldp'])
            title = (request.POST['title'])
            review = (request.POST['review'])
            
            if linkid=='' or linkid=='NULL' or linkid=='null' or 'Null':
                linkid = 'NULL'

            try:
                cursor.execute("insert into pp_reviewsss(name,linkedin,title,review) values(%s,%s,%s,%s);",(name,linkid,title,review,))
                connection.commit()
            except Exception as e:
                cursor.close()
                pass
            
            close_old_connections()
            cursor.close()
            return redirect("/")

        elif request.POST.get('letstalk-post',False) == "letstalk-post":
            name = request.POST['Full-Name']
            companyName = request.POST['Company-Name']
            email = request.POST['email']
            message = request.POST['Message']
            

            print("lets talk request posted")
            # cursor = connection.cursor()
            try:        
                cursor.execute('insert into pp_letstalk(name,company_name,company_email,message) values(%s,%s,%s,%s)',(name,companyName,email,message))
            except Exception as e:
                # cursor.close()
                pass

            close_old_connections()
            cursor.close()
            return redirect('/')

        else:
            close_old_connections()
            # cursor.close()
            print("none posted")


        connections.close_all() 
        close_old_connections()
        cursor.close()  
        return render(request, "pp/index.html",context)

    return render(request, "pp/index.html",context)


def pdf_download(request):
    return FileResponse(open('Resume-Saad-Khan.pdf','rb'),as_attachment=True,content_type='application/pdf')





