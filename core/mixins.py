from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

class StaffRequiredMixin(LoginRequiredMixin):
    @method_decorator(staff_member_required(login_url="/")) # type: ignore
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff: # type: ignore
            return redirect('/')
        return super().dispatch(request, *args, **kwargs) # type: ignore
