from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from urllib.parse import urlencode

def index(request):
    context = {}

    if request.method == "POST" and "letstalk-post" in request.POST:
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
            # Redirect with a success flag in the URL
            params = urlencode({"success": "1"})
            return redirect(f"/?{params}")

        except BadHeaderError:
            params = urlencode({"error": "Invalid header found. Please try again."})
            return redirect(f"/?{params}")
        except Exception:
            params = urlencode({"error": "Something went wrong while sending your message. Please try again later."})
            return redirect(f"/?{params}")

    # Handle messages from query params
    success = request.GET.get("success")
    error = request.GET.get("error")

    if success:
        context["success"] = "Your message has been sent successfully! 🎉"
    elif error:
        context["error"] = error

    return render(request, "pp/index.html", context)
