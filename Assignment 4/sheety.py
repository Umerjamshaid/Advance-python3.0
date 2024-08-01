import requests
import smtplib

SHEETY_API_URL = "https://api.sheety.co/347a860d7c6079a6e6250616420962dc/ufc4/sheet1"

# Fetch all fighters
def fetch_figthers():
    response = requests.get(SHEETY_API_URL)
    if response.status_code == 200:
        return response.json.get('sheety1, []')
    else :
        print("failed to fetch figthers info, please try again", response.text)
        return []
    
def uptade_eligibility_email(to_address, fighter):
    from_address = "umerjamshaid481@gmail.com"
    password = "kver lyyy irkg eqiz"
    subject = f"Eligibility notifications for {fighter['name']}"
    body = f"Dear {fighter['name']} , \n\nyou are cruntly eligilibile to enter in the {fighter['weightClass']} division"
    massage =f"subject: {subject}\n\n{body}"

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_address,password)
        server.sendmail(from_address, to_address, massage)
        print(f"Eligibility email sent to {to_address} for {fighter['name']}")

def update_eligibility(fighter_id, eligibility):
    url = f"{SHEETY_API_URL}/{fighter_id}"
    data = {
        "sheet1": {
            "Eligibility": eligibility
        }
    }
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print(f"Updated eligibility of fighter ID {fighter_id} to {eligibility}")
    else:
        print(f"Failed to update eligibility of fighter ID {fighter_id}:", response.text)

if __name__ == "__main__":
    fighters = fetch_figthers()
    for fighter in fighters:
        if fighter['age'] >= 18:
            send_eligibility_email(fighter['email'], fighter) 
            update_eligibility(fighter['id'], "yes")
        else:
            update_eligibility(fighter['id'], "no")


