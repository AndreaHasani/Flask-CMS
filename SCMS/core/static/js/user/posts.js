// A $( document ).ready() block.
$(document).ready(function() {
  $(".editor").trumbowyg();
  $(".password .generate").on("click", function() {
    $('.password input').val(
      Math.random()
        .toString(36)
        .slice(-10)
    );
  });
});

if (typeof Storage !== "undefined") {
  $(".editor").keypress(function() {
    $(this)
      .find(".saved")
      .detach();
  });
  $(".newPost .editor").html(localStorage.getItem("wysiwyg_content"));
  $(".newPost .title").html(localStorage.getItem("wysiwyg_title"));

  $('button[data-func="save"]').click(function() {
    $content = $(".editor").html();
    $title = $(".title").html();
    localStorage.setItem("wysiwyg_content", $content);
    localStorage.setItem("wysiwyg_title", $title);

    var content = $("#editorDemo").html();
    console.log(content);
    var url = "http://0.0.0.0:5000/admin/api/posts/new";
    $.ajax({
      type: "POST",
      url: url,
      data: { title: $title, content: $content }
    });

    $(".editor")
      .append('<span class="saved"><i class="fa fa-check"></i></span>')
      .fadeIn(function() {
        $(this)
          .find(".saved")
          .fadeOut(700);
      });
    $(".editor.saved").remove();
  });

  $('button[data-func="clear"]').click(function() {
    $(".editor").html("");
    localStorage.removeItem("wysiwyg_content", $content);
    localStorage.removeItem("wysiwyg_title", $title);
  });
}
