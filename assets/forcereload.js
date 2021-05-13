document.load = function() {
  fetch(window.location.href, {method: 'HEAD', cache: "no-store"}).then(
    function(response) {
      let cc = response.headers.get("cache-control")
      if (cc.includes("immutable"))  // pages stuck in cache contain
        window.location.reload(true);  // force
      });
}