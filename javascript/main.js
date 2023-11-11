// get theme button from the HTML file
const THEME_BUTTON = document.querySelector(".theme-button");

// get the root HTML tag from the HTML file
const ROOT = document.querySelector("html");

// theme set function
function setTheme(theme_name) {
    if (theme_name == "dark") {
        ROOT.dataset.theme = "dark";
        THEME_BUTTON.innerText = "dark_mode";
        localStorage.setItem("theme", "dark"); // update the value of theme in localStorage

    } else if (theme_name == "light") {
        ROOT.dataset.theme = "light";
        THEME_BUTTON.innerText = "light_mode";
        localStorage.setItem("theme", "light"); // update the value of theme in localStorage
    }
}

// theme toggle function
function toggleTheme() {
    // switch the theme value of ROOT from dark to light or light to dark
    // change the innerText of theme button to change the icon
    if (ROOT.dataset.theme === "light") {
        setTheme("dark");
    } else {
        setTheme("light");
    }

    // css will take care of the rest
}

// define what happens when theme button is clicked
THEME_BUTTON.addEventListener("click", toggleTheme);

// set the starting theme
// search localStorage for a theme value if it is not set then use dark theme
const starting_theme = localStorage.getItem("theme") || "dark";
setTheme(starting_theme);
