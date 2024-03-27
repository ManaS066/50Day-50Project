import requests
from datetime import datetime
USERNAME="manas001"
TOKEN ="manas2004"
pixela_end ="https://pixe.la/v1/users"
para = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# already created the acount once
# response = requests.post(pixela_end,json=para)
# print(response.text)

graph_end = f"{pixela_end}/{USERNAME}/graphs"

graph_config ={
    "id":"graph2",
    "name":"my coading graph",
    "unit":"hour",
    "type":"float",
    "color":"sora"
}

headers = {
    "X-USER-TOKEN":TOKEN
}
#response = requests.post(url=graph_end,json=graph_config,headers=headers)

x= datetime.today()
date = x.strftime("%Y%m%d")
header1 = {
    "X-USER-TOKEN":TOKEN
}
update_end = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph2"
def insert():
    quanti = input("enter number of hour")
    update_config = {
        "date": date,
        "quantity": quanti
    }

    response_update = requests.post(update_end,json=update_config,headers=header1)
    print(response_update.text)


insert_end = f"{update_end}/{date}"


def update():
    qty = input("enter hour to modify the previous value")
    config = {
        "quantity": qty
    }
    response = requests.put(url=insert_end,json=config,headers=header1)

    print(response.text)

def delete():
    del_response = requests.delete(url=insert_end,headers=header1)
    print(del_response.text)

x= input("Enter 'insert' for insert today working value \n Enter 'update' for update the exiting value \n Enter 'delete' for delete todays progress").lower()
if x=="insert":
    insert()
elif x=="update":
    update()
elif x=="delete":
    delete()