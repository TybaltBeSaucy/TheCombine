// Placeholder data for User Bets
const userBetsData = [
    { betId: 1, amount: 50, status: 'Active' },
    { betId: 2, amount: 30, status: 'Completed' },
    { betId: 3, amount: 20, status: 'Pending' },
];

// Placeholder data for Live Events
const liveEventsData = [
    { eventId: 101, name: 'Football Match', status: 'In Progress' },
    { eventId: 102, name: 'Basketball Game', status: 'Scheduled' },
    { eventId: 103, name: 'Tennis Tournament', status: 'Completed' },
];

// Function to populate the table with data
function populateTable(tableId, data) {
    const table = document.getElementById(tableId);
    const tbody = table.querySelector('tbody');

    // Clear existing rows
    tbody.innerHTML = '';

    // Populate the table with data
    data.forEach(item => {
        const row = document.createElement('tr');
        Object.values(item).forEach(value => {
            const cell = document.createElement('td');
            cell.textContent = value;
            row.appendChild(cell);
        });
        tbody.appendChild(row);
    });
}

// Call the function to populate User Bets and Live Events tables
populateTable('userBetsTable', userBetsData);
populateTable('liveEventsTable', liveEventsData);
