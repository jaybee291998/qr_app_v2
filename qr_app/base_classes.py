import random

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

class BaseCreateView(CreateView):
	def form_valid(self, form):
		form.instance.qr_code = generate_qr_string()
		form.save()

		return super(BaseCreateView, self).form_valid(form)

def generate_qr_string():
	qr_str = ''
	for _ in range(6):
		qr_str += chr(random.randrange(32, 128, 1))

	return qr_str