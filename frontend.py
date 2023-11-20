import threading
import requests
from time import sleep
leaderAddr = ''
import json 


def setLeader(leader):
    global leaderAddr
    leaderAddr = leader
    return leaderAddr

def getLeader():
    global leaderAddr
    return leaderAddr
def getleader():
    while True:
        sleep(1)
        # print("called")
        try:
            pass
            url = 'http://127.0.1.1:6000/GetLeaderAddr'
            data = b'get leader address'
            r = requests.post(url=url,data=data)
            # setLeader(r)
            # print(r.content.decode())
            data = b'{"name": "share"}'
            setLeader(r.content.decode())
            
            
            
            # print(r.content.decode())
            try:
                r = requests.post(url=url,data=data)
            except:
                print("not able to make request")
            
        except:
            print("not able to fetch leader")

thread1 = threading.Thread(target=getleader)
thread1.start()

createBrokerUrl = str(getLeader())+'/createBrokerFromClient'
createTopicUrl =str(getLeader())+'/createTopicFromClient'
createpartitionUrl =str( getLeader())+'/createPartitionFromClient'
createproducerUrl =str(getLeader())+'/createProducerFromClient'

getAllActiveBrokers = str(getLeader())+'/GetAllActiveBrokers'
getBrokerById =str(getLeader())+'/GetBrokerById'
getTopicBYId =str(getLeader())+'/GetTopicBYId'
       


sleep(2)
leader = getLeader()         
print("---------------------------------",leader,"------------------------------------------")       
    
            # try:
            #     r = requests.post(url=url,data=data)
            # except:
            #     print("not able to make request")
import streamlit as st
# st.title("BD Project")

def display_broker():

    b1 = st.text_input("BrokerId","2")
    b2 = st.text_input("brokerHost","hello.com")
    b3 = st.text_input("brokerPort","3000")
    b4 = st.text_input("securityProtocol","HTTPS")
    b5 = st.text_input("rackId","12")
    btn4= st.button("Submit")
    # data = "{"+"brokerId"+":"+2+","+"brokerHost"+": "+"hello.com"+","+"brokerPort": "3000","securityProtocol": "HTTPS","rackId": "12"}'
    data = {"brokerId":b1,"brokerHost": b2,"brokerPort": b3,"securityProtocol": b4,"rackId": b5}
    # data = str(data)
    data = json.dumps(data)
    if btn4:
        print("called")
        # try:
        leader = getLeader()
        print(leader)
        createBrokerUrl = str(leader)+'/createBrokerFromClient'
        r = requests.post(createBrokerUrl,bytes(data,'ascii'))
        # except:
            # print("not able to send")
# def display_partition():

    

# def display_topic():

 

def display_producer():

    a1 = st.text_input("BrokerId")
    a2 = st.text_input("producerId","hello.com")
    btn3= st.button("Submit")
    # a3 = st.text_input("brokerPort","3000")
    # a4 = st.text_input("securityProtocol","HTTPS")
    # a5 = st.text_input("rackId","12")

st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", ("Create", "Read","Delete","b4","b5","b6"))

if selected_page == "Create":
    st.title("Create")
    selected_options = st.selectbox("",("createBroker","createPartition","createTopic","createProducer"),index=None,placeholder="Select Catagory")
        # selected_options = st.selectbox("Select options",options)
    if selected_options == "createBroker":
        display_broker()
    if selected_options =="createTopic":
            b1 = st.text_input("name","abc")
            btn2= st.button("Submit")
            # b2 = st.text_input("brokerHost","hello.com")
            # b3 = st.text_input("brokerPort","3000")
            # b4 = st.text_input("securityProtocol","HTTPS")
            # b5 = st.text_input("rackId","12")
    elif selected_options=="createPartition":

        b1 = st.text_input("partitionId")
        b2 = st.text_input("replicas")
        b3 = st.text_input("ISR")
        b4 = st.text_input("removingReplicas")
        b5 = st.text_input("addingReplicas")
        b5 = st.text_input("leader")
        b5 = st.text_input("partitionEpoch")
        btn1= st.button("Submit")

    elif selected_options=="createProducer":
            display_producer()
        
if selected_page == "Read":
    st.title("Retrive")
    selected_options = st.selectbox("",("Get_All_Active_Brokers","Get_Brokers_by_ID","Get_Topic_by_Name"),index=None,placeholder="Select Catagory")
    if selected_options == "Get_All_Active_Brokers":
        activeBrokers= st.button("Get_all_Active_Brokers")
    if selected_options == "Get_Brokers_by_ID":
        broker_ID= st.text_input("Enter broker ID")
    if selected_options == "Get_Brokers_by_ID":
        broker_ID= st.text_input("Enter broker ID")
    if selected_options == "Get_Topic_by_Name":
        broker_ID= st.text_input("Enter Topic Name")

#

thread1.join()