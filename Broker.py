import requests
from flask import Flask, Response, request
from flask_cors import CORS
import time
import threading

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


# @app.route('/GetLeaderAddr',methods = ['POST'])
# def GetLeaderAddr():
#     leaderIP = getLeaderAddr()
#     return Response(str(leaderIP))


@app.route('/BrokerHeartBeat',methods=['POST'])
def BrokerHeartBeat():
    # time.sleep(2)
    recieved_data = request.data.decode()
    offset = recieved_data.strip().split("|")[0]
    leaderAddr = recieved_data.strip().split("|")[1]
    setLeaderAddr(leaderAddr)
    print(leaderAddr)
    print(offset.strip() != timeStamp.strip())
    if offset != timeStamp:
        leaderIP = getLeaderAddr()
        url = leaderIP+'/FetchSnapshot'
        r = requests.post(url=url,data=b'send MetaData')
        # print("requested for metadata")
    return Response("recieved meta data")

@app.route('/recieveSnapshot',methods=['POST'])
def recieveSnapshot():
    data = request.data.decode()
    data = data.strip().split(" ")[-2][1:]+" "+data.strip().split(" ")[-1][:-2]
    setTimeStamp(data)
    setMetaData(request.data.decode())
    return Response("Snapshot recieved")


def startServer():
    app.run(debug=False,port=6000,host='127.0.1.1')

server = threading.Thread(target=startServer)
server.start()

time.sleep(5)
# Create Broker Record 

# newBroker = b'{"brokerId":"2","brokerHost": "hello.com","brokerPort": "3000","securityProtocol": "HTTPS","rackId": "12"}'
# createBrokerUrl = str(getLeaderAddr())+'/createBrokerFromClient'
# res = requests.post(url=createBrokerUrl,data=newBroker)

# print("-------------------------------->",res.content.decode())

# Create Topic Record
# newTopic =  b'{"name": "share"}'
# createTopicUrl =str(getLeaderAddr())+'/createTopicFromClient'
# res = requests.post(url=createTopicUrl,data=newTopic)

# print("-------------------------------->",res.content.decode())


# Create Partitions Record 
newPartiton =  b'{"partitionId": "0", "topicUUID": "",  "replicas": [], "ISR": [], "removingReplicas": [], "addingReplicas": [],"leader": "", "partitionEpoch": "0" }'
createpartitionUrl =str(getLeaderAddr())+'/createPartitionFromClient'
res = requests.post(url=createpartitionUrl,data=newPartiton)




server.join()
