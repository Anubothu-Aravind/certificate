import os
import csv
from PIL import Image, ImageDraw, ImageFont
import pandas as production
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
FONT_COLOR = "#000000"
WIDTH, HEIGHT = 380,270
e_w,e_h=318,377
FONT_SIZE = 35  # Set your desired font size here

def send_email_with_attachment(subject, message, recipient_list, attachment_path):
    email = EmailMessage(
        subject,
        message,
        "intelligentsia.techclub@gmail.com",  # Sender's email address
        recipient_list,
    )

    # Attach the file
    email.attach_file(attachment_path)

    # Send the email
    email.send()


def make_cert(name, id, event):
    """function to generate certificate"""
    image_source = Image.open(r'./genrator//template_certificate//template.png')
    draw = ImageDraw.Draw(image_source)

    font = ImageFont.truetype("./genrator//template_certificate/fonts/Italic.ttf", FONT_SIZE)
    text_bbox = draw.textbbox((0, 0), name, font=font)
    font_e = ImageFont.truetype("./genrator//template_certificate/fonts/Italic.ttf", 20)
    # Calculate the width and height from the bounding box
    name_width = text_bbox[2] - text_bbox[0]
    name_height = text_bbox[3] - text_bbox[1]

    # Draw the text with the new font
    draw.text((WIDTH - name_width / 2, HEIGHT - name_height / 2), name, fill=FONT_COLOR, font=font)
    draw.text((e_w, e_h), event, fill=FONT_COLOR, font=font_e)
    event_directory = os.path.join("./genrator//template_certificate/Certificates/" + event)
    if not os.path.exists(event_directory):
        os.mkdir(event_directory)
    output_path = os.path.join(event_directory, f"{id}.png")
    image_source.save(output_path)
    print('printing certificate of: ' + name)

def certificate():
    with open("./genrator//template_certificate/data/data.csv", 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        header = csv_reader.fieldnames
        print(' '.join(header))
        for row in csv_reader:
            make_cert(row['name'],row['id'],row['event_name'])
            subject = "Certificate of"+row['event_name']
            message = "Hii "+row['name']+" We are happy to say that you are actively participated in "+row['event_name']+".This is your certificate."
            recipient_list = [row['email']]
            attachment_path = './genrator/template_certificate/Certificates/'+row['event_name']+"/"+row['id']+".png"
            send_email_with_attachment(subject, message, recipient_list, attachment_path)