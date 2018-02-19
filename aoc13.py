def check_severity(data):
    lines=data.split('\n')[:-1]
    layers={}
    for line in lines:
        key,value=line.split(': ')
        layers[int(key)]=int(value)
#    layers[0]=3
#    layers[1]=2
#    layers[4]=4
#    layers[6]=4
    #start from picosecond 0
    severity=None
    position=0
    delay=0
    flag=0
    while(flag!=1):
        severity=0
        delay+=1
        for position in range(max(layers)+1):
            time=position+delay
            if position in layers:
                if(time%((layers[position]-1)*2)==0):
                    severity+=position*layers[position]
                    break
        else:
            flag=1
    return delay
            
        

def main():
    with open('input13','r') as file:
        data=file.read()
        severity=check_severity(data)
        print(severity)

if __name__=='__main__':
    main()
