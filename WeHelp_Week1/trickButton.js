let btn = document.querySelector(".burger");
let btn2 = document.querySelector(".x");
let btn3 = document.querySelector(".MenuItems-buttonMode");
//點擊漢堡圖示時
btn.addEventListener("click", function () {
  console.log("click!");
  //MenuItems-buttonMode打開
  btn3.style.display = "flex";
});
//點擊X時
btn2.addEventListener("click", function () {
  console.log("click!");
  //MenuItems-buttonMode關閉
  btn3.style.display = "none";
});
