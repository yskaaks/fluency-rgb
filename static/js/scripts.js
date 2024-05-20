document.getElementById('generateButton').addEventListener('click', function() {
    var colorImage = document.getElementById('colorImage');
    colorImage.src = '/generate?' + new Date().getTime(); // Add a unique timestamp to prevent caching
});
