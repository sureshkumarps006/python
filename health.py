from yangcli.yangcli import yangcli
from lxml import etree
import yangrpc
import subprocess
import sys
import os
import paramiko


                
deviceip = str(subprocess.check_output(" hostname -I | awk '{print $1}'", shell=True), 'utf-8')

deviceip = "netconf-subscription-test netconf:"+deviceip.partition('\n')[0]+":830"
print(deviceip)

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='10.10.110.52', username='karaf',password='karaf', port=8101)
stdin,stdout,stderr=ssh_client.exec_command(deviceip)
output = stdout.readlines()
for items in output:
    print(items)

ssh_client.close()





conn = yangrpc.connect("10.10.12.4", 830, "niab400", "root123","/root/.ssh/id_rsa","/root/.ssh/id_rsa.pub")
#conn = yangrpc.connect("10.10.19.30", 830, "amantya", "root123","/root/.ssh/id_rsa","/root/.ssh/id_rsa.pub")
#conn = yangrpc.connect("10.10.19.71", 830, "amantya", "root123","/root/.ssh/id_rsa","/root/.ssh/id_rsa.pub")
#conn = yangrpc.connect("10.10.110.53", 830, "amantya", "root123","/root/.ssh/id_rsa","/root/.ssh/id_rsa.pub")

if(conn==None):
        print("Error: yangrpc failed to connect!")
        sys.exit(1)


yangcli(conn,"load Amantya-NIAB-5gsacore")
statechangedupf = "False"
statechangedamf = "False"
statechangedsmf = "False"
statechangednrf = "False"
statechangedausf = "False"
statechangednssf = "False"
statechangednef = "False"
statechangedpcf = "False"
statechangedaf = "False"
statechangedbsf = "False"
statechangedudm = "False"


while 1>0:
        try:
        
                response = str(subprocess.check_output(" sudo docker ps --filter 'ancestor=upf'  --format '{{.Status}}'", shell=True))
                #print(response)   
                if(statechangedupf != response):
                        if ("Up" in response and "Up" not in statechangedupf):
                                yangcli(conn, "alarms impactedEntity='upf' changedState='active' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='WARNING' description='UPF Container is UP'  clearAlarm='true' alarmType='Software Alarms'")
                                print("upf is active")
                                print(response)
                        elif ("Up" not in response):
                                yangcli(conn,"alarms impactedEntity='upf' changedState='inactive' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='UPF Container is DOWN'  clearAlarm='true' alarmType='Software Alarms'")
                                print("upf is inactive")
                                print(response)
                statechangedupf = response
        except:
                yangcli(conn,"alarms impactedEntity='upf' changedState='error' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='UPF Container has ERROR'  clearAlarm='true' alarmType='Software Alarms'")
                print("error in upf ")
        
        


        try:
                response = str(subprocess.check_output(" sudo docker ps --filter 'ancestor=amf'  --format '{{.Status}}'", shell=True))
                
                if(statechangedamf != response):
                        if ("Up" in response and "Up" not in statechangedamf):
                                yangcli(conn,"alarms impactedEntity='amf' changedState='active' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='WARNING' description='AMF Container is UP'  clearAlarm='true' alarmType='Software Alarms'")
                                print("amf is active")
                                print(response)
                        elif ("Up" not in response):
                                yangcli(conn,"alarms impactedEntity='amf' changedState='inactive' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='AMF Container is DOWN'  clearAlarm='true' alarmType='Software Alarms'")
                                print("amf is inactive")
                                print(response)
                                
                statechangedamf = response
        except:
                yangcli(conn,"alarms impactedEntity='amf' changedState='error' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='AMF Container has ERROR'  clearAlarm='true' alarmType='Software Alarms'")
                print("error in amf ")
        



        try:
                response = str(subprocess.check_output(" sudo docker ps --filter 'ancestor=smf'  --format '{{.Status}}'", shell=True))
                
                if(statechangedsmf != response):
                        if ("Up" in response and "Up" not in statechangedsmf):
                                yangcli(conn,"alarms impactedEntity='smf' changedState='active' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='WARNING' description='SMF Container is UP'  clearAlarm='true' alarmType='Software Alarms'")
                                print("smf is active")
                                print(response)
                        
                        elif ("Up" not in response):
                                yangcli(conn,"alarms impactedEntity='smf' changedState='inactive' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='SMF Container is DOWN'  clearAlarm='true' alarmType='Software Alarms'")
                                print("smf is inactive")
                                print(response)
                                
                statechangedsmf = response
        
        except:
                yangcli(conn,"alarms impactedEntity='smf' changedState='error' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='SMF Container has ERROR'  clearAlarm='true' alarmType='Software Alarms'")
                print("error in smf ")


        



        try:
                response = str(subprocess.check_output(" sudo docker ps --filter 'ancestor=nrf'  --format '{{.Status}}'", shell=True))
                
                if(statechangednrf != response):
                        if ("Up" in response and "Up" not in statechangednrf):
                                yangcli(conn,"alarms impactedEntity='nrf' changedState='active' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='WARNING' description='NRF Container is UP'  clearAlarm='true' alarmType='Software Alarms'")
                                print("nrf is active")
                                print(response)
                        elif ("Up" not in response):
                                yangcli(conn,"alarms impactedEntity='nrf' changedState='inactive' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='NRF Container is DOWN'  clearAlarm='true' alarmType='Software Alarms'")
                                print("nrf is inactive")
                                print(response)
                statechangednrf = response
        except:
                yangcli(conn,"alarms impactedEntity='nrf' changedState='error' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='NRF Container has ERROR'  clearAlarm='true' alarmType='Software Alarms'")
                print("error in nrf ")


        


        try:
                response = str(subprocess.check_output(" sudo docker ps --filter 'ancestor=ausf'  --format '{{.Status}}'", shell=True))
                
                if(statechangedausf != response):
                        if ("Up" in response and "Up" not in statechangedausf):
                                yangcli(conn,"alarms impactedEntity='ausf' changedState='active' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='WARNING' description='AUSF Container is UP'  clearAlarm='true' alarmType='Software Alarms'")
                                print("ausf is active")
                                print(response)
                        elif ("Up" not in response):
                                yangcli(conn,"alarms impactedEntity='ausf' changedState='inactive' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='AUSF Container is DOWN'  clearAlarm='true' alarmType='Software Alarms'")
                                print("ausf is inactive")
                                print(response)
                                
                statechangedausf = response
        except:
                yangcli(conn,"alarms impactedEntity='ausf' changedState='error' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='AUSF Container has ERROR'  clearAlarm='true' alarmType='Software Alarms'")
                print("error in ausf ")



        

        try:
                response = str(subprocess.check_output(" sudo docker ps --filter 'ancestor=nssf'  --format '{{.Status}}'", shell=True))
                
                if(statechangednssf != response):
                        if ("Up" in response and "Up" not in statechangednssf):
                                yangcli(conn,"alarms impactedEntity='nssf' changedState='active' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='WARNING' description='NSSF Container is UP'  clearAlarm='true' alarmType='Software Alarms'")
                                print("nssf is active")
                                print(response)
                        elif ("Up" not in response):
                                yangcli(conn,"alarms impactedEntity='nssf' changedState='inactive' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='NSSF Container is DOWN'  clearAlarm='true' alarmType='Software Alarms'")
                                print("nssf is inactive")
                                print(response)
                statechangednssf = response

        except:
                yangcli(conn,"alarms impactedEntity='nssf' changedState='error' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='NSSF Container has ERROR'  clearAlarm='true' alarmType='Software Alarms'")
                print("error in nssf ")



        


        try:
                response = str(subprocess.check_output(" sudo docker ps --filter 'ancestor=nef'  --format '{{.Status}}'", shell=True))
                
                if(statechangednef != response):
                        if ("Up" in response and "Up" not in statechangednef):
                                yangcli(conn,"alarms impactedEntity='nef' changedState='active' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='WARNING' description='NEF Container is UP'  clearAlarm='true' alarmType='Software Alarms'")
                                print("nef is active")
                                print(response)
                        elif ("Up" not in response):
                                yangcli(conn,"alarms impactedEntity='nef' changedState='inactive' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='NEF Container is DOWN'  clearAlarm='true' alarmType='Software Alarms'")
                                print("nef is inactive")
                                print(response)
                statechangednef = response
                
        except:
                yangcli(conn,"alarms impactedEntity='nef' changedState='error' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='NEF Container has ERROR'  clearAlarm='true' alarmType='Software Alarms'")
                print("error in nef ")



        



        try:
                response = str(subprocess.check_output(" sudo docker ps --filter 'ancestor=pcf'  --format '{{.Status}}'", shell=True))
                
                if(statechangedpcf != response):
                        
                        if ("Up" in response and "Up" not in statechangedpcf):
                                yangcli(conn,"alarms impactedEntity='pcf' changedState='active' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='WARNING' description='PCF Container is UP'  clearAlarm='true' alarmType='Software Alarms'")
                                print("pcf is active")
                                print(response)
                        elif ("Up" not in response):
                                yangcli(conn,"alarms impactedEntity='pcf' changedState='inactive' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='PCF Container is DOWN'  clearAlarm='true' alarmType='Software Alarms'")
                                print("pcf is inactive")
                                print(response)
                
                statechangedpcf = response
        except:
                yangcli(conn,"alarms impactedEntity='pcf' changedState='error' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='PCF Container has ERROR'  clearAlarm='true' alarmType='Software Alarms'")
                print("error in pcf ")



        

        try:
                response = str(subprocess.check_output(" sudo docker ps --filter 'ancestor=af'  --format '{{.Status}}'", shell=True))
                
                if(statechangedaf != response):
                        if ("Up" in response and "Up" not in statechangedaf):
                                yangcli(conn,"alarms impactedEntity='af' changedState='active' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='WARNING' description='AF Container is UP'  clearAlarm='true' alarmType='Software Alarms'")
                                print("af is active")
                                print(response)
                        elif ("Up" not in response):
                                yangcli(conn,"alarms impactedEntity='af' changedState='inactive' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='AF Container is DOWN'  clearAlarm='true' alarmType='Software Alarms'")
                                print("af is inactive")
                                print(response)
                                
                statechangedaf = response
        
        except:
                yangcli(conn,"alarms impactedEntity='af' changedState='error' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='AF Container has ERROR'  clearAlarm='true' alarmType='Software Alarms'")
                print("error in af ")




        
        try:
                response = str(subprocess.check_output(" sudo docker ps --filter 'ancestor=bsf'  --format '{{.Status}}'", shell=True))
                
                if(statechangedbsf != response):
                        if ("Up" in response and "Up" not in statechangedbsf):
                                yangcli(conn,"alarms impactedEntity='bsf' changedState='active' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='WARNING' description='BSF Container is UP'  clearAlarm='true' alarmType='Software Alarms'")
                                print("bsf is active")
                                print(response)
                        elif ("Up" not in response):
                                yangcli(conn,"alarms impactedEntity='bsf' changedState='inactive' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='BSF Container is DOWN'  clearAlarm='true' alarmType='Software Alarms'")
                                print("bsf is inactive")
                                print(response)
                        
                statechangedbsf = response
                
        except:
                yangcli(conn,"alarms impactedEntity='bsf' changedState='error' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='BSF Container has ERROR'  clearAlarm='true' alarmType='Software Alarms'")
                print("error in bsf ")





        
        try:
                response = str(subprocess.check_output(" sudo docker ps --filter 'ancestor=udm'  --format '{{.Status}}'", shell=True))
                
                if(statechangedudm != response):
                        if ("Up" in response and "Up" not in statechangedudm):
                                yangcli(conn,"alarms impactedEntity='udm' changedState='active' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='WARNING' description='UDM Container is UP'  clearAlarm='true' alarmType='Software Alarms'")
                                print("udm is active")
                                print(response)
                        elif ("Up" not in response):
                                yangcli(conn,"alarms impactedEntity='udm' changedState='inactive' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='UDM Container is DOWN'  clearAlarm='true' alarmType='Software Alarms'")
                                print("udm is inactive")
                                print(response)
                                
                statechangedudm = response
        
        except:
                yangcli(conn,"alarms impactedEntity='udm' changedState='error' alarmSource='port:830' timeRaised='13-01-23 18:52:20' severity='CRITICAL' description='UDM Container has ERROR'  clearAlarm='true' alarmType='Software Alarms'")
                print("error in udm ")




