from datetime import datetime
from scapy.all import sniff, TCP, wrpcap

'''
    Log any errors that occur in the program
    @param error: Error that occured during runtime.
'''
def Log(error):
    t_stamp = datetime.today().strftime('%m/%d/%Y %H:%M:%S')
    
    with open('ErrorLog.log', 'a+') as log:
        msg = ''.join([t_stamp, '-' * 20, '\n', error, '\n\n'])
        log.write(msg)
    
        

'''
    Search for traffic to / from the Alarm panel
'''
def handle_packet(pkt):
    if pkt.haslayer(TCP) and (pkt[0][1].dst == '192.168.1.13' or pkt[0][1].src == '192.168.1.13'):
        try:
            wrpcap('captured.pcap', pkt, append=True)
        except Exception as error:
            Log(error)Alam
        


'''
    Starting point of the program
'''
def main():
    sniff(prn = handle_packet)


main()
