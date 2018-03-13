  
       <div class="item">
          <a data="" target="_blank" href="https://www.moglix.com/deals/emailer-deals">
            <img class="img-fluid h-315 h-auto-xs" src="https://cdnx1.moglix.com/cms/flyout/Images_2018-01-24_04-27-49_HP10025_22Jan_Safer_India.gif">
          </a>
         
        </div>


        <div class="item">
          <a data="" target="_blank" href="https://www.moglix.com/deals/wintersale">
            <img class="img-fluid h-315 h-auto-xs" src="https://cdnx1.moglix.com/cms/flyout/Images_2018-01-24_04-27-49_HP10024_24Jan_Live_At_Store.gif">
          </a>
         
        </div>

        <div class="item">
          <a data="" target="_blank" href="https://www.moglix.com/brands/metis">
            <img class="img-fluid h-315 h-auto-xs" src="https://cdnx1.moglix.com/cms/flyout/Images_2018-01-23_06-00-57_HP10023_weighingscales_platinum_banner-min.jpg">
          </a>
         
        </div>

       <div class="item">
          <a data="" target="_blank" href="https://www.moglix.com/deals">
            <img class="img-fluid h-315 h-auto-xs" src="https://cdnx1.moglix.com/cms/flyout/Images_2018-01-24_04-27-49_HP10011_22Jan_Exclisive_Deals.gif">
          </a>
         
        </div>

      <div class="item">
          <a data="" target="_blank" href="https://www.moglix.com/deals/made-in-india">
            <img class="img-fluid h-315 h-auto-xs" src="https://cdnx1.moglix.com/cms/flyout/Images_2018-01-24_04-27-49_HP10010_24Jan_MadeInIndia.jpg">
          </a>
         
        </div>




        function botmessage()
{
    setDate();
      updateScrollbar();
     $('<div class="message loading new"><figure class="avatar"><img src="/static/res/265668.svg" /></figure><span></span></div>').appendTo($('.mCSB_container'));
	$.post('/botmessage', {
	}).done(function(botmessage) {
            
	var splitreply = botmessage['text']
        alert(splitreply.length);
         setDate();
      updateScrollbar();
        $('.message.loading').remove();
         for(var i=0;i<splitreply.length;i++){
          alert(splitreply[i]);
        $('  <div id="idm" class="message new"><figure class="avatar"><img src="/static/res/265668.svg" /></figure>'+splitreply[i]+'</div>').appendTo($('.mCSB_container')).addClass('new');
       }
 setDate();
      updateScrollbar();
		}).fail(function() {
				alert('error calling function');
				});
}
 
<script type="text/javascript" language="JavaScript">
          botmessage();
      </script>


<audio controls autoplay><source src="static/upload/'+reply['path']+'" type="audio/mp3"></audio>
