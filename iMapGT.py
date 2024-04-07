import imaplib
import email
import re
import webbrowser
from email.header import decode_header

while True:
    credentials_input = input("Masukkan email dan kata sandi (format: email:password), atau ketik 'purani' untuk keluar: ")
    
    if credentials_input.lower() == 'purani':
        break


    credentials_list = credentials_input.split(",")

    for credentials in credentials_list:
        username, password = credentials.strip().split(":")

        imap_server = 'imap-mail.outlook.com'
        port = 993

        imap = imaplib.IMAP4_SSL(imap_server, port)

        try:
            imap.login(username, password)

            imap.select('inbox')

            status, email_ids = imap.search(None, 'ALL')

            email_id_list = email_ids[0].split()

            def extract_growtopia_links(text):
                return re.findall(r'https://growtopiagame\.com/player/[^\s]+', text)

            last_link = None  

            for email_id in email_id_list:
                status, email_data = imap.fetch(email_id, '(RFC822)')

                raw_email = email_data[0][1]
                msg = email.message_from_bytes(raw_email)

                if msg['From'] and "Growtopia Game" in msg['From']:
                    print(f"From: {msg['From']}")
                    print(f"Subject: {decode_header(msg['Subject'])[0][0]}")  
                    print(f"Date: {msg['Date']}")

                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                body = part.get_payload(decode=True)
                                text = body.decode('utf-8')
                                growtopia_links = extract_growtopia_links(text)
                                for link in growtopia_links:
                                    last_link = link  
                                    print(f"Link: {link}")
                    else:
                        body = msg.get_payload(decode=True)
                        text = body.decode('utf-8')
                        growtopia_links = extract_growtopia_links(text)
                        for link in growtopia_links:
                            link = link.replace("</p>", '"')
                            last_link = link 
                            print(f"Link: {link}")

                    print("-" * 50)

            imap.logout()

            if last_link:
                link = link.replace('"', '')
                last_link = link 
                webbrowser.open(last_link)
            else:
                print(f"Tidak ada tautan yang ditemukan pada : {username}:{password}")
        except Exception as e:
            print(f"Terjadi kesalahan: {username}:{password}")