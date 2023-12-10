document.getElementById('class-selector').addEventListener('change', function() {
    // let classFields = {{ classes|tojson }};
    let selectedClass = this.value;
    let formFieldsContainer = document.getElementById('form-fields');

    // Clear the current form fields
    formFieldsContainer.innerHTML = '';

    // Generate new form fields
    classFields[selectedClass].forEach(function(field) {
        let label = document.createElement('label');
        label.textContent = field;

        let input = document.createElement('input');
        input.name = field;

        formFieldsContainer.appendChild(label);
        formFieldsContainer.appendChild(input);
    });
});