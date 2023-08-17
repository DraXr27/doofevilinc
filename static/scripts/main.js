var prevScrollpos = window.scrollY;
var sidebar_m = document.getElementById("main_sidebar")
window.onscroll = function() {
    var currentScrollPos = window.scrollY;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("top_bar").style.top = "0";
    } else {
        document.getElementById("top_bar").style.top = "-6ch";
    }
    prevScrollpos = currentScrollPos;
}



window.onload = function() {
    popup = document.getElementById("mdc-dialog");
    if (popup) {
        if (popup.style.display == "block") {
            body_block()
        }
    }
}



function open_spc_options(thisbtn) {
    button = thisbtn
    buttons = document.getElementsByClassName("option_btn")
    menus = document.getElementsByClassName("menu-menu")

    for (var i = 0; i < buttons.length; i++) {
        if (buttons[i] == button) {
            menus[i].style.display = menus[i].style.display === "block" ? 'none' : 'block';
        }
        else {
            menus[i].style.display = menus[i].style.display === "none" ? 'none' : 'none';
        }
    }
}


function closeall_spc_options() {
    menus = document.getElementsByClassName("menu-menu")

    for (var i = 0; i < menus.length; i++) {
        menus[i].style.display = menus[i].style.display === "none" ? 'none' : 'none';
    }
}



function this_popup_openclose(thisbtn) {
    button = thisbtn
    buttons = document.getElementsByClassName("delete-btn")
    popups = document.getElementsByClassName("mdc-dialog")

    for (var i = 0; i < buttons.length; i++) {
        if (buttons[i] == button) {
            popups[i].style.display = popups[i].style.display === "block" ? 'none' : 'block';
        }
        else {
            popups[i].style.display = popups[i].style.display === "none" ? 'none' : 'none';
        }
    }

    closeall_spc_options()
}


function popup_openclose() {
    popup = document.getElementById("mdc-dialog");
    main = document.getElementById("body");
    sidebar = document.getElementById("main_sidebar");

    popup.style.display = popup.style.display === "block" ? 'none' : 'block';
    main.style.overflowY = main.style.overflowY === "hidden" ? 'scroll' : 'hidden';
    sidebar.style.width = sidebar.style.width === "0ch" ? '27px' : '0ch';
}


function body_block() {
    main = document.getElementById("body");

    main.style.overflowY = main.style.overflowY === "hidden" ? 'hidden' : 'hidden';
}


function sidebar_openclose() {
    popup = document.getElementById("mdc-dialog");
    menus = document.getElementsByClassName("menu-menu")

    if (menus) {
        for (var i = 0; i < menus.length; i++) {
            if (menus[i].style.display = 'block') {
                menus[i].style.display = 'none'
            }
        }
    }

    if (popup) {

        if (popup.style.display == "block") {
            body_block()
        }

        else {
            sidebar_openclosenover()
        }
    }
    else {
        sidebar_openclosenover()
    }
}

function sidebar_openclosenover() {
    sidebar = document.getElementById("main_sidebar");
    main = document.getElementById("body");
    cont = document.getElementById("ac_cont");
    image = document.getElementById('image_bg');
    icon = document.getElementById('open_sidebar');
    imagedoof = document.getElementById('image_doof');
    filled_butt = document.getElementById('filled_butt');
    icon.innerHTML = icon.innerHTML === "close" ? 'menu' : 'close';
    sidebar.style.width = sidebar.style.width === "27ch" ? '0px' : '27ch';
    main.style.overflowY = main.style.overflowY === "hidden" ? 'scroll' : 'hidden';
    main.style.backgroundColor = main.style.backgroundColor === "rgba(0, 0, 0, 0.8)" ? 'white' : 'rgba(0, 0, 0, 0.8)';
    cont.style.backgroundColor = cont.style.backgroundColor === "rgba(40, 40, 40, 0.5)" ? 'white' : 'rgba(40, 40, 40, 0.5)';
    image.style.filter = image.style.filter === "blur(4px) brightness(20%)" ? 'blur(4px) brightness(95%)' : 'blur(4px) brightness(20%)';
    if (filled_butt != null) {
        filled_butt.style.backgroundColor = filled_butt.style.backgroundColor === "rgba(72, 0, 160, 0.7)" ? '#6200ee' : 'rgba(72, 0, 160, 0.7)';
        filled_butt.style.color = filled_butt.style.color === "gray" ? 'white' : 'gray';
    }
    if (imagedoof != null) {
        imagedoof.style.filter = imagedoof.style.filter === "brightness(20%)" ? 'brightness(95%)' : 'brightness(20%)';
    }
}

function sidebar_close() {
    sidebar = document.getElementById("main_sidebar");
    main = document.getElementById("body");
    cont = document.getElementById("ac_cont");
    image = document.getElementById('image_bg');
    icon = document.getElementById('open_sidebar');
    imagedoof = document.getElementById('image_doof');
    filled_butt = document.getElementById('filled_butt');
    icon.innerHTML = icon.innerHTML === "menu" ? 'menu' : 'menu';
    sidebar.style.width = sidebar.style.width === "0" ? '0' : '0';
    main.style.overflowY = main.style.overflowY === "scroll" ? 'scroll' : 'scroll';
    main.style.backgroundColor = main.style.backgroundColor === "white" ? 'white' : 'white';
    cont.style.backgroundColor = cont.style.backgroundColor === "white" ? 'white' : 'white';
    image.style.filter = image.style.filter === "blur(4px) brightness(95%)" ? 'blur(4px) brightness(95%)' : 'blur(4px) brightness(95%)';
    if (filled_butt != null) {
    filled_butt.style.backgroundColor = filled_butt.style.backgroundColor === "#6200ee" ? '#6200ee' : '#6200ee';
    filled_butt.style.color = filled_butt.style.color === "white" ? 'white' : 'white';
    }
    if (imagedoof != null) {
        imagedoof.style.filter = imagedoof.style.filter === "brightness(95%)" ? 'brightness(95%)' : 'brightness(95%)';
    }
}


function pass_show_hide() {
    psw_btn = document.getElementById("show_psw_icon");
    psw_text = document.getElementById("user_password");
    if (psw_btn && psw_text) {
        psw_text.type = psw_text.type === "text" ? 'password' : 'text';
        psw_btn.innerHTML = psw_btn.innerHTML === "visibility_off" ? 'visibility' : 'visibility_off';
    }
}