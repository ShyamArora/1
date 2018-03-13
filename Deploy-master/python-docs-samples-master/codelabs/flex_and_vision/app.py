import math
from flask import Flask, render_template, request
from flask import jsonify
from werkzeug.utils import secure_filename
import lang_call
import os
import check_msg
import random
from gtts import gTTS
import speech_to_text
from nltk import word_tokenize
import time

messages=['fg','dg','dc']

app = Flask(__name__,static_url_path="/static") 
def refresh():
    app.run(host= '0.0.0.0',port =5001)

    messages=['fg','dg','dc']

language_=''
@app.route('/language', methods=['POST'])
def language():
    print("ascas")
    print(request.form['json_str'])
    #language_="English"
    language_ = request.form['json_str']
    print(language_)
    return "done"

@app.route('/uploadajax', methods=['POST'])
def upldfile():
    if request.method == 'POST':
        file = request.files['file']
        
        filename = secure_filename(file.filename)
        path ='static/upload/'
        
        file.save(os.path.join(path, filename))

        check_msg.add_attach(os.path.join(path, filename))
        return jsonify( { 'text': filename } ) 

    
@app.route('/speech', methods=['POST'])
def speech_():
    msg=speech_to_text.speech_to_text_()
    print("cd"+msg)
    return jsonify( { 'text': msg } )


            

@app.route('/message', methods=['POST'])
def reply():
    language_="English"
    msg1=request.form['msg']
    msg =lang_call.lan_to_eng(msg1,language_)
    classify_action_return =check_msg.classify_action(msg,messages[len(messages)-1],messages[len(messages)-2])
    
    if classify_action_return==False:
        classify_multiple_return=check_msg.check_multiple_option(msg,messages[len(messages)-1])

        if classify_multiple_return==False:
            classify_yes_or_no_in_option=check_msg.check_yes_or_no_in_option(msg,messages[len(messages)-1])
            if classify_yes_or_no_in_option==False:
                classify_yes_no_return=check_msg.check_yes_or_no(msg,messages[len(messages)-1])

                if classify_yes_no_return ==False:
                    classify_query_return=check_msg.classify_query_(msg)
                    if classify_query_return ==False:
                        classify_chatter_return=check_msg.check_chatterbot(msg)

                        if classify_chatter_return==False:
                            reply = "Sorry, Is this relevent? <br>I did not understand. Please give me more information"
                        else:
                            reply = classify_chatter_return
                    else:
                        reply = classify_query_return
                else:
                    reply = classify_yes_no_return
            else:
                reply = classify_yes_or_no_in_option

        else:
            reply = classify_multiple_return
    else:
        reply = classify_action_return

    messages.append(reply)
    if isinstance(reply, list):
        reply2=reply
        
##        path=text_to_speech(reply[0])
        
    else :
        s=''
        mystr = reply.split()
        for i in range(len(mystr)):
        
            substr = "http://"
            substrs = "https://"
            if substr in mystr[i] or substrs in mystr[i]:
                print(mystr[i])
                a_link=mystr[i]
                s+='<a target="_blank" href="'+reply+'" style="color: #B2DFDB">'+a_link+'</a>'
            else:
                s+=' '+mystr[i]
        reply = s        
        
        reply =lang_call.eng_to_lang(reply,language_)
##        path=text_to_speech(reply)
        reply2=reply 

##    return jsonify( { 'text': reply,'path': path } )
    return jsonify( { 'text': reply2 } )

@app.route('/botmessage', methods=['POST'])
def botmessage():
    reply2=[]
    time.sleep(4)
    print("adcdcsadcadcadcasda")
    reply2.append('New Deals')

    reply2.append('<a data="" target="_blank" href="https://www.moglix.com/deals/emailer-deals"><img class="img-fluid h-315 h-auto-xs" src="https://cdnx1.moglix.com/cms/flyout/Images_2018-01-24_04-27-49_HP10025_22Jan_Safer_India.gif" style=" max-width: 220px;max-height :120px;"></a>INDUSTRIAL SAFETY--Upto 80% Off')
    reply2.append('<a data="" target="_blank" href="https://www.moglix.com/deals/wintersale"><img class="img-fluid h-315 h-auto-xs" src="https://cdnx1.moglix.com/cms/flyout/Images_2018-01-24_04-27-49_HP10024_24Jan_Live_At_Store.gif" style=" max-width: 220px;max-height :120px;"></a>69 STORE--Explore Now')
    reply2.append('<a data="" target="_blank" href="https://www.moglix.com/brands/metis"> <img class="img-fluid h-315 h-auto-xs" src="https://cdnx1.moglix.com/cms/flyout/Images_2018-01-23_06-00-57_HP10023_weighingscales_platinum_banner-min.jpg" style=" max-width: 220px;max-height :120px;"></a>EXTRA 10% OFF--Weighing Scales')
    reply2.append('<a data="" target="_blank" href="https://www.moglix.com/deals"><img class="img-fluid h-315 h-auto-xs" src="https://cdnx1.moglix.com/cms/flyout/Images_2018-01-24_04-27-49_HP10011_22Jan_Exclisive_Deals.gif" style=" max-width: 220px;max-height :120px;"></a>REPUBLIC DAY SALE--Live Now')
    reply2.append('<a data="" target="_blank" href="https://www.moglix.com/deals/made-in-india"><img class="img-fluid h-315 h-auto-xs" src="https://cdnx1.moglix.com/cms/flyout/Images_2018-01-24_04-27-49_HP10010_24Jan_MadeInIndia.jpg" style=" max-width: 220px;max-height :120px;"></a>TOP INDIAN PRODUCTS--Shop Now')
    return jsonify( { 'text': reply2 } )



@app.route('/botmessage1', methods=['POST'])
def botmessage1():
    
    time.sleep(2)
    print("---------------88")
    return jsonify( { 'text': 'g' } )



def text_to_speech(value):
    sentence_words = word_tokenize(value)
    if len(sentence_words)>13:
        value="Message is big, So I have displayed it on the screen."    
    print(format(value).encode("utf-8"))
    tts = gTTS(value, lang='en')
    path = 'static/upload/'
    str1 =str(random.random())
    str2 = ".mp3"
    filename=str1+str2
    #filename = "audio.mp3"
##    <audio controls autoplay><source src="static/upload/'+reply['path']+'" type="audio/mp3"></audio>
    tts.save(os.path.join(path, filename))
    return filename 
  


@app.route("/")
def index():
    messages=['fg','dg','dc']
    
    return render_template("index.html",data="Hello I am Moglix, How can I help you?")


        
if (__name__ == "__main__"):
    app.run(host= '0.0.0.0',port =5058)
    
