from django.shortcuts import render, redirect
from django.http import FileResponse
from django.core.mail import send_mail, BadHeaderError

def index(request):
    context = {}

    if request.method == "POST":
        if "letstalk-post" in request.POST:
            name = request.POST.get("Full-Name")
            companyName = request.POST.get("Company-Name")
            email = request.POST.get("email")
            message = request.POST.get("Message")

            try:
                send_mail(
                    subject=f"Portfolio Contact from {name} ({companyName})",
                    message=f"Message from: {name}\nCompany: {companyName}\nEmail: {email}\n\n{message}",
                    from_email="saadan06@gmail.com",  # your email
                    recipient_list=["saadan06@gmail.com"],
                    fail_silently=False,
                )
                # ✅ Store a success message in session before redirecting
                request.session['success_message'] = "Your message has been sent successfully! 🎉"
            except BadHeaderError:
                request.session['error_message'] = "Invalid header found. Please try again."
            except Exception:
                request.session['error_message'] = "Something went wrong while sending your message. Please try again later."

            # ✅ Redirect to avoid form resubmission
            return redirect("/")

    # ✅ Check if there was a success/error message from a previous redirect
    if 'success_message' in request.session:
        context['success'] = request.session.pop('success_message')
    elif 'error_message' in request.session:
        context['error'] = request.session.pop('error_message')

    return render(request, "pp/index.html", context)


def pdf_download(request):
    return FileResponse(open('Resume-Saad-Khan.pdf','rb'), as_attachment=True, content_type='application/pdf')
