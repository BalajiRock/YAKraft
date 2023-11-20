import requests
from flask import Flask, Response, request
from flask_cors import CORS
import time

leader_addr = ''
def getLeaderAddr():
    global leader_addr
    return leader_addr

def setLeaderAddr(addr):
    global leader_addr
    leader_addr = addr
    return leader_addr


Metadata =''
timeStamp = ''

def setTimeStamp(currentTimeStamp):
    global timeStamp 
    timeStamp = currentTimeStamp
    return timeStamp

    
def setMetaData(currData):
    global Metadata
    Metadata = currData
    return Metadata

app = Flask(__name__)
CORS(app)


@app.route('/GetLeaderAddr',methods = ['POST'])
def GetLeaderAddr():
    leaderIP = getLeaderAddr()
    return Response(str(leaderIP))


@app.route('/BrokerHeartBeat',methods=['POST'])
def BrokerHeartBeat():
    time.sleep(2)
    # print(request.data.decode())
    recieved_data = request.data.decode()
    offset = recieved_data.strip().split("|")[0]
    leaderAddr = recieved_data.strip().split("|")[1]
    setLeaderAddr(leaderAddr)
    # print("1111111111111111111",offset,"=================",timeStamp,"111111111111111111111")
    print(offset.strip() != timeStamp.strip())
    if offset != timeStamp:
        leaderIP = getLeaderAddr()
        url = leaderIP+'/FetchSnapshot'
        
        r = requests.post(url=url,data=b'send MetaData')
        print("requested for metadata")
        
    # print("-------------------------------------------->>",Metadata)
    
    
    return Response("recieved meta data")

@app.route('/recieveSnapshot',methods=['POST'])
def recieveSnapshot():
    data = request.data.decode()
    data = data.strip().split(" ")[-2][1:]+" "+data.strip().split(" ")[-1][:-2]
    setTimeStamp(data)
    setMetaData(request.data.decode())

    # print("---------------------------------------",request.data.decode(),"--------------------------------------------")

    return Response("Snapshot recieved")







app.run(debug=False,port=6000,host='127.0.1.1')