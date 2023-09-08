$(function () {
    $("div.cont button").on("click", () => {
        const item1 = "<li>am the first</i>";
        const item2 = $("<li></li>").text("am the second");
        const item3 = $("<li></i>").html("<b>am the the bold one</b>");
        const mydiv = $("<div></div>")
        mydiv.html(`
          <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample" aria-controls="offcanvasExample">
            Button with data-bs-target
          </button>
        `);
        $("div.cont").append(mydiv);
        $("div.cont ul").append(item1, item2, item3);
        });
});
