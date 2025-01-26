document.addEventListener("DOMContentLoaded", function() {
    // Example for interactive charts, implement logic to load data dynamically
    const chartData = {labels: ['Topic 1', 'Topic 2', 'Topic 3'], data: [80, 60, 90]}; 
    
    // Display performance chart (this would ideally be dynamically generated)
    const ctx = document.getElementById('performanceChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: chartData.labels,
            datasets: [{
                label: 'Accuracy',
                data: chartData.data,
                backgroundColor: ['#4CAF50', '#FF9800', '#F44336'],
                borderColor: ['#4CAF50', '#FF9800', '#F44336'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
