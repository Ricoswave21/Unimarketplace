from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewitemForm
from .models import Items
from django.core.mail import send_mail
from .forms import EmailForm

def detail(request, pk):
    item = get_object_or_404(Items, pk=pk)
    related_items = Items.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewitemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('items:detail', pk=item.id)
    else:
        form = NewitemForm()

    return render(request, "item/form.html", {
        "form": form,
        "title": "New item",
    })
@login_required
def contact_seller(request, pk):
    item = get_object_or_404(Items, pk=pk)
    seller_email = item.created_by.email
    seller_name = item.created_by.username
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            phone_number = form.cleaned_data.get('phone_number', '')
            address = form.cleaned_data.get('address', '')
            sender_email = request.user.email
            subject = sender_email  # Set the subject to the email of the logged-in user
            
            # Include phone number and address in the message body
            message += f"\n\nPhone Number: {phone_number}\nAddress: {address}"
            
            # Send the email
            send_mail(
                subject,
                message,
                sender_email,
                [seller_email],
                fail_silently=False,
            )
            # Optionally, you can add a success message or redirect the user to another page
            return redirect('items:detail', pk=item.id)  # Redirect to a success page
    else:
        form = EmailForm()

        return render(request, 'item/contact_seller.html', {'form': form, 'seller_name': seller_name})
    