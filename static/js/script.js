$(function () {
     $(window).on('load', function () {
        $('p.post-content').linkify();
    });
    
        
    rate_up();
    rate_down();
    delete_post();
});

function intial_rating()
{
    
    var rating_up = parseInt($("#tbl-rating").find('td[data-name="rating-up"] b').html()); 
    var rating_down = parseInt($("#tbl-rating").find('td[data-name="rating-down"] b').html());
    var total_rating_td = $("#tbl-rating").find('td[data-name="total-rating"] b');
    
    var total_rating = rating_up - rating_down;
    total_rating_td.html(total_rating);
}

function rate_up() {
    $('.glyphicon-chevron-up').click(function () {   
        $(this).preventDefault = true;
        
        var rate_dialog = $('#rate_dialog');
        if(rate_dialog.val() != null)
        {
            rate_dialog.modal('show');
            return 0;
        }

        var next_url = $(this).parent().find('input[name="next"]').val();
        var csrfmiddlewaretoken = $(this).parent().find('input[name="csrfmiddlewaretoken"]').val();
        var post_id = $(this).attr('data-postid');
        
        var rating_div = $(this).parents("#tbl-rating").find('td[data-name="rating-up"] b');
        var rating_up = parseInt($(this).parents("#tbl-rating").find('td[data-name="rating-up"] b').html()); 
        var rating_down = parseInt($(this).parents("#tbl-rating").find('td[data-name="rating-down"] b').html());
        var total_rating_td = $(this).parents("#tbl-rating").find('td[data-name="total-rating"] b');
       
        $.ajax({
            "type": "POST",
            "url": "/rate_up/",
            "data": {
                "post_id": post_id,
                "csrfmiddlewaretoken": csrfmiddlewaretoken,
                "next": next_url
            },

            "beforeSend": function (xhr, settings) {
                $.ajaxSettings.beforeSend(xhr, settings);
            }
        }).success(function (data) {
            rating_div.hide().fadeIn();
            if (data == "success") {
                rating_up++;
                rating_div.html(rating_up);
            }
            var total_rating = rating_up - rating_down;
            total_rating_td.hide().fadeIn();
            total_rating_td.html(total_rating);
        });
    });
}

function rate_down() {
    $('.glyphicon-chevron-down').click(function () {
        $(this).preventDefault = true;
        
        var rate_dialog = $('#rate_dialog');
        if(rate_dialog.val() != null)
        {
            rate_dialog.modal('show');
            return 0;
        }

        var next_url = $(this).parent().find('input[name="next"]').val();
        var csrfmiddlewaretoken = $(this).parent().find('input[name="csrfmiddlewaretoken"]').val();
        var post_id = $(this).attr('data-postid');
        
        var rating_div = $(this).parents("#tbl-rating").find('td[data-name="rating-down"] b');
        var rating_up = parseInt($(this).parents("#tbl-rating").find('td[data-name="rating-up"] b').html()); 
        var rating_down = parseInt($(this).parents("#tbl-rating").find('td[data-name="rating-down"] b').html());
        var total_rating_td = $(this).parents("#tbl-rating").find('td[data-name="total-rating"] b');
        
        
        
        $.ajax({
            "type": "POST",
            "url": "/rate_down/",
            "data": {
                "post_id": post_id,
                "csrfmiddlewaretoken": csrfmiddlewaretoken,
                "next": next_url
            },

            "beforeSend": function (xhr, settings) {
                $.ajaxSettings.beforeSend(xhr, settings);
            }
        }).success(function (data) {
            rating_div.hide().fadeIn();
            if (data == "success") {
                rating_down++;
                rating_div.html(rating_down);
            }
             
             var total_rating = rating_up - rating_down;
             total_rating_td.hide().fadeIn();
             total_rating_td.html(total_rating);
        });
    });
}

function delete_post( ) {
    $('span.delete-post a').click(function(){
        $(this).preventDefault = true;
        var clicked_item = $(this);
        var next_url = $(this).parent().find('input[name="next"]').val();
        var csrfmiddlewaretoken = $(this).parent().find('input[name="csrfmiddlewaretoken"]').val();
        var post_id = $(this).attr('data-postid');

        if (confirm("هل انت متأكد من حذف الخبر؟")) {
            $.ajax({
                type: "POST",
                url: "/home/delete_post/",
                data: {
                    "post_id": post_id,
                    "csrfmiddlewaretoken": csrfmiddlewaretoken,
                    "next": next_url
                }
            }).success(function(data){
                if(data=="success"){
                    clicked_item.parents(".panel.panel-default").remove();
                }
            });
        }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});