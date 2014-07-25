$(document).ready(function() {

var ETSY_API_KEY = 'rkohg59oxwmar76a3lq2jkhx';


var etsy_color = "7f7fb8";
var count = 0;
$('#colorSelector').ColorPicker({
	color: '#0000ff',
	onShow: function (colpkr) {
		$(colpkr).fadeIn(500);
		return false;
	},
	onHide: function (colpkr) {
		$(colpkr).fadeOut(500);
		return false;
	},
	onChange: function (hsb, hex, rgb) {
        etsy_color = "";
//        console.log('firing ' + hex);
        $('body').css('backgroundColor', '#' + hex);
        $('#colorSelector div').css('backgroundColor', '#' + hex);
        etsy_color = hex;
    },
    onSubmit: function (hsb, hex, rgb) {
        etsy_color = "";
        etsy_color = hex;
        $.ajax({
            url: 'https://openapi.etsy.com/v2/listings/active.js?api_key='
                + ETSY_API_KEY + '&color='+ etsy_color + '&limit=1&color_accuracy=10&includes=MainImage',
            type: 'GET',
            dataType: 'jsonp',
            success: function(response) {
//                console.log('color: '+ etsy_color);
//                console.log('a'+response.results[0].title);
                var item = {};
                item = response.results[0];
                item.etsy_color = etsy_color;
                displayItem(item);
//                var itemInfo = {};
//                itemInfo.title = item.title;
//                itemInfo.image_url = item.MainImage.url_75x75;
//                itemInfo.etsy_id = item.listing_id;
//                itemInfo.price = item.price;
//                itemInfo.listing_url = item.url;
//                itemInfo.category_path = item.category_path;
//                itemInfo.tags = item.tags;
//                itemInfo.style = item.style;
//                itemInfo.description = item.description;
//                $('#displayItemsBox').append('<img src="'+itemInfo.image_url+'"> <h1 style="display:inline-block;background-color:#'+etsy_color+'">' + itemInfo.title + '</h1> <div style="display:inline-block;height:30px;width:30px;background-color:#'+etsy_color+'"></div>');
//                console.log(movieInfo);

//                $('#saveMovie').show();
                etsy_color = "";
            },
            error: function(error_response) {
                console.log('b'+error_response);
            }
        });
	}
});

var displayItem = function(item) {
    var itemInfo = {};
    itemInfo.title = item.title;
    itemInfo.image_url = item.MainImage.url_570xN;
    itemInfo.etsy_id = item.listing_id;
    itemInfo.price = item.price;
    itemInfo.listing_url = item.url;
    itemInfo.category_path = item.category_path;
    itemInfo.tags = item.tags;
    itemInfo.style = item.style;
    itemInfo.description = item.description;
    itemInfo.etsy_color = item.etsy_color;
    itemInfo = JSON.stringify(itemInfo);
    $.ajax({
        url: '/new_item/',
        type: 'POST',
        dataType: 'html',
        data: itemInfo,
        success: function (item_response) {
//            console.log('b'+ movie_response);
            $('#displayItemsBox').append(item_response);
        },
        error: function(error_response) {
            console.log(error_response);
        }
    });
};

    var postMovie = function(movieInfo) {
    movieInfo = JSON.stringify(movieInfo);
    $.ajax({
        url: '/new_movie/',
        type: 'POST',
        dataType: 'html',
        data: movieInfo,
        success: function (movie_response) {
//            console.log('b'+ movie_response);
            $('.movieInfoContainer').append(movie_response);
        },
        error: function(error_response) {
            console.log(error_response);
        }
    });
};

// TOGGLE SYNOPSIS
$(document).on('click', '.showhide', function() {
    $(this).toggleClass('description');
});


$('#getOne').on('click', function() {
    $.ajax({
        url: 'https://openapi.etsy.com/v2/listings/interesting.js?api_key='
            + ETSY_API_KEY + '&color_triplet='+ etsy_color + '&color_wiggle=5',
        type: 'GET',
        dataType: 'jsonp',
            success: function(response) {
                console.log('b'+response);
                console.log('colorb: '+etsy_color);
                console.log('b'+response.results[0].title);
                var item = {};
                item = response.results[0];
                var itemInfo = {};
                itemInfo.title = item.title;
                itemInfo.etsy_id = item.listing_id;
                itemInfo.price = item.price;
                itemInfo.listing_url = item.url;
                itemInfo.category_path = item.category_path;
                itemInfo.tags = item.tags;
                itemInfo.style = item.style;
                itemInfo.description = item.description;
                $('#displayItemsBox').append('<h1>'+itemInfo.title+'</h1>');
//                console.log(movieInfo);

//                $('#saveMovie').show();
            },
        error: function(error_response) {
            console.log('b'+error_response);
        }
    });
});

// MORE INFO BUTTON
$(document).on('click', '#moreInfo', function() {
    $(this).siblings('.moreInfoBox').toggle('slow');
    $(this).text(function(i, text){
        return text === "More Information" ? "Hide Information" : "More Information";
    });
});


//
//
//$('#colorpickerHolder2').ColorPicker({
//    flat: true,
//    color: '#00ff00',
//    onSubmit: function(hsb, hex, rgb) {
//        $('#colorSelector2 div').css('backgroundColor', '#' + hex);
//    }
//});
//$('#colorpickerHolder2>div').css('position', 'absolute');
//var widt = false;
//$('#colorSelector2').bind('click', function() {
//    $('#colorpickerHolder2').stop().animate({height: widt ? 0 : 173}, 500);
//    widt = !widt;
//});


});
