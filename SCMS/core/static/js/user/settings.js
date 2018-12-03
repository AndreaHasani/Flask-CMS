function readFile() {
  if (this.files && this.files[0]) {
    var FR = new FileReader();

    FR.addEventListener("load", function(e) {
      $(".profileimg").attr("src", e.target.result);
      console.log(e.target.result);
    });

    FR.readAsDataURL(this.files[0]);
  }
}

function init() {
  $("#fileinput").trigger("click");
  $("#fileinput").on("change", readFile);
}

$(document).ready(function() {
  $(".password .generate").on("click", function() {
    $(".password input").val(
      Math.random()
        .toString(36)
        .slice(-10)
    );
  });

  $(".profileimg").on("click", init);
});
