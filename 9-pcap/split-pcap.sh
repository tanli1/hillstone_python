#!/bin/bash
find / -name 'ltan.pcap' > pcapfilename.txt

while read LINE
	do
		 echo $LINE
		 temp=${LINE%.*}
		 filedic=""${temp}
		 echo $filedic
		 mkdir -p $filedic
		 #if ($2>=0)消除首行的空格， > 每次覆盖前一次的内容
		 tshark -r $LINE -T fields -e tcp.stream |sort -n | uniq -c | awk -F ' ' '{if ($2>=0)print $2 }' > tcp_stream_number.txt
		 while read tcpnumber
			do 
			#sed替换空格为下划线，tcp.flags，tcp.ack取首包的名称，$(($tcpnumber))，字符串转数字
			streamname=`tshark -r $LINE -Y "tcp.stream eq $(($tcpnumber)) and (tcp.flags & 0x02)and !(tcp.ack & 0xFFFFFFFF)" -T fields -e tcp.stream -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e ip.proto | sed s/[[:space:]]/_/g`
			#判断变量是否为空
			if [ ! $streamname ]
			then
				echo "IS NULL"
			else
				echo 'streamname' $streamname
                echo 'LINE ' $LINE
                echo 'tcpnumber ' $tcpnumber
                echo 'filedic ' $filedic
				tshark -r $LINE -Y "tcp.stream eq $(($tcpnumber))" -w $filedic/$streamname.pcap
			fi
		done < tcp_stream_number.txt
done < pcapfilename.txt 
