// A $( document ).ready() block.
$(document).ready(function() {
  var post = $(".post .left .top").attr("id");

  if (typeof post !== "undefined") {
    var content = $(".editor .holder").html();
    $(".editor").trumbowyg();
    $(".editor").trumbowyg("html", content);
  } else {
    $(".editor").trumbowyg();
  }

  $(".password .generate").on("click", function() {
    $(".password input").val(
      Math.random()
        .toString(36)
        .slice(-10)
    );
  });

  // Post Tags
  $(".tags button").click(function() {
    var tag = $(".tags input").val();
    var check = $(".tags-added p").length;
    if (check === 0) {
      $(".tags-added").append("<p>" + tag + "</p>");
    } else {
      $(".tags-added").append(", <p>" + tag + "</p>");
    }
  });
});

// Accordion

$(document).ready(function() {
  $(".set > a").addClass("active");
  $(".set > div").show();
  $(".set > a").on("click", function() {
    if ($(this).hasClass("active")) {
      $(this).removeClass("active");
      $(this)
        .siblings(".content")
        .slideUp(200);
      $(".set > a i")
        .removeClass("fa-minus")
        .addClass("fa-plus");
    } else {
      $(".set > a i")
        .removeClass("fa-minus")
        .addClass("fa-plus");
      $(this)
        .find("i")
        .removeClass("fa-plus")
        .addClass("fa-minus");
      $(this).addClass("active");
      $(this)
        .siblings(".content")
        .slideDown(200);
    }
  });
});

// Checked Checkbox
var checked = $('input[name="chk[]"]:checked');

// if (typeof Storage !== "undefined") {
//   $(".editor").keypress(function() {
//     $(this)
//       .find(".saved")
//       .detach();
//   });
//   $(".newPost .editor").html(localStorage.getItem("wysiwyg_content"));
//   $(".newPost .title").html(localStorage.getItem("wysiwyg_title"));

//   $('button[data-func="save"]').click(function() {
//     $content = $(".editor").html();
//     $title = $(".title").html();
//     localStorage.setItem("wysiwyg_content", $content);
//     localStorage.setItem("wysiwyg_title", $title);

//     var content = $("#editorDemo").html();
//     console.log(content);
//     var url = "http://0.0.0.0:5000/admin/api/posts/new";
//     $.ajax({
//       type: "POST",
//       url: url,
//       data: { title: $title, content: $content }
//     });

//     $(".editor")
//       .append('<span class="saved"><i class="fa fa-check"></i></span>')
//       .fadeIn(function() {
//         $(this)
//           .find(".saved")
//           .fadeOut(700);
//       });
//     $(".editor.saved").remove();
//   });

//   $('button[data-func="clear"]').click(function() {
//     $(".editor").html("");
//     localStorage.removeItem("wysiwyg_content", $content);
//     localStorage.removeItem("wysiwyg_title", $title);
//   });
// }
