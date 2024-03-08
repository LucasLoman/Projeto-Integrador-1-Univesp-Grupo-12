class Header extends HTMLElement {
    constructor () {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
        <nav>
        <ul class="menu">
            <div class="container img">
               <a href="HomePage.html"> <img src="logo_autoita-semfundo.png" alt="Logo_Autoita"> </a>
            </div>
            <li><a href="HomePage.html"><b>Pagina Inicial</b></a></li>
            <li><a href="Forms.html"><b>Trabalhe Conosco</b></a></li>
            <li><a href="Contato.html"><b>Contato</b></a></li>
        </ul>
    </nav>
    `;
    }
}

customElements.define('header-component', Header);