document.addEventListener('DOMContentLoaded', function() {
    var previewButtons = document.querySelectorAll('.preview-btn');
    var previewModal = document.getElementById('previewModal');
    var csvPreviewContent = document.getElementById('csvPreviewContent');

    previewButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var csvUrl = button.getAttribute('data-csv');
            console.log('Fetching CSV from URL:', csvUrl);  // Debug log
            fetch(csvUrl)
                .then(response => response.text())
                .then(data => {
                    csvPreviewContent.innerHTML = convertCSVToHTMLTable(data);
                    $('#previewModal').modal('show');
                })
                .catch(error => console.error('Error fetching CSV:', error));
        });
    });

    $('#previewModal').on('hidden.bs.modal', function() {
        csvPreviewContent.innerHTML = '';
    });

    // Image preview functionality
    var imagePreviewButtons = document.querySelectorAll('.preview-img');
    var imagePreviewModal = document.getElementById('imageModal');
    var imagePreviewContent = document.getElementById('modalImage');

    if (imagePreviewContent) {
        imagePreviewButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                var imgSrc = button.getAttribute('src');
                console.log('Image clicked:', imgSrc);  // Debug log
                if (imgSrc) {
                    imagePreviewContent.src = imgSrc;
                    $('#imageModal').modal('show');
                }
            });
        });

        $('#imageModal').on('hidden.bs.modal', function() {
            imagePreviewContent.src = '';
        });

        // Zoom functionality for image preview
        imagePreviewContent.addEventListener('click', function() {
            if (imagePreviewContent.style.transform === 'scale(2)') {
                imagePreviewContent.style.transform = 'scale(1)';
            } else {
                imagePreviewContent.style.transform = 'scale(2)';
            }
        });
    }

    // Load and display the overview CSV
    var overviewCsvContent = document.getElementById('overviewCsvContent');
    if (overviewCsvContent) {
        fetch('data_statistics/institution_overview.csv')
            .then(response => response.text())
            .then(data => {
                overviewCsvContent.innerHTML = convertCSVToHTMLTable(data, 'available_distance_km');
            })
            .catch(error => console.error('Error fetching overview CSV:', error));
    }

    // Dark mode toggle
    const toggleBtn = document.createElement('button');
    toggleBtn.classList.add('toggle-btn');
    toggleBtn.textContent = "🌙"; // Moon icon for dark mode
    toggleBtn.title = "Toggle Dark Mode";

    const header = document.querySelector('header .container');
    header.appendChild(toggleBtn);

    // Check the current theme and apply it
    const storedTheme = localStorage.getItem('theme');
    if (storedTheme) {
        document.body.classList.add(storedTheme);
        if (storedTheme === 'dark-mode') {
            toggleBtn.textContent = "🌞"; // Sun icon for light mode
        }
    }

    toggleBtn.addEventListener('click', function () {
        document.body.classList.toggle('dark-mode');
        const isDarkMode = document.body.classList.contains('dark-mode');

        // Update the button text
        toggleBtn.textContent = isDarkMode ? "🌞" : "🌙";

        // Save the current theme to localStorage
        localStorage.setItem('theme', isDarkMode ? 'dark-mode' : 'light-mode');
    });

    function convertCSVToHTMLTable(csv, highlightColumn) {
        const rows = csv.split('\n');
        let html = '<table class="table table-striped"><thead><tr>';

        // Add headers
        const headers = parseCSVLine(rows[0]);
        headers.forEach(header => {
            html += `<th>${header.trim()}</th>`;
        });
        html += '</tr></thead><tbody>';

        // Add rows
        for (let i = 1; i < rows.length; i++) {
            const cells = parseCSVLine(rows[i]);
            html += '<tr>';
            cells.forEach((cell, index) => {
                if (highlightColumn && headers[index].trim() === highlightColumn && parseFloat(cell.trim()) === 0.0) {
                    html += `<td style="background-color: #ffdddd;">${cell.trim()}</td>`;
                } else {
                    html += `<td>${cell.trim()}</td>`;
                }
            });
            html += '</tr>';
        }
        html += '</tbody></table>';
        return html;
    }

    function parseCSVLine(line) {
        const regex = /,(?=(?:(?:[^"]*"){2})*[^"]*$)/;
        return line.split(regex).map(cell => cell.replace(/(^"|"$)/g, ''));
    }

    const hamburgerBtn = document.getElementById('hamburger-btn');
    const navbar = document.getElementById('navbar');

    hamburgerBtn.addEventListener('click', () => {
        hamburgerBtn.classList.toggle('active');
        navbar.classList.toggle('active');
    });
});
