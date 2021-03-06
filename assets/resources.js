function hide(x) { x.className += ' hidden' }
function show(x) { x.classList.remove('hidden') }

function filter_resources() {
  let t1 = document.getElementById("resource_topic");
  let t2 = document.getElementById("resource_type");
  tags = [t1.options[t1.selectedIndex].value, t = t2.options[t2.selectedIndex].value];
  table = document.getElementById("resource");
  if (tags[0] || tags[1]) {
    Array.from(table.getElementsByTagName("tr")).forEach(hide);
    Array.from(table.getElementsByClassName("header")).forEach(show);
    Array.from(table.getElementsByClassName(tags.join(" "))).forEach(show);
  } else {
    Array.from(table.getElementsByTagName("tr")).forEach(show);
  }
}

window.onload = function() {
  document.getElementById("resource_topic").onchange = filter_resources;
  document.getElementById("resource_type").onchange = filter_resources;
}
