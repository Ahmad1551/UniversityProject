from django.views.generic.base import View

from wkhtmltopdf.views import PDFTemplateResponse

from projects.models import Installment, File


class MyPDFView(View):
    template = 'invoice.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['installments'] = Installment.objects.filter(plot_id=kwargs.get('pk', None)).order_by('id')
        self.origin = self.context["installments"].first()
        self.context['file'] = File.objects.filter(plot_id=kwargs.get('pk', None)).first()
        self.context['origin'] = self.origin
        response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       filename=f"{self.origin.plot.plot_book_number}.pdf",
                                       show_content_in_browser=False,
                                       context=self.context,
                                       cmd_options={'quiet': False, "enable-local-file-access": ""},
                                       )
        return response
