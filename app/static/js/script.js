$(document).ready(function () {
    $(document).on("click", ".open-edit-profile", function (e) {
      e.preventDefault();
      $("#update_user_profile").modal("show");
    });
    $(document).on("click", ".add-post", function (e) {
      e.preventDefault();
      $("#add_post_modal").modal("show");
    });
  });