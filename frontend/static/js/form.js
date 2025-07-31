console.log('JS Loaded')

document.addEventListener('DOMContentLoaded' , () => {
    const form = document.getElementById('guidance-form');
    const statusMessage = document.getElementById('form-status');

    form.addEventListener('submit' , async (e) => {
        e.preventDefault();

        // Clear the previous status.
        statusMessage.textContent = '';
        statusMessage.classList.remove('error' , 'success');

        // Collect form data.
        const formData = new FormData(form);
        const payload = {};

        formData.forEach((value, key) => {
            payload[key] = value.trim();

        });

        // Basic frontend validation
        if (!payload.fullName || !payload.email || !payload.phone || !payload.topic || !payload.message) {

            statusMessage.textContent = 'Please fill in all required fields.';
            statusMessage.classList.add('error');
            return;
        }

        // Send the data to the backend.
        try {
            const response = await fetch('/api/advanced-guidance' , {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload)
            });

            if (response.ok) {
                const data = await response.json();
                statusMessage.textContent = data.message || 'Message sent successfully!';
                statusMessage.classList.add('success');
                form.reset();

            } else {
                const errorData = await response.json();
                statusMessage.textContent = errorData.message || 'Something went wrong. Try again.';
                statusMessage.classList.add('error');
            }
        }

        catch (err) {

            console.error('Error:', err);
            statusMessage.textContent = 'Failed to send. Check your connection.';
            statusMessage.classList.add('error');

        };
    });
});