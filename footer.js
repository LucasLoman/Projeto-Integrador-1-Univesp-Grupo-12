class Footer extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
        <footer class="footer_banner">
        <div class="gradient2"></div>
        <img src="Imagens/AutoIta_Banner_Cortada.png" alt="Autoita-logo-footer">
        <div class="texto_footer"><pre>
Fale Conosco!

(15)3531-2467
(15)99690-7899

autoitapecas@gmail.com

Rua Frei Caneca Nº2455, Centro, Itararé SP</pre></div>
    </footer>
    `;
    }
}

customElements.define('footer-component', Footer);