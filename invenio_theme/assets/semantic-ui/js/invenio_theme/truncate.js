import $ from "jquery";

$(".truncate-button").on("click", function () {
  const $clickButton = $(this);
  const siblings = $clickButton.siblings();
  siblings.first().toggleClass("truncate-2");
  $clickButton.toggle();
  siblings.eq(1).toggle();
});

const ps = document.querySelectorAll(".truncate-container .truncate-text");
const observer = new ResizeObserver((entries) => {
  for (let entry of entries) {
    const truncate =
      Math.ceil(entry.target.scrollHeight) > Math.ceil(entry.contentRect.height) ? "add" : "remove";
    entry.target.classList[truncate]("truncate-2");
    if (truncate === "add") {
      $(entry.target).siblings().first().show();
    }
  }
});
ps.forEach((p) => {
  observer.observe(p);
});
