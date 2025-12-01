document.addEventListener("DOMContentLoaded", () => {

    const cpfInput = document.querySelector("input[name='cpf']");
    const alturaInput = document.querySelector("input[name='altura']");
    const form = document.getElementById("form-imc");

    if (cpfInput) {
        cpfInput.addEventListener("input", () => {
            let value = cpfInput.value.replace(/\D/g, ""); // remove tudo que não for número

            if (value.length > 11) value = value.slice(0, 11);

            // aplica formatação
            value = value.replace(/(\d{3})(\d)/, "$1.$2");
            value = value.replace(/(\d{3})(\d)/, "$1.$2");
            value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");

            cpfInput.value = value;
        });
    }

    if (alturaInput) {
        alturaInput.addEventListener("input", () => {
            let v = alturaInput.value.replace(/\D/g, ""); // só números

            if (v.length >= 2) {
                v = v[0] + "." + v.substring(1); // poe a merda do ponto pra nao ter que mexer no models
            }

            alturaInput.value = v;
        });
    }

    if (form) {
        form.addEventListener("submit", () => {

            // limpa o cpf
            if (cpfInput) {
                cpfInput.value = cpfInput.value.replace(/\D/g, "");
            }
        });
    }

});
