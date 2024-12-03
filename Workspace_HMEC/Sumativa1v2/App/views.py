from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Reserva
from .forms import ReservaForm
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as PlatypusImage, HRFlowable
from PIL import Image as PILImage
from io import BytesIO
import os
from django.contrib import messages

def agregarReserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            reserva = form.save()
            # Enviar correo electrónico de confirmación
            send_mail(
                'Reserva Confirmada',
                f'Su reserva ha sido confirmada:\n\n'
                f'Nombre: {reserva.nombre}\n'
                f'Fecha: {reserva.fechareserva}\n'
                f'Hora: {reserva.horareserva}',
                settings.EMAIL_HOST_USER,
                [reserva.email],
                fail_silently=False,
            )
            # Agregamos un mensaje de éxito al sistema de mensajes
            messages.success(request, 'Reserva confirmada')
            return redirect('/')
    else:
        form = ReservaForm()

    reservas = Reserva.objects.all()
    context = {
        'form': form,
        'reservas': reservas,
    }
    return render(request, 'templatesApp/agregar.html', context)

def eliminarReserva(request, id):
    reserva = get_object_or_404(Reserva, idSolicitud=id)
    reserva.delete()
    return redirect('/')

def actualizarReserva(request, id):
    reserva = get_object_or_404(Reserva, idSolicitud=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ReservaForm(instance=reserva)

    reservas = Reserva.objects.all()
    context = {
        'form': form,
        'reservas': reservas,
    }
    return render(request, 'templatesApp/agregar.html', context)

def generar_pdf(request, id):
    reserva = get_object_or_404(Reserva, idSolicitud=id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Reserva_{reserva.nombre}.pdf"'
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='TitleStyle',
        fontSize=20,
        leading=24,
        alignment=1,
        textColor=colors.HexColor("#2E86C1"),
        spaceAfter=20
    ))
    styles.add(ParagraphStyle(
        name='NormalStyle',
        fontSize=12,
        leading=15,
        spaceAfter=10
    ))
    styles.add(ParagraphStyle(
        name='FooterStyle',
        fontSize=10,
        leading=12,
        alignment=1,
        textColor=colors.HexColor("#7B7D7D"),
        spaceBefore=30
    ))
    elements = []
    titulo = f"Confirmación de Reserva para {reserva.nombre}"
    elements.append(Paragraph(titulo, styles['TitleStyle']))
    hr = HRFlowable(width="100%", thickness=2, lineCap='round',
                   color=colors.HexColor("#2E86C1"), spaceAfter=20)
    elements.append(hr)
    datos = [
        f"<b>Nombre:</b> {reserva.nombre}",
        f"<b>Teléfono:</b> {reserva.telefono}",
        f"<b>Fecha de Nacimiento:</b> {reserva.fecha_nacimiento.strftime('%d/%m/%Y')}",
        f"<b>Edad:</b> {reserva.edad}",
        f"<b>Fecha de Reserva:</b> {reserva.fechareserva.strftime('%d/%m/%Y')}",
        f"<b>Hora de Reserva:</b> {reserva.horareserva.strftime('%H:%M')}",
        f"<b>Cantidad de Hermanos:</b> {reserva.cantidad_hermanos}",
        f"<b>Observaciones:</b> {reserva.observaciones}",
        f"<b>Website:</b> <a href='{reserva.website}' color='blue'>{reserva.website}</a>",
        f"<b>Email:</b> <a href='mailto:{reserva.email}' color='blue'>{reserva.email}</a>",
        f"<b>Estado de Reserva:</b> {reserva.estadoReservaId}",
        f"<b>Tipo de Reserva:</b> {reserva.tipoSolicitudId}",
    ]
    for dato in datos:
        elements.append(Paragraph(dato, styles['NormalStyle']))
    if reserva.foto_carnet and reserva.foto_carnet.path and os.path.exists(reserva.foto_carnet.path):
        try:
            carnet_image = PlatypusImage(reserva.foto_carnet.path)
            carnet_image.hAlign = 'CENTER'
            max_width = 200
            if carnet_image.imageWidth > max_width:
                ratio = max_width / carnet_image.imageWidth
                carnet_image.drawWidth = max_width
                carnet_image.drawHeight = carnet_image.imageHeight * ratio
            elements.append(Spacer(1, 20))
            elements.append(carnet_image)
        except Exception as e:
            error_message = f"Error al cargar la imagen: {str(e)}"
            elements.append(Spacer(1, 10))
            error_paragraph = Paragraph(f"<font color='red'>{error_message}</font>", styles['NormalStyle'])
            elements.append(error_paragraph)
    else:
        elements.append(Spacer(1, 10))
        no_image_paragraph = Paragraph("<font color='gray'>Imagen no disponible.</font>", styles['NormalStyle'])
        elements.append(no_image_paragraph)
    elements.append(Spacer(1, 30))
    footer_text = "Gracias por su reserva. Esperamos verle pronto."
    elements.append(Paragraph(footer_text, styles['FooterStyle']))
    try:
        doc.build(elements)
    except Exception as e:
        response = HttpResponse(content_type='text/plain')
        response.write(f"Error al generar el PDF: {str(e)}")
        return response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def generar_qr_pdf(request, id):
    reserva = get_object_or_404(Reserva, idSolicitud=id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="QR_{reserva.nombre}.pdf"'
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='TitleStyle',
        fontSize=20,
        leading=24,
        alignment=1,
        textColor=colors.HexColor("#2E86C1"),
        spaceAfter=20
    ))
    styles.add(ParagraphStyle(
        name='NormalStyle',
        fontSize=12,
        leading=15,
        spaceAfter=10
    ))
    elements = []
    titulo = f"Código QR de la Reserva de {reserva.nombre}"
    elements.append(Paragraph(titulo, styles['TitleStyle']))
    hr = HRFlowable(width="100%", thickness=2, lineCap='round',
                   color=colors.HexColor("#2E86C1"), spaceAfter=20)
    elements.append(hr)
    if reserva.qr_code and reserva.qr_code.path and os.path.exists(reserva.qr_code.path):
        try:
            qr_image = PlatypusImage(reserva.qr_code.path)
            qr_image.hAlign = 'CENTER'
            max_width = 200
            if qr_image.imageWidth > max_width:
                ratio = max_width / qr_image.imageWidth
                qr_image.drawWidth = max_width
                qr_image.drawHeight = qr_image.imageHeight * ratio
            elements.append(Spacer(1, 20))
            elements.append(qr_image)
        except Exception as e:
            error_message = f"Error al cargar el código QR: {str(e)}"
            elements.append(Spacer(1, 10))
            error_paragraph = Paragraph(f"<font color='red'>{error_message}</font>", styles['NormalStyle'])
            elements.append(error_paragraph)
    else:
        elements.append(Spacer(1, 10))
        no_qr_paragraph = Paragraph("<font color='gray'>Código QR no disponible.</font>", styles['NormalStyle'])
        elements.append(no_qr_paragraph)
    try:
        doc.build(elements)
    except Exception as e:
        response = HttpResponse(content_type='text/plain')
        response.write(f"Error al generar el PDF: {str(e)}")
        return response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
