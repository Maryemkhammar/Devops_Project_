document.querySelectorAll('#cvForm input, #cvForm textarea').forEach(input => {
    input.addEventListener('input', async () => {
        const form = document.getElementById('cvForm');
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        const res = await fetch('/preview', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const html = await res.text();
        document.getElementById('preview').innerHTML = html;
    });
});
