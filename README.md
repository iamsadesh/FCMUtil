# FCMUtil
Utility CLI script to send FCM/GCM notifications to the Android devices. This will be handy if you want to test how your app behaves for various push notifications of your App.

This script is a simple python script. So, having Python installed in your system is a prerequisite. This script can be called from the command line like this. 

### python send_pn.py "Title" "Message Body" fcm_tokens.txt 

The first and second argument are the title and body of the push notification based on the payload that I have provided in the python script which is the "data" part within the data field. Feel free to modify that according to your needs. The last argument is the file name which contains the FCM/GCM tokens separated by newline char. 

Note that FCM is backward compatible, hence the same script can be used to test the PN via GCM as well. 
