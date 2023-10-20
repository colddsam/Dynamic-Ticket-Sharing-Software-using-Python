# Dynamic Ticket Sharing Software using Python
It is my second version of QR code login software. Where you can mail every person from google form registration for an event automatically with unique ID and barcode/qrcode to everyone (limitation 500 request/hr) and the data will save in "data.csv" file.

## FEATURES :
- You can automate your google form just by sharing your form with your google cloud generated service mail id.
- Here it will generate Unique ID for every person on the google form.
- We also sending the Unique QR code to every person using the mail.

## NEW FEATURES:
- Now you can create Barcode with it.
- The data can now save into csv file ("data.csv").
- Dynamically make image or ticket for each unique ID.

## TECHNICAL STACK :
- Python
- SMTP
- MAIL
- HTML
- Labelimg
- Google Sheets

## PREREQUISITES:
- First got the google service account credentials secret key in .json format and save it as "secret_key.json" in this format on the project directory.
- Then create a Google Sheet and make two column with "First Name" and "Email Address" is mandatory.
- Then save your smtp email id and password in ".env" file.
- Now you have to label the place in where you want to attach the Barcode or QR code.
- Then according to this you have to modify the "imageoperation.py" file.
- At the end run "app.py" file in terminal it will work automatically.
- Make sure you are in the project directory.

## UPCOMING MODIFICATION : 
In next update I will add a proper GUI for this software.