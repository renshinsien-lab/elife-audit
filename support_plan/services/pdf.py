from django.template.loader import render_to_string
from weasyprint import HTML

def generate_plan_pdf(plan):
    html = render_to_string("support_plan/report.html", {"plan": plan})
    return HTML(string=html).write_pdf()