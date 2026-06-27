const themeBtn = document.getElementById("theme-btn");

themeBtn.addEventListener("click", () => {

    document.body.classList.toggle("dark");

    if(document.body.classList.contains("dark")){
        localStorage.setItem("theme","dark");
        themeBtn.innerHTML = "☀️";
    }else{
        localStorage.setItem("theme","light");
        themeBtn.innerHTML = "🌙";
    }

});

window.onload = () => {

    const theme = localStorage.getItem("theme");

    if(theme === "dark"){

        document.body.classList.add("dark");

        themeBtn.innerHTML = "☀️";
    }
};

function showLoader(){

    document
    .getElementById("loader")
    .classList
    .remove("hidden");
}