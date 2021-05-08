window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$','$$'], ['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    renderActions: { addMenu: [] }
  }
};

//window.onload = (event) => {
//  document.querySelectorAll("mjx-container").forEach(function(x){
//    x.parentElement.classList += 'has-jax'})
//};