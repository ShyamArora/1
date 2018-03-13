var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

$(window).load(function() {
  $messages.mCustomScrollbar();
  setTimeout(function() {
    //fakeMessage();
  }, 100);
});

function updateScrollbar() {
    
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function setDate(){
     
  d = new Date();
 /*  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
	
	
	
  }  */
    $('<div class="timestamp">' + d.getHours() + ':' + d.getMinutes() + '</div>').appendTo($('.message:last'));
	
}

function insertMessage(option) {
  msg = $('.message-input').val();
 
if (option==0||option==1||option==2||option==3||option==4||option==5){
   var option_ =option+1;
 $('<div class="message message-personal">Selected Option - ' + option_ + '</div>').appendTo($('.mCSB_container')).addClass('new');
     setDate();
  $('.message-input').val(null);
  updateScrollbar();
	interact(option);
 }
  if (option==10) {
      $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  $('.message-input').val(null);
  updateScrollbar();
	interact(msg);
  setTimeout(function() {
    //fakeMessage();
  }, 1000 + (Math.random() * 20) * 100);

    
  }

}
$('.message-submit').click(function() {
    var option =10; 
    insertMessage(option);
   
});

function option0(option) {
    


  insertMessage(option);
        
    }

function option1(option) {
      

  insertMessage(option);
        
    }
function option2(option) {
    

  insertMessage(option);
        
    }
function option3(option) {
      
  insertMessage(option);
        
    }
function option4(option) {
  

  insertMessage(option);
        
    }



$('.message-speech').click(function() {
   document.getElementById("myNav").style.height = "100%";
 $.post('/speech', {
      
	}).done(function(speech_) {
	document.getElementById("myNav").style.height = "0%";	
    $('.message-input').val(speech_['text']) ;
   
    }).fail(function() {
alert('e speak agaaxs  fail in') ;
});
});


$(window).on('keydown', function(e) {
  if (e.which == 13) {
     var option =10; 
    insertMessage(option);
    return false;
  }
})


function interact(message){
	// loading message
   $('<div class="message loading new"><figure class="avatar"><img src="/static/res/265668.svg" /></figure><span></span></div>').appendTo($('.mCSB_container'));
	// make a POST request [ajax call]
	$.post('/message', {
		msg: message,
	}).done(function(reply) {
		// Message Received
                
                var splitreply = reply['text']
                 if(splitreply.length<6){
       
       $('.message.loading').remove();
$('<div class="message new"><figure class="avatar"><img src="/static/res/265668.svg" /></figure>Select from below options?</div>').appendTo($('.mCSB_container')).addClass('new');
     
        for(var i=0;i<splitreply.length;i++){
        
      var a=i+1;
            $('<div class="message new1"  onmouseover="hovers(this)"><figure class="avatar" style="width:0px;height:0px;border:0;"><img src="/static/res/265668.svg" /></figure><button type="submit" onclick="option'+i+'('+i+')" class="message-option'+i+'">('+a+'). '+splitreply[i]+ '</button></div>').appendTo($('.mCSB_container')).addClass('new');
          setDate();
    updateScrollbar(); 
    setDate();
    updateScrollbar();
  }
setDate();
    updateScrollbar();
    }else{
          $('.message.loading').delay(5000);
		// 	remove loading meassage
    $('.message.loading').remove();
    //giving options to chose

		// Add message to chatbox
               
    $('<div class="message new" ><figure class="avatar"><img src="/static/res/265668.svg" /></figure>' + reply['text'] + '</div>').appendTo($('.mCSB_container')).addClass('new');
    
    setDate();
    updateScrollbar();}
setDate();
    updateScrollbar();
		}).fail(function() {
				alert('error calling function');
				});
}




function botmessage(){ 

   
    $.post('/botmessage1', {
                
	}).done(function(botmessage1) {
      $('<div class="message loading new"><figure class="avatar"><img src="/static/res/265668.svg" /></figure><span></span></div>').appendTo($('.mCSB_container'));

		}).fail(function() {
				alert('error calling function');
				});
    	$.post('/botmessage', {
                
	}).done(function(botmessage) {
            
	var splitreply = botmessage['text']

   $('.message.loading').remove();
  
     for(var i=0;i<splitreply.length;i++){
      
        $('<div id="idm" class="message new"><figure class="avatar"><img src="/static/res/265668.svg" /></figure>'+splitreply[i]+'</div>').appendTo($('.mCSB_container')).addClass('new');
       } 
 setDate();
      updateScrollbar();
		}).fail(function() {
				alert('error calling function');
				});


}

botmessage();



