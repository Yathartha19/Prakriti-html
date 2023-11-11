// get theme button from the HTML file
const THEME_BUTTON = document.querySelector(".theme-button");

// get the root HTML tag from the HTML file
const ROOT = document.querySelector("html");

// define what happens when theme button is clicked
THEME_BUTTON.addEventListener("click", () => {

    // switch the theme value of ROOT from dark to light or light to dark
    // change the innerText of theme button to change the icon
    if (ROOT.dataset.theme === "dark") {
        ROOT.dataset.theme = "light";
        THEME_BUTTON.innerText = "dark_mode";
    }

    else {
        ROOT.dataset.theme = "dark";
        THEME_BUTTON.innerText = "light_mode";
    }

    // css will take care of the rest
});
