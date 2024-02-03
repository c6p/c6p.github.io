document.addEventListener("DOMContentLoaded", () => {
  const koji = document.getElementsByClassName('koji');

  const archiveDialog = document.getElementById('archiveDialog');
  archiveDialog.addEventListener('click', () => archiveDialog.close());

  for (let a of koji) {
    a = a.querySelector("a") ?? a;
    const href = a.href;
    a.addEventListener('click', () => {
      archiveDialog.showModal()
      archiveDialog.querySelector("replay-web-page").url = href;
      return false;
    });
    a.href = "#";
    a.target = "_self";
  };


  archiveDialog.addEventListener('close', () => {
    archiveDialog.querySelector("replay-web-page").url = "";
  });
})