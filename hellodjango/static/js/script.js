
function welcome() {
  document.getElementById("content_welcome").style.display = "inline";
  document.getElementById("content_about_me").style.display = "none";
  document.getElementById("content_career").style.display = "none";
  document.getElementById("content_schools").style.display = "none";
  document.getElementById("content_hobbies").style.display = "none";
}

function about_me() {
  document.getElementById("content_welcome").style.display = "none";
  document.getElementById("content_about_me").style.display = "inline";
  document.getElementById("content_career").style.display = "none";
  document.getElementById("content_schools").style.display = "none";
  document.getElementById("content_hobbies").style.display = "none";
}

function career() {
  document.getElementById("content_welcome").style.display = "none";
  document.getElementById("content_about_me").style.display = "none";
  document.getElementById("content_career").style.display = "inline";
  document.getElementById("content_schools").style.display = "none";
  document.getElementById("content_hobbies").style.display = "none";
}

function schools() {
  document.getElementById("content_welcome").style.display = "none";
  document.getElementById("content_about_me").style.display = "none";
  document.getElementById("content_career").style.display = "none";
  document.getElementById("content_schools").style.display = "inline";
  document.getElementById("content_hobbies").style.display = "none";
}

function hobbies() {
  document.getElementById("content_welcome").style.display = "none";
  document.getElementById("content_about_me").style.display = "none";
  document.getElementById("content_career").style.display = "none";
  document.getElementById("content_schools").style.display = "none";
  document.getElementById("content_hobbies").style.display = "inline";
}

