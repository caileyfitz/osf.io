//////////////////
// Site-wide JS //
//////////////////
(function() {


var setStatus = function(status){
    $('#alert-container').append(status);//'<div class=\'alert-message warning fade in\' data-alert=\'alert\'><a class=\'close\' href=\'#\'>&times;</a><p>'+ status +'</p></div>');
};

var urlDecode = function(str) {
    return decodeURIComponent((str+'').replace(/\+/g, '%20'));
}


/**
 * Display a modal confirmation window before relocating to an url.
 * @param  <String> message
 * @param  <String> url
 */
var modalConfirm = function(message, url){
    bootbox.confirm(message,
        function(result) {
            if (result) {
                window.location.href = url;
            }
        }
    )
}

var urlDecode = function(str) {
    return decodeURIComponent((str+'').replace(/\+/g, '%20'));
}


/**
 * Display a modal confirmation window before relocating to an url.
 * @param  <String> message
 * @param  <String> url
 */
var modalConfirm = function(message, url){
    bootbox.confirm(message,
        function(result) {
            if (result) {
                window.location.href = url;
            }
        }
    )
}


$(document).ready(function(){
    // Highlight active tabs and nav labels
    $('.nav a[href="' + location.pathname + '"]').parent().addClass('active');
    $('.tabs a[href="' + location.pathname + '"]').parent().addClass('active');

    // Initiate tag input
    $('#tagitfy').tagit({
              availableTags: ["analysis", "methods", "introduction", "hypotheses"], // this param is of course optional. it's for autocomplete.
              // configure the name of the input field (will be submitted with form), default: item[tags]
              fieldName: 'tags',
              singleField: true
    });

    // Build tooltips on user activity widgets
    $('.ua-meter').tooltip();
    $("[rel=tooltip]").tooltip({
        placement:'bottom',
    });

    //  Initiate tag cloud (on search page)
    $.fn.tagcloud.defaults = {
      size: {start: 14, end: 18, unit: 'pt'},
      color: {start: '#cde', end: '#f52'}
    };

    $(function () {
      $('#whatever a').tagcloud();
    });



});

}).call(this);