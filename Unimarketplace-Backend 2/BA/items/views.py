from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.contrib.auth.decorators import login_required
from .forms import NewitemForm, EdititemForm
from .models import Items
from django.core.mail import send_mail
from .forms import EmailForm


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
def Edit(request, pk):
    items = get_object_or_404(Items, pk=pk, created_by=request.user)
   
    if request.method == 'POST':
        form = EdititemForm(request.POST, request.FILES, instance=items )
       
        if form.is_valid():
           form.save()
            
           return redirect('items:detail', pk=items.id)
    else:
        form = EdititemForm(instance=items)

    return render(request, "item/form.html", {
        "form": form,
        "title": "Edit items",
    })

@login_required
def delete(request, pk):
    items = get_object_or_404(Items, pk=pk, created_by=request.user)
    items.delete()

    return redirect('dashboard:index')

@login_required
def detail(request, pk):
    try:
        item = Items.objects.get(pk=pk)
    except Items.DoesNotExist:
        raise Http404("Item does not exist")

    return render(request, 'Item/detail.html', {'item': item})


@login_required
def contact_seller(request, pk):
    item = get_object_or_404(Items, pk=pk)
    seller_email = item.created_by.email
    seller_name = item.created_by.username
    pass
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            phone_number = form.cleaned_data.get('phone_number', '')
            address = form.cleaned_data.get('address', '')
            sender_email = request.user.email
            subject = sender_email  
            
            # 
            message += f"\n\nPhone Number: {phone_number}\nAddress: {address}"
            
            # 
            send_mail(
                subject,
                message,
                sender_email,
                [seller_email],
                fail_silently=False,
            )
            # 
            return redirect('items:detail', pk=item.id)  # 
    else:
        form = EmailForm()

        return render(request, 'item/contact_seller.html', {'form': form, 'seller_name': seller_name})


