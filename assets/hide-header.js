/* When the user scrolls down, hide the navbar. When the user scrolls up, show the header */
const bp = getComputedStyle(document.documentElement).getPropertyValue('--mobile-breakpoint'); 
const mq = window.matchMedia(`(max-width: ${bp})`)
let prev = window.pageYOffset;
window.onscroll = function() {
  if (!mq.matches)
    return
  const cur = window.pageYOffset;
  const header = document.getElementById("book-header")
  if (prev > cur) {
    header.style.transform = "translateY(0)"
  } else {
    header.style.transform = "translateY(-5rem)"
  }
  prev = cur
}