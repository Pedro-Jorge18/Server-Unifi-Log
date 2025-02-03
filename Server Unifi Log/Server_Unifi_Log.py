import datetime
from datetime import datetime, date, timedelta
import time
import json
from unificontrol import UnifiClient #install the unificontrol module

client = UnifiClient(
    host="....", #host of the controller
    username="....", #username of the controller
    password="....", #password of the controller
    )

def safeGet(m, key): #function to get the value of the key
    try:
        return m[key]
    except:
        return ''

def main(): #main function
    devices = client.list_devices()

    # create file with the correct date
    time_change = timedelta(hours=2)
    date = datetime.today().strftime('%Y-%m-%d')
    f = open("log_ubiquiti_" + date , "w")

    # write the data to the file
    for device in devices:    
        f.write(safeGet(device, 'name') + '\n')  
        f.write("    model: " + safeGet(device,'model') + '\n')
        f.write("    ip: " + safeGet(device,'ip') + '\n')
        f.write("    mac: " + safeGet(device,'mac') + '\n')
        uptime = safeGet(device,'_uptime')
        if uptime != '':
            f.write(f"    uptime: {round((float(uptime) / 60 / 60 / 24), 1)} days")
        f.write("    version: " + safeGet(device,'version') + '\n')
        f.write("    required_version: " + safeGet(device,'required_version') + '\n')
        connectedAt = safeGet(device, 'connected_at')
        if connectedAt != '':
            f.write("    connected_at: " + datetime.utcfromtimestamp(connectedAt) + '\n')
        if 'gateway_mac' in device:
            f.write("    gateway_mac: " + device['gateway_mac'] + '\n')

    # Added json.dumps() to properly format the data as JSON

    f.write("----------------------Network Health-----------------------------------------")

    health = client.list_health()                 #health of the network
    f.write(json.dumps(health, indent=4))

    f.write("----------------------Network List-------------------------------------------")

    listnetwork = client.list_networkconf(network_id=None) #you can change the network id up to choice#
    f.write(json.dumps(listnetwork, indent=4))

    f.write("----------------Rogue AP-----------------------------------------------------")

    rogueap = client.list_rogueaps(within=24)
    f.write(json.dumps(rogueap, indent=4))     #rogue ap

    f.write("------------------------Client Status ---------------------------------------")

    statusserver = client.stat_status()
    f.write(json.dumps(statusserver, indent=4))    #status of the server

    f.write("-----------------------Server Events-----------------------------------------")

    eventsserver = client.list_events(historyhours=720, start=0, limit=1000)
    f.write(json.dumps(eventsserver, indent=4))                                      #events of the server

    f.write("------------------------Wlan Config------------------------------------------")

    wlanconf = client.list_wlanconf(wlan_id=None)
    f.write(json.dumps(wlanconf, indent=4))           #wlan configuration
    
    # close file 
    f.close()


    # upload the file to the server
if __name__ == '__main__':
    while True:
        main()
        time.sleep(30) #time to wait
