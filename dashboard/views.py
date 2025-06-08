from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import OperationsFile

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    files = OperationsFile.objects.all().order_by('-last_updated')
    return render(request, 'dashboard/admin_dashboard.html', {'files': files})