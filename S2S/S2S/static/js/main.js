// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("toTop").style.display = "block";
    } else {
        document.getElementById("toTop").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

//upload image
function upload_img(input) {
	if (input.files && input.files[0]) {
		var reader = new FileReader();
		reader.onload = function (e) {
		$('#img_id').attr('src', e.target.result);
		}
		reader.readAsDataURL(input.files[0]);
	}
}

// like and dislike function
$( ".like-btn" ).click( function () {
	var element = this
 	var article_id = $(element).closest("#article").attr("article-id");
	$.ajax({
		type: "GET",
		url: "/blog/like/",
		data:{"article_id":article_id},
		success: function(data){
			if (data.is_liked == 1){
				$(element).removeClass("my-btn-color").addClass("dislike");
			}
			else{
				$(element).removeClass("dislike").addClass("my-btn-color");
			}
			$(element).siblings('.like-nb').text( data.count );
		}
	});
} );

// follow and unfollow function
$( ".follow-btn" ).click( function () {
	var element = this
 	var user_id = $(element).closest("#user").attr("user-id");
	$.ajax({
		type: "GET",
		url: "/blog/follow/",
		data:{"user_id":user_id},
		success: function(data){
			if (data.followed == 1){
				$(element).removeClass("btn-primary").addClass("btn-outline-primary");
				$(element).text("Following");
			}
			else{
				$(element).removeClass("btn-outline-primary").addClass("btn-primary");
				$(element).text("Follow");
			}
		}
	});
} );


// pass article id
$( ".comment-btn" ).click( function () {
	var article_id = $(this).closest("#article").attr("article-id");
	$(".modal-body #article-id").val( article_id );
} );

// pass comment id
$( ".reply-btn" ).click( function () {
	var comment_id = $(this).closest("#comment-id").attr("comment-id");
	$(".modal-body #comment-id").val( comment_id );
} );


// make a comment
$( ".comment-submit" ).click( function () {
	var csrfmiddlewaretoken =  $("[name='csrfmiddlewaretoken']").val();
 	var article_id = $("#article-id").val();
 	var comment_content = $("#comment-content").val();
	$.ajax({
		type: "POST",
		url: "/blog/comment/",
		data:{
			"csrfmiddlewaretoken":csrfmiddlewaretoken,
			"article_id":article_id,
			"comment_content":comment_content,
		},
		success: function(data){
			var comment = `<div class="row py-2">
							<div class="col-md-1">
							<div class="square">
							<a href="/blog/profile/` + data.user_id + `"><img class="rounded sqaure-image" src="` + data.image + `"></a>
							</div>
							</div>
							<div class="col-md-10">
							<div>
							<a href="/blog/profile/` + data.user_id + `">` + data.username + `</a><span class="bullet" aria-hidden="true">•</span><small>Just now</small>
							</div>
							<div>
								` + data.comment + `
							</div>
							<div>
							</div>
							</div>
							<div class="col-md-1 text-center">
							<span class="my-btn-color" href="#"><h4><i class="ion-chatbox-working"></i></h4></span>
							</div>
							</div>`
			$("#comment").prepend(comment)
		}
	});

} );

// make a reply
$( ".reply-submit" ).click( function () {
	var csrfmiddlewaretoken =  $("[name='csrfmiddlewaretoken']").val();
 	var comment_id = $(".modal-body #comment-id").val();
 	var reply_content = $("#reply-content").val();
	$.ajax({
		type: "POST",
		url: "/blog/reply/",
		data:{
			"csrfmiddlewaretoken":csrfmiddlewaretoken,
			"comment_id":comment_id,
			"reply_content":reply_content,
		},
		success: function(data){
			var reply = `<div class="row py-2">
						<div class="col-md-1 mt-2">
						<div class="square">
						<a href="/blog/profile/` + data.user_id + `"><img class="rounded sqaure-image" src="` + data.image + `"></a>
						</div>
						</div>
						<div class="col-md-10">
						<div>
						<a href="/blog/profile/` + data.user_id + `">` + data.username + `</a><span class="bullet text-muted">•</span><small class="text-muted">Just now</small>
						</div>
						<div>
						` + data.reply + `
						</div>
						</div>
						</div>`;
			$('[data-id="' + comment_id+ '"]').prepend(reply);
		}
	});

} );