class Header extends HTMLElement {
    constructor () {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/solid.css"
        integrity="sha384-Tv5i09RULyHKMwX0E8wJUqSOaXlyu3SQxORObAI08iUwIalMmN5L6AvlPX2LMoSE" crossorigin="anonymous" />
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/fontawesome.css"
        integrity="sha384-jLKHWM3JRmfMU0A5x5AkjWkw/EYfGUAGagvnfryNV3F9VqM98XiIH7VBGVoxVSc7" crossorigin="anonymous" />
        <nav>
        <ul class="menu">
            <div class="container img">
               <a href="HomePage.html"> <img src="Imagens/logo_autoita-cortada.png" alt="Logo_Autoita"> </a>
            </div>
            <li><a href="HomePage.html"><b><span class="fa fa-home"></span>
            <span>Página Inicial</span></b></a></li>
            <li><a href="Forms.html"><b><span class="fa fa-search"></span>
            <span>Trabalhe Conosco</span></b></a></li>
            <li><a href="Contato.html"><b><span class="fa fa-phone"></span>
            <span>Contato</span></b></a></li>
        </ul>
    </nav>
    `;
    }
}

customElements.define('header-component', Header);