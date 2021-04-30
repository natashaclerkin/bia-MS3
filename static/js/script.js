// MaterializeCSS Nav initialization

document.addEventListener('DOMContentLoaded', function () {
     let sidenavs = document.querySelectorAll(".sidenav");
     let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});
});


// MaterializeCSS Select initialization
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
});